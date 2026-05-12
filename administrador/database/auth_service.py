from administrador.database import json_manager as json_manager
from administrador.services import id_generator as id_generator


def auth_user(user, senha):
    usuarios = json_manager.carregar_json("administrador/data/usuarios.json")
    for u in usuarios:
      if u["usuario"] == user and u["senha"] == senha:
        return u
        break
    return False

def cadastrar_user(caminho):
  usuario = input("Usuario: ")
  senha = input("Senha: ")

  print("1 - Admin")
  print("2 - Recepcionista")
  print("3 - Médico")

  nivel = input("Nível: ")
  if nivel not in ["1", "2", "3"]:
    print("Valor inválido:")
    nivel = input("Nível: ")

  if nivel == "1": nivel = "Administrado"
  elif nivel == "2": nivel = "Recepcionista"
  elif nivel == "3": nivel = "Médico"
  dados = {
    "usuario": usuario,
    "senha": senha,
    "nivel": nivel,
    "id": id_generator.id_generator(caminho)
  }

  json_manager.adicionar_json(caminho,dados)

  return dados

def check_user(id_user):
  usuarios = json_manager.carregar_json('administrador/data/usuarios.json')

  for u in usuarios:
    if id_user == u["id"]:
      return True

  return False