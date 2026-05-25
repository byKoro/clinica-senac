import administrador.database.auth_user as auth_user
import administrador.menus.menu_login as menu
import administrador.menus.menu_admin as menu_admin
import Recepcionista.Menus.menu_pacientes as menu_pacientes

usuario = {}

while True:
  op = menu.menu_login()

  if op == '1':
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    autenticado = auth_user.auth_user(usuario,senha)

    while not autenticado:
      print("Usuário ou senha inválido")
      usuario = input("Usuário: ")
      senha = input("Senha: ")
      autenticado = auth_user.auth_user(usuario,senha)

    usuario = autenticado

  elif op == '0':
    break

  if usuario["nivel"] == "Administrador":
    menu_admin.menu_admin()

  elif usuario["nivel"] == "Recepcionista":
    menu_pacientes.menu_pacientes()