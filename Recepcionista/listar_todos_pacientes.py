from administrador.database import json_manager

def listar_todos():

    pacientes = json_manager.carregar_json(
        "data/pacientes.json"
    )

    for paciente in pacientes:
        print(
            f'ID: {paciente["id"]} | '
            f'Nome: {paciente["nome"]} | '
            f'Idade: {paciente["idade"]}'
        )

listar_todos()