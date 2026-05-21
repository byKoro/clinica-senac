from administrador.database import json_manager as json_manager
from administrador.database.medico import auth_medico as auth_medico
def menu_medico():
    while True:
        print(
        """================================
            MENU MÉDICO
        ================================""")
        print("1 - Cadastrar médico")
        print("2 - Editar médico")
        print("3 - Exluir médico")
        print("4 - Listar médicos")
        print("0 - Sair")

        op = input("Escolha uma opção: ")
        while op not in ["1","2","3","4","0"]:
            op = input("Opção invalída! Escolha uma opção: ")

        if op == "1":
            auth_medico.cadastrar_medico()
        elif op == "2":
            auth_medico.edit_medico()