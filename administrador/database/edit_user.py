from administrador.database import json_manager as json_manager
from administrador.database import auth_service as auth_service
from administrador.services import list_user as list_user


def editar_user():
  list_user.list_user()
  while True: 
    print("0 - Voltar")
    id_user = input("Escolha um usuario pelo ID: ")
    if id_user == "0": break # Voltar
    while not auth_service.check_user(int(id_user)):
      print("Usuário não encontrado")
      id_user = input("Escolha um usuario pelo ID: ")
    
    for i, u in enumerate(usuarios_lista):
      if int(id_user) == u["id"]:
        user = u
        index = i
        break


    while True:
      print("1 - Nome de usuário: ")
      print("2 - Senha: ")
      print("3 - Nível: ")
      print("0 - Salvar")
      op = input("O que deseja editar: ")

      if op == "1":
        usuario = input("Nome de usuário: ")
        user["usuario"] = usuario

      elif op == "2":
        senha = input("Digíte a nova senha: ")
        user["senha"] = senha

      elif op == "3":
        print("1 - Adminitrador")
        print("2 - Recepcionista")
        print("3 - Médico")

        nivel = input("Escolha um nível: ")
        while nivel not in ["1","2","3"]:
          print("Valor inválido")
          nivel = input("Escolha um nível: ")
          
        if nivel == "1": nivel = "Administrador"
        elif nivel == "2": nivel = "Recepcionista"
        elif nivel == "3": nivel = "Médico"

        user["nivel"] = nivel

      elif op == "0":
        usuarios_lista[index] = user
        json_manager.salvar_json('data/usuarios.json', usuarios_lista)
        print("Editado com sucesso!")
        break

def del_user():
  while True:
    list_user.list_user()
    user_list = json_manager.carregar_json("data/usuarios.json")
    print("0 - Voltar")
    op = input("Escolha um usuário pelo id: ")
    if op == "0": break
    while not auth_service.check_user(int(op)):
      print("Usuário inválido")
      op = input("Escolha um usuário pelo id: ")

    for i, u in enumerate(user_list):
      if u["id"] == int(op):
        index = i
        break
    
    user_list.pop(index)
    json_manager.salvar_json('data/usuarios.json', user_list)
    print("Usuário deletado com sucesso!")