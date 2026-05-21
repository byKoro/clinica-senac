def menu_login():
    print(
"""================================
     SISTEMA CLÍNICA MÉDICA
================================""")
    print("1 - Login")
    print("0 - Sair")
    op = input("Escolha: ")
    while op not in ["1","2"]:
        op = input("Opção invalída! Escolha:")
    return op
