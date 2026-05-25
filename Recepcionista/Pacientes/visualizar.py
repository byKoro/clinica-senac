from administrador.database import json_manager as json_manager

def visualizar_paciente():
    cpf = input("Digite o cpf do paciente: ")
    pacientes = json_manager.carregar_json("data/pacientes.json")
    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            print(f"Paciente encontrado: {paciente['nome']}")
            print(f"ID: {paciente['id']}, Nome: {paciente['nome']}, Idade: {paciente['idade']}, Endereço: {paciente['endereco']} {paciente['telefone']}, CPF: {paciente['cpf']}")
            return paciente
    print("Paciente não encontrado.")
    return None