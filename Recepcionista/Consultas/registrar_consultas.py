from administrador.database import json_manager as json_manager
from administrador.services import id_generator as id_generator


def registrar_consultas():
    while True:
        print("Registre aqui sua consulta: ")

        print("-=-=-=Pacientes=-=-=-=-")
        paciente_lista = json_manager.carregar_json("data/pacientes.json")

        for m in paciente_lista:
            print(f"{m["id"]} - {m["nome"]}")

        paciente_id = int(input("ID do paciente: "))
        while not json_manager.search_json(paciente_id,"id","data/pacientes.json"):
            paciente_id = int(input("Id não encontrado, digíte o ID do paciente: "))

        print("-=-=-=Médicos=-=-=-=-")
        medico_lista = json_manager.carregar_json("data/medicos.json")

        for m in medico_lista:
            print(f"{m["id"]} - {m["nome"]}")

        medico_id = int(input("ID do médico: "))
        while not json_manager.search_json(medico_id, "id", "data/medicos.json"):
            medico_id = int(input("Id não encontrado, digíte o ID do médico: "))

        data = input("Digíte a data: ")
        hora = input("Digít a hora: ")
        status = input("Digíte o status: ")

        registrar = {
            "id": id_generator.id_generator("data/consultas.json"),
            "id_paciente": paciente_id,
            "id_medico": medico_id,
            "data": data,
            "hora": hora,
            "status": status
        }

        json_manager.adicionar_json("data/consultas.json", registrar)

        print("Consulta marcada com sucesso!\n\n")
        print("0. Sair")
        print("1. Continuar")
        op = input("Deseja registar outra consulta: ")