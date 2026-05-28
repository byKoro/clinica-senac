from administrador.database import auth_medic 

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
      auth_medic.cad_medic()
    elif op == "2":
      auth_medic.edit_medic()
    elif op == "3":
      auth_medic.del_medic()
    elif op == "4":
      auth_medic.list_medic()
    elif op == "0":
      break