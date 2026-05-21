from administrador.database import json_manager as json_manager
def list_user():
  usuarios_lista = json_manager.carregar_json('data/usuarios.json')
  for i in usuarios_lista:
    print(f"id: {i["id"]} - usuario: {i["usuario"]}")