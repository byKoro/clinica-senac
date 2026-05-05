import utilidades.cores as cr
import administrador.UsersOptions.user_menu_admin as user_admin


def menu_admin():
    print("1.Usuários")
    print("2.Médicos")
    print("3.Pacientes")
    print("0.Sair")

    opcao = input("Selecione uma opção: ")
    while opcao not in ["1","2","3","0"]:
        print(cr.vermelho("Opção inválida!"))
        opcao = input("Selecione uma opção: ")
    
    if opcao == "1":
        user_admin.menu_admin_usuarios()

    elif opcao == "0":
        print(cr.vermelho("Programa finalizado!"))
        