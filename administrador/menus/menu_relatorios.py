from administrador.database import auth_relatorios as relatorios

def menu_relatorios():
    while True:
        print("""================================
        MENU RELATÓRIOS
================================""")
        print("1 - Total de consultas realizadas por período")
        print("2 - Total de consultas canceladas")
        print("3 - Quantidade de pacientes cadastrados")
        print("4 - Quantidade de médicos ativos")
        print("5 - Consultas por médico")
        print("6 - Atendimentos realizados no dia")
        print("7 - Pacientes mais atendidos")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            relatorios.rel_consultas_por_periodo()

        elif op == "2":
            relatorios.rel_consultas_canceladas()

        elif op == "3":
            relatorios.rel_total_pacientes()

        elif op == "4":
            relatorios.rel_medicos_ativos()

        elif op == "5":
            relatorios.rel_consultas_por_medico()

        elif op == "6":
            relatorios.rel_atendimentos_dia()

        elif op == "7":
            relatorios.rel_pacientes_mais_atendidos()

        elif op == "0":
            break

        else:
            print("Opção inválida!")