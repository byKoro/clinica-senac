from Recepcionista.Consultas import registrar_consultas as agendar_consultas
from Recepcionista.Consultas import editar_consultas
from Recepcionista.Consultas import listar_consultas

def menu_consultas():
    while True:
        print("""================================
        MENU CONSULTAS================================ """)
        print("1 - Agendar consulta")
        print("2 - Editar consulta")
        print("3 - Listar consultas")
        print("0 - Sair")
        op = input("Escolha uma opção: ")
        while op not in ["1","2","3","0"]:
            op = input("Invalído! Escolha uma opção: ")
        if op == "1":
            agendar_consultas.agendar_consulta()
        elif op == "2": 
            editar_consultas.editar_consulta()
        elif op == "3":
            listar_consultas.listar_consultas()