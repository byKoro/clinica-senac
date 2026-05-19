from administrador.database import json_manager as json_manager
from administrador.services import id_generator as id_generator

def list_medic():
  lista = json_manager.carregar_json("data/medicos.json")
  for m in lista:
    print(f"{m["id"]} - {m["nome"]}")

def cad_medic():
  nome = input("Nome do médico: ")
  especialidade = input("Especialidade do médico: ")
  crm = input("CRM: ")

  registrar = {
    "id": id_generator.id_generator("data/medicos.json"),
    "nome": nome,
    "especialidade": especialidade,
    "crm": crm
  }

  json_manager.adicionar_json("data/medicos.json", registrar)

def del_medic():
  list_medic()

  del_id_medic = int(input("Deletar médico pelo ID: "))
  while not json_manager.search_json(del_id_medic,"id", "data/medicos.json"):
    del_id_medic = int(input("ID inválido! Deletar médico pelo ID: "))

  lista_medicos = json_manager.carregar_json("data/medicos.json")

  for i, m in enumerate(lista_medicos):
    if del_id_medic == m["id"]:
      del_index = i - 1
      break
  
  lista_medicos.pop(del_index)
  json_manager.salvar_json("data/medicos.json", lista_medicos)
  print("Deletado com sucesso!")