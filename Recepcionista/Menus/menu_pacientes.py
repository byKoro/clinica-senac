from Recepcionista.Pacientes import cadastrar
from Recepcionista.Pacientes import editar_paciente

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
        editar_paciente.editar_paciente()