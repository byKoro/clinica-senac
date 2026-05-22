from administrador.database import json_manager

def list_consults():
    consultas = json_manager.carregar_json("data/consultas.json")
    medicos = json_manager.carregar_json("data/medicos.json")
    pacientes = json_manager.carregar_json("data/pacientes.json")

    for c in consultas:
        paciente_nome = "Desconhecido"
        medico_nome = "Desconhecido"

        # busca paciente
        for p in pacientes:
            if p["id"] == c["id_paciente"]:
                paciente_nome = p["nome"]
                break

        # busca médico
        for m in medicos:
            if m["id"] == c["id_medico"]:
                medico_nome = m["nome"]
                break

        print(
            f"\nID Consulta: {c['id']}\n"
            f"Paciente: {paciente_nome} (ID {c['id_paciente']})\n"
            f"Médico: {medico_nome} (ID {c['id_medico']})\n"
            f"Data: {c['data']} - Hora: {c['hora']}\n"
            f"Status: {c['status']}\n"
            f"-----------------------------"
        )

from administrador.database import json_manager

def rel_consultas_do_dia():
    consultas = json_manager.carregar_json("data/consultas.json")

    hoje = input("Digite a data de hoje (dd mm aaaa): ")

    encontrou = False

    for c in consultas:
        if c["data"] == hoje:
            print(
                f"\nID: {c['id']} - Paciente {c['id_paciente']} - Médico {c['id_medico']}"
                f"\nHora: {c['hora']} - Status: {c['status']}"
                f"\n-----------------------------"
            )
            encontrou = True

    if not encontrou:
        print("\nNenhuma consulta encontrada para hoje.")

from administrador.database import json_manager

def rel_consultas_futuras():
    consultas = json_manager.carregar_json("data/consultas.json")

    data_atual = input("Digite a data atual (dd mm aaaa): ")

    encontrou = False

    for c in consultas:
        if c["data"] > data_atual:
            print(
                f"\nID: {c['id']} - Paciente {c['id_paciente']} - Médico {c['id_medico']}"
                f"\nData: {c['data']} - Hora: {c['hora']} - Status: {c['status']}"
                f"\n-----------------------------"
            )
            encontrou = True

    if not encontrou:
        print("\nNenhuma consulta futura encontrada.")