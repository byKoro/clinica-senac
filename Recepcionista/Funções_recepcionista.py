def cadastrar_pacientes(pacientes):
    nome = input("Digite o nome: ")
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida, usando 0.")
        idade = 0
    cpf = input("Digite seu CPF: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")
    numero = input("Digite o número da sua casa: ")
    endereco_completo = f"{endereco}, {numero}"


    next_id = max((p.get("id", 0) for p in pacientes), default=0) + 1 

    novo_paciente = {
        "id": next_id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco_completo
    }
    pacientes.append(novo_paciente)
    return pacientes

pacientes = []

print(cadastrar_pacientes(pacientes))