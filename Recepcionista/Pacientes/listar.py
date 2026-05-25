from administrador.database import json_manager as json_manager

def listar_pacientes():
    pacientes = json_manager.carregar_json("data/pacientes.json")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    print("Lista de Pacientes:")
    for paciente in pacientes:
        print(f"ID: {paciente['id']}, Nome: {paciente['nome']}, Idade: {paciente['idade']}, Endereço: {paciente['endereco']} {paciente['telefone']}, CPF: {paciente['cpf']}")