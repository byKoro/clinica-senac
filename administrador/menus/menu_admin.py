from administrador.menus import menu_usuarios as menu_usuarios
from administrador.menus import menu_medicos  as menu_medicos
def menu_admin():
  while True:
    print(
    """================================
        MENU ADMIN
    ================================""")
    print("1 - Usuários")
    print("2 - Médicos")
    print("3 - Pacientes")
    print("4 - Consultas")
    print("5 - Relatórios")
    print("0 - Logout")

    op = input("Escolha uma opção: ")

    if op == "1":
      menu_usuarios.menu_usuarios()
    elif op == "2":
      menu_medicos.menu_medicos()
    elif op == "0":
      break
