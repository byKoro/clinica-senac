from administrador.database import json_manager
def get_quantidade(chave, valor, caminho):
    item = json_manager.carregar_json(caminho)
    count = 0
    for i in item:
        if i[chave] == valor:
            count = count + 1
    return count



def menu_recepcionista():
    consultas = get_quantidade("status", "Agendado", "data/consultas.json")
    pacientes = len(json_manager.carregar_json("data/pacientes.json"))
    medicos = len(json_manager.carregar_json("data/medicos.json"))
    consultas_finalizadas = get_quantidade("status", "Confirmado", "data/consultas.json")

    while True:
        print("""================================
        MENU RECEPCIONISTA
================================""")
        print(f"Consultas hoje: {consultas}")
        print(f"Pacientes cadastrados: {pacientes}")
        print(f"Medicos ativos: {medicos}")
        print(f"Consultas finalizadas hoje: {consultas_finalizadas}")
        
        print("-=-==-=-=-=-=-=-=-=-=-")
        print("1 - Pacientes")
        print("2 - Consultas")
        print("3 - Relatório")
        print("0 - Sair")
        op = input("Escolha uma opção: ")
        while op not in ["1","2","3","0"]:
            op = input("Invalído! Escolha uma opção: ")


        if op == "1":
            continue
        