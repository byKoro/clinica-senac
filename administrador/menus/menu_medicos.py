from administrador.database import auth_service as auth_service
from administrador.database import auth_medic as list_medic
from administrador.database import auth_medic as cad_medic
from administrador.database import auth_medic as del_medic

def menu_medicos():
  while True:
    print("""================================
      GERENCIAR MÉDICOS
    ================================""")
    print("1 - Cadastrar")
    print("2 - Editar médicos")
    print("3 - Excluir médicos")
    print("4 - Listar médicos")
    print("0 - Voltar")

    op = input("Selecionar opção: ")

    if op == "1":
      cad_medic.cad_medic()
    elif op == "2":
      print("BUILDING")
    elif op == "3":
      del_medic.del_medic()
    elif op == "4":
      list_medic.list_medic()
    elif op == "0":
      break