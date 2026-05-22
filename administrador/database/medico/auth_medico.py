from administrador.services import id_generator as id_generator
from administrador.database import json_manager as json_manager
def cadastrar_medico():
    nome = input("Nome do médico: ")
    especialidade = input("Especialidade do médico: ")
    crm = input("CRM do médico: ")

    medico = {
        "id": id_generator.id_generator("data/medicos.json"),
        "nome": nome,
        "especialidade": especialidade,
        "crm": crm
    }

    print("Médico adicionado com sucesso!")
    json_manager.adicionar_json("data/medicos.json", medico)
    

def edit_medico():
    while True:
        medicos = json_manager.carregar_json("data/medicos.json")

        for m in medicos:
            id_medico = m["id"]
            nome = m["nome"]

            print(f"ID: {id_medico} - Nome: {nome}")
        
        op = int(input("Escolha um médico pelo ID: ")) - 1
        while not json_manager.search_json("id", op, "data/medicos.json"):
            op = int(input("Médico invalído! Escolha um médico pelo ID: "))

        medico = medicos[op]
        print("1 - Nome")
        print("2 - Especialidade")
        print("3 - CRM")
        print("0 - Sair")

        op = input("O que deseja alterar ?: ")
        while op not in ["1","2","3","0"]:
            op = input("Opção invalída! O que deseja alterar ? ")
        
        # Nome
        if op == "1": 
            nome = input("Novo nome: ")
            medico["nome"] = nome
            print("Nome alterado com sucesso!")

        # Especialidade
        elif op == "2":
            especialidade = input("Nova especialidade: ")
            medico["especialidade"] = especialidade
            print("Especialidade alterada com sucesso!")

        # CRM
        elif op == "3":
            crm = input("Novo CRM: ")
            medico["crm"] = crm
            print("CRM alterado com sucesso!")

        # Sair
        elif op == "0":
            break

        print("1 - Sim")
        print("0 - Sair")
        op_ = input("Deseja continuar? ")
        while op_ not in ["0","1"]:
            op_ = input("Opção invalída! Deseja continuar? ")
        
        if op == "0": break
        