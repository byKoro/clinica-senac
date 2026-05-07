from administrador.database import json_manager as json_manager
def auth_user(user, senha):
    usuarios = json_manager.carregar_json("administrador/data/usuarios.json")
    for u in usuarios:
        if u["usuario"] == user and u["senha"] == senha:
            return True
            break
    return False
