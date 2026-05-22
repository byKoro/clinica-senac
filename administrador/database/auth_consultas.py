from administrador.database import json_manager as json_manager

def list_consults():
    consultas = json_manager.carregar_json("data/consultas.json")

    for c in consultas:
        paciente_id = c["id_paciente"]
        medico_id = c["id_medico"]
        data = c["data"]
        hora = c["hora"]
        status = c["status"]

        medico = json_manager.search_json(medico_id, "id", "data/medicos.json")
        paciente = json_manager.search_json(paciente_id, "id", "data/pacientes.json")

        nome_medico = medico["nome"] if medico else "Médico não encontrado"
        nome_paciente = paciente["nome"] if paciente else "Paciente não encontrado"

        print(
            f"Consulta ID: {c['id']}\n"
            f"Paciente: {nome_paciente} (ID {paciente_id})\n"
            f"Médico: {nome_medico} (ID {medico_id})\n"
            f"Data: {data} - Hora: {hora}\n"
            f"Status: {status}\n"
            f"-----------------------------"
        )