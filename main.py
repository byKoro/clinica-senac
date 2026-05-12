import administrador.database.auth_service as auth_service
import administrador.menus.menu_login as menu
import administrador.database.json_manager as json_manager
import administrador.menus.menu_admin as menu_admin
import Recepcionista.Funções_recepcionista as Recepcionista

usuario = {}

while True:
  op = menu.menu_login()

  if op == '1':
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    autenticado = auth_service.auth_user(usuario,senha)

    while not autenticado:
      print("Usuário ou senha inválido")
      usuario = input("Usuário: ")
      senha = input("Senha: ")
      usuario = auth_service.auth_user(usuario,senha)

  elif op == '0':
    break

  if usuario["nivel"] == "Administrador":
    menu_admin.menu_admin()

  if usuario["nivel"] == "Recepcionista":
    Recepcionista.