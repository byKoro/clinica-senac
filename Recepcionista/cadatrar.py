from administrador.services import id_generator as id_generator
from administrador.database import json_manager as json_manager
def cadastrar_pacientes():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade do paciente: "))
    endereço = input("Digite seu número de endereço: ")
    numero = int(input("Digite o numero da casa: "))
    cpf = int(input("Digite seu cpf:"))
    id_paciente = id_generator.id_generator("data/pacientes.json")
    
    paciente = {
        "id": id_paciente,
        "nome": nome,
        "idade": idade,
        "endereço": endereço,
        "numero": numero,
        "cpf": cpf
    }
    
    json_manager.adicionar_json("data/pacientes.json", paciente)