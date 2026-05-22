from administrador.database import json_manager as json_manager
from administrador.database import auth_pacientes

def menu_paciente():
  while True:
    print("""================================
      GERENCIAR PACIENTES
    ================================""")
    print("1 - Listar pacientes")
    print("2 - Buscar pacientes")
    print("0 - Voltar")

    op = input("Selecionar opção: ")

    if op == "1":
      auth_pacientes.list_pacientes()
    elif op == "2":
      auth_pacientes.search_paciente()
    elif op == "0":
      break