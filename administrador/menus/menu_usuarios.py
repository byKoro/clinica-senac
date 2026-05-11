from administrador.database import auth_service as auth_service
from administrador.database import edit_user as edit_user
from administrador.database import json_manager as json_manager
from administrador.services import list_user as list_user

def menu_usuarios():
  while True:
    print("""================================
      GERENCIAR USUÁRIOS
    ================================""")
    print("1 - Cadastrar")
    print("2 - Editar usuário")
    print("3 - Excluir usuário")
    print("4 - Listar usuários")
    print("0 - Voltar")

    op = input("Selecionar opção: ")

    if op == "1":
      auth_service.cadastrar_user('administrador/data/usuarios.json')
      print("Cadastrado com sucesso!")

    elif op == "2":
      edit_user.editar_user()

    elif op == "3":
      edit_user.del_user()

    elif op == "4":
      list_user.list_user()

    elif op == "0":
      break