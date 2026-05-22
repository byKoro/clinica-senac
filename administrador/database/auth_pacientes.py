from administrador.database import json_manager as json_manager

def list_pacientes():
    pacientes = json_manager.carregar_json("data/pacientes.json")

    for p in pacientes:
        id_paciente = p["id"]
        nome = p["nome"]
        cpf = p["cpf"]

        print(f"ID: {id_paciente} - Nome: {nome} - CPF: {cpf}")

def search_paciente():
    while True:
        pacientes = json_manager.carregar_json("data/pacientes.json")

        print("0 - Sair")
        search = input("Busque um paciente pelo nome: ")

        if search == "0":
            break

        encontrados = False

        for p in pacientes:
            if search.lower() in p["nome"].lower():
                print(
                    f"ID: {p['id']} - Nome: {p['nome']} - "
                    f"Idade: {p['idade']} - CPF: {p['cpf']} - "
                    f"Telefone: {p['telefone']} - Endereço: {p['endereco']}"
                )
                encontrados = True

        if not encontrados:
            print("Nenhum paciente encontrado.")