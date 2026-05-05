import json
import os

pasta = "arquivos"

def salvar(arquivo, lista):
  os.makedirs(pasta, exist_ok=True)

  caminho = os.path.join(pasta, f"{arquivo}.json")

  with open(caminho,"w") as f:
    json.dump(lista, f, indent=4)
    return True

def carregar(arquivo):
  os.makedirs(pasta, exist_ok=True)

  caminho = os.path.join(pasta, f"{arquivo}.json")


  if not os.path.exists(caminho):
    with open(caminho,"w") as f:
      json.dump([], f)
      return []
  else:
    with open(caminho,"r") as f:
        try:
            return json.load(f)
        except:
            salvar(arquivo,[])
            return []

def adicionar(arquivo,dicionario):
  informacoes = carregar(arquivo)
  informacoes.append(dicionario)
  salvar(arquivo, informacoes)
  return True

def gerar_id(arquivo):
  informacoes = carregar(arquivo)
  if not informacoes:
    return 1
  maior_id = 0
  for i in informacoes:
    if i["id"] > maior_id:
      maior_id = i["id"]
  return maior_id + 1

def listar_arquivo(arquivo="usuarios"):
  usuarios = carregar(arquivo)
  for i in usuarios:
    print(f"Id: {i["id"]} - Nome: {i["usuario"]}")

def validar_senha_len(senha,config):
  min_limit = config["min"]
  max_limit = config["max"]
  message_min = config["message_min"]
  message_max = config["message_max"]
  message_pass_error = config["message_pass_error"]
  senha_len = len(senha)


  if senha_len < min_limit:
    print(message_min)
    return False
  elif senha_len > max_limit:
    print(message_max)
    return False
  else:
    return True

  return False

def validar_senha(user,senha,config):
  message_pass_error = config["message_pass_error"]
  usuarios = carregar("usuarios")

  for u in usuarios:
    if u["usuario"] == user and u["senha"] != senha:
      print(message_pass_error)
      return False

    elif u["usuario"] == user and senha == u["senha"]:
      return True
  
