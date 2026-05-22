from administrador.database import json_manager as json_manager

def excluir_paciente():

    pacientes = json_manager.carregar_json("data/pacientes.json")

    print("\nLista de pacientes")
    json_manager.list_json("data/pacientes.json")

    nome_busca = input("\nDigite o nome do paciente que deseja excluir: ")

    for paciente in pacientes:

        if paciente["nome"] == nome_busca:

            pacientes.remove(paciente)

            json_manager.salvar_json("data/pacientes.json", pacientes)

            print("Paciente excluído com sucesso!")

            return

    print("Paciente não encontrado!")