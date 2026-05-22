from administrador.menus import menu_usuarios as menu_usuarios
from administrador.menus import menu_medicos  as menu_medicos
from administrador.menus import menu_pacientes as menu_paciente
from administrador.menus import menu_consultas as menu_consultas
from administrador.menus import menu_relatorios
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
    while op not in ["0","1","2","3","4","5"]:
      op = input("Opção invalída! Escolha uma opção: ")
    

    if op == "1":
      menu_usuarios.menu_usuarios()
    elif op == "2":
      menu_medicos.menu_medicos()
    elif op == "3":
      menu_paciente.menu_paciente()
    elif op == "4":
      menu_consultas.menu_consultas()
    elif op == "5":
      menu_relatorios.menu_relatorios()
    elif op == "0":
      break
