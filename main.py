import utilidades.cores as cr
import utilidades.utils as ut
import utilidades.system as st
import utilidades.menus as mn

while True:
  usuario = input("Digíte o nome do usuário: ")
  senha = input("Digíte a senha: ")

  Usuario = st.logar_usuario(usuario,senha)

  if Usuario is None:
    print(cr.vermelho("Login ou senha inválido!"))
  else:
    break


if Usuario["nivel"] == "Administrador":
  print("Tela do Administrador")


elif Usuario["nivel"] == "Recepcionista":
  print("Tela da Recepcionista.")
  print("Tela do Felipe")

elif Usuario["nivel"] == "Médico":
  print("Tela do Médico")

