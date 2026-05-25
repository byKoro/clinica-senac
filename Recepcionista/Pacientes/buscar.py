from administrador.database import json_manager as json_manager

def buscar_paciente():
    cpf = input("Digite o cpf do paciente: ")
    pacientes = json_manager.carregar_json("data/pacientes.json")
    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            print(f"Paciente encontrado: {paciente['nome']}")
            return paciente
    print("Paciente não encontrado.")
    return None