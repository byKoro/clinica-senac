import utilidades.system as st
import utilidades.cores as cr
import utilidades.utils as ut

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
        menu_admin_usuarios()

    elif opcao == "0":
        print(cr.vermelho("Programa finalizado!"))

def menu_admin_usuarios():
    print("1. Cadastrar novo usuário: ")
    print("2. Editar usuarios: ")
    print("6. Sair")
    
    opcao = input("Digíte sua opção: ")
    
    while opcao not in ['1','2','3','4','5','6']:
        print(cr.vermelho("Opção invalida!"))
        opcao = input("Digite opcao: ")

    if opcao == "1":
        cadastrar_usuarios()
    elif opcao == "2":
        editar_usuarios()


def cadastrar_usuarios():
    nome = input("Cadastrar novo usuário: ")
    while st.buscar_usuario(nome) is not None:
        print(cr.vermelho("Usuário já cadastrado!"))
        nome = input("Cadastrar novo usuário: ")

    senha = input("Cadastrar Senha: ")
    while len(senha) > 14 or len(senha) < 4:
        print(cr.vermelho("A senha deve ter entre 4 e 14 caracteres."))
        senha = input("Cadastrar senha: ")
    
    print("Niveis de acesso")
    print("1.Administrador")
    print("2.Recepcionista")
    print("3.Médico")
    nivel = input("Selecione uma categoria para o novo usuário: ")
    while nivel not in ["1","2","3"]:
        print(cr.vermelho("Opção inválida!"))
        nivel = input("Selecione uma categoria para o novo usuário: ")
    
    if nivel == "1": nivel = "Administrador"
    elif nivel == "2": nivel = "Recepcionista"
    elif nivel == "3": nivel = "Médico"

    novo_usuario = {
        "id": ut.gerar_id("usuarios"),
        "usuario": nome,
        "senha": senha,
        "nivel": nivel
    }

    ut.adicionar("usuarios", novo_usuario)
    print(cr.verde("Usuário cadastrado com Sucesso!"))

def editar_usuarios():
    usuarios = ut.carregar("usuarios")
    ut.listar_arquivo()
    editar_usuario = input("Editar usuário: ")

    Busca = False
    while not Busca:
        for i in usuarios: 
            if i["usuario"] == editar_usuario:
                editar_usuario = i
                Busca = True
        if not Busca:
            print(cr.vermelho("Esse usuário não foi encontrado!"))
            editar_usuario = input("Editar usuário: ")
        
    Salvar = False
    while not Salvar:
        print("1.Nome")
        print("3.Senha")
        print("2.Nível")
        print("0.Sair")
        opcao = input("Escolha o que deseja alterar: ")

        while opcao not in ["1","2","3","0"]:
            print(cr.vermelho("Opção inválida!"))
            opcao = input("Escolha o que deseja alterar: ")

        if opcao == "1":
            nome = input("Novo nome de usuário: ")
        elif opcao == "2":
            senha = input("Nova senha: ")
            while len(senha)
        


while True:
    menu_admin()
    