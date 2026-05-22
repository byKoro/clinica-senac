from administrador.database import json_manager

def rel_consultas_por_periodo():
    consultas = json_manager.carregar_json("data/consultas.json")

    inicio = input("Data inicial (dd mm aaaa): ")
    fim = input("Data final (dd mm aaaa): ")

    total = 0

    for c in consultas:
        data = c["data"]
        status = c["status"]

        if status.lower() == "realizado":
            if inicio <= data <= fim:
                total += 1

    print(f"\nTotal de consultas realizadas no período: {total}")

def rel_consultas_canceladas():
    consultas = json_manager.carregar_json("data/consultas.json")

    total_canceladas = 0

    for c in consultas:
        if c["status"].lower() == "cancelado":
            total_canceladas += 1

    print(f"\nTotal de consultas canceladas: {total_canceladas}")

def rel_total_pacientes():
    pacientes = json_manager.carregar_json("data/pacientes.json")
    print(f"\nTotal de pacientes cadastrados: {len(pacientes)}")

def rel_medicos_ativos():
    medicos = json_manager.carregar_json("data/medicos.json")
    print(f"\nTotal de médicos cadastrados: {len(medicos)}")

def rel_consultas_por_medico():
    consultas = json_manager.carregar_json("data/consultas.json")
    medicos = json_manager.carregar_json("data/medicos.json")

    for m in medicos:
        total = 0

        for c in consultas:
            if c["id_medico"] == m["id"]:
                total += 1

        print(f"Médico: {m['nome']} - Consultas: {total}")

def rel_atendimentos_dia():
    consultas = json_manager.carregar_json("data/consultas.json")

    data_busca = input("Digite a data (dd mm aaaa): ")

    total = 0

    for c in consultas:
        if c["status"].lower() == "realizado" and c["data"] == data_busca:
            total += 1

    print(f"\nAtendimentos realizados no dia: {total}")

def rel_pacientes_mais_atendidos():
    consultas = json_manager.carregar_json("data/consultas.json")
    pacientes = json_manager.carregar_json("data/pacientes.json")

    contador = {}

    for c in consultas:
        if c["status"].lower() == "realizado":
            id_paciente = c["id_paciente"]

            if id_paciente in contador:
                contador[id_paciente] += 1
            else:
                contador[id_paciente] = 1

    if not contador:
        print("Nenhum atendimento realizado.")
        return

    maior_id = max(contador, key=contador.get)
    qtd = contador[maior_id]

    nome = "Desconhecido"

    for p in pacientes:
        if p["id"] == maior_id:
            nome = p["nome"]
            break

    print(f"\nPaciente mais atendido: {nome} - {qtd} atendimentos")