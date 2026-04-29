import utilidades.utils as utils

def cadastrar_usuario(usuario, senha, nivel):
  if not usuario or not senha:
    return False
  
  if nivel not in ["Administrador", "Recepcionista" , "Médico"]:
    return False
  if buscar_usuario(usuario):
    return False

  novo_usuario = {
    "id": utils.gerar_id("usuarios"),
    "usuario": usuario,
    "senha": senha,
    "nivel": nivel
  } 

  utils.adicionar("usuarios", novo_usuario)
  return True

def buscar_usuario(usuario):
  informacoes = utils.carregar("usuarios")
  for i in informacoes:
    if i["usuario"] == usuario:
      return i
  return None

def logar_usuario(usuario,senha):
  informacoes = utils.carregar("usuarios")
  for i in informacoes:
    if i["usuario"] == usuario and i["senha"] == senha:
      return i

  return None

def deletar_usuario():
    usuario = input("Deletar usuario: ")
    while st.buscar_usuario(usuario) is None:
        print("Erro")
        usuario = input("Deletar usuario: ")
    lista_usuarios = ut.carregar("usuarios")
    for u, i in enumerate(lista_usuarios):
        if usuario == i["usuario"]:
            lista_usuarios.pop(u)
    ut.salvar("usuarios", lista_usuarios)

