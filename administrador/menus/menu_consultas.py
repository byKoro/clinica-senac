from administrador.database import auth_consultas as list_consults

def menu_consultas():
    while True:
        print("""================================
        MENU CONSULTAS
================================""")
        print("1 - Listar consultas")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            list_consults.list_consults()
        elif op == "0":
            break
        else:
            print("Opção inválida!")