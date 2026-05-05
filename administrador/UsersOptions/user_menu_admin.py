import utilidades.cores as cr
import utilidades.system as st
import utilidades.utils as ut
import administrador.config.senha_config as config_senha

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
    while not ut.validar_senha_len(senha,config.config_senha):
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
        print("2.Senha")
        print("3.Nível")
        print("0.Sair")
        opcao = input("Escolha o que deseja alterar: ")

        while opcao not in ["1","2","3","0"]:
            print(cr.vermelho("Opção inválida!"))
            opcao = input("Escolha o que deseja alterar: ")

        if opcao == "1":
            nome = input("Novo nome de usuário: ")
            editar_usuario[i]["nome"] = nome

        elif opcao == "2":
            senha = input("Nova senha: ")
            while not ut.validar_senha_len(senha,config_senha):
                senha = input("Nova senha")
            editar_usuario[i]["senha"] = senha
        elif opcao == "3":
            print("Niveis de acesso")
            print("1.Administrador")
            print("2.Recepcionista")
            print("3.Médico")
            nivel = input("Escolha uma opção: ")
            while nivel not in ["1","2","3"]:
                nivel = input("Escolha uma opção: ")
            if nivel == "1": nivel = "Administrador"
            elif nivel == "2": nivel = "Recepcionista"
            elif nivel == "3": nivel = "Médico"
            editar_usuario[i]["nivel"] = nivel