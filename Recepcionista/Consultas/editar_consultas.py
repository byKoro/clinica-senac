from administrador.database import json_manager as json_manager

from administrador.database import json_manager

def edit_consulta():
    consultas = json_manager.carregar_json("data/consultas.json")

    # lista consultas
    for c in consultas:
        print(f"{c['id']} - Paciente {c['id_paciente']} - Médico {c['id_medico']} - {c['data']} {c['hora']} - {c['status']}")

    op = int(input("\nEscolha o ID da consulta para editar: "))

    consulta_index = None

    for i, c in enumerate(consultas):
        if c["id"] == op:
            consulta_index = i
            break

    if consulta_index is None:
        print("ID inválido!")
        return

    while True:
        print("\n===== EDITAR CONSULTA =====")
        print("1 - Paciente")
        print("2 - Médico")
        print("3 - Data")
        print("4 - Hora")
        print("5 - Status")
        print("0 - Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            consultas[consulta_index]["id_paciente"] = int(input("Novo ID do paciente: "))

        elif escolha == "2":
            consultas[consulta_index]["id_medico"] = int(input("Novo ID do médico: "))

        elif escolha == "3":
            consultas[consulta_index]["data"] = input("Nova data (dd mm aaaa): ")

        elif escolha == "4":
            consultas[consulta_index]["hora"] = input("Nova hora (hh:mm): ")

        elif escolha == "5":
            print("\nStatus disponíveis:")
            print("1 - Agendado")
            print("2 - Cancelado")
            print("3 - Realizado")

            status_op = input("Escolha o status: ")

            if status_op == "1":
                consultas[consulta_index]["status"] = "Agendado"
            elif status_op == "2":
                consultas[consulta_index]["status"] = "Cancelado"
            elif status_op == "3":
                consultas[consulta_index]["status"] = "Realizado"
            else:
                print("Status inválido!")

        elif escolha == "0":
            break

        else:
            print("Opção inválida!")

    json_manager.salvar_json("data/consultas.json", consultas)
    print("\nConsulta atualizada com sucesso!")