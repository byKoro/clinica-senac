from administrador.services import id_generator as id_generator

def cadastrar_pacientes():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade do paciente: "))
    endereço = input("Digite seu número de endereço: ")
    numero = int(input("Digite o numero da casa: "))
    cpf = int(input("Digite seu cpf:"))
    #id = int(input({id.generate_id("Digite seu id")}))
    