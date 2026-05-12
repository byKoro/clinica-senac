from administrador.database import json_manager as json_manager
def id_generator(arquivo):
    arquivo_ids = json_manager.carregar_json(arquivo)

    if not arquivo_ids:
        return 1

    id_max = arquivo_ids[0]["id"]


    for i in arquivo_ids:
        if id_max < i["id"] : id_max = i["id"]

    return id_max + 1