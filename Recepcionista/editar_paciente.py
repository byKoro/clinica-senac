from administrador.database.json_manager import salvar_json, carregar_json, list_json

def editar_paciente():

    pacientes = carregar_json("data/pacientes.json")

    print("\nLista de pacientes")
    list_json("data/pacientes.json")

    nome_busca = input("\nDigite o nome do paciente: ")

    for paciente in pacientes:

        if paciente["nome"] == nome_busca:

            print("\nEditar paciente")
            print("1 - Editar nome")
            print("2 - Editar idade")
            print("3 - Editar endereço")
            print("4 - Editar número da casa")
            print("5 - Editar CPF")

            op = input("Digite uma opção: ")

            if op == '1':
                paciente["nome"] = input("Digite o novo nome: ")

            elif op == '2':
                paciente["idade"] = input("Digite a nova idade: ")

            elif op == '3':
                paciente["endereco"] = input("Digite o novo endereço: ")

            elif op == '4':
                paciente["numero_casa"] = input("Digite o novo número da casa: ")

            elif op == '5':
                paciente["cpf"] = input("Digite o novo CPF: ")

            salvar_json("data/pacientes.json", pacientes)

            print("Paciente atualizado com sucesso!")