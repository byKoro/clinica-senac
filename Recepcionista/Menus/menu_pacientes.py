from Recepcionista.Pacientes import cadastrar
# from Recepcionista.Pacientes import editar_paciente
from Recepcionista.Pacientes import buscar
from Recepcionista.Pacientes import listar 
from Recepcionista.Pacientes import visualizar

def menu_pacientes():
    while True:
        print("""================================
        MENU RECEPCIONISTA
================================""")
        print("1 - Cadastrar paciente")
        print("2 - Editar paciente")
        print("3 - Buscar paciente")
        print("4 - Listar pacientes")
        print("5 - Visualizar dados completos do paciente")
        print("0 - Sair")

        op = input("Escolha uma opção: ")
        while op not in ["1","2","3","4","5","0"]:
            op = input("Invalído! Escolha uma opção: ")

        if op == "1":
            cadastrar.cadastrar_pacientes()
        elif op == "2":
            #editar_paciente.editar_paciente()
            continue
        elif op == "3":
            buscar.buscar_paciente()
        elif op == "4":
            listar.listar_pacientes()
        elif op == "5":
            visualizar.visualizar_paciente()
        elif op == "0":
            break
        else: 
            print("Opção inválida, tente novamente.")

        