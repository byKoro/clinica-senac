import utilidades.cores as cr
import utilidades.utils as ut
import utilidades.system as st
import utilidades.menus as mn
import administrador.index as adm
import administrador.config.senha_config as senha_config
while True:
  usuario = input("Digíte o nome do usuário: ")
  senha = input("Digíte a senha: ")

  Usuario = st.logar_usuario(usuario,senha)

  if Usuario is None:
    error = senha_config.config_senha["message_pass_error"]
    print(error)
    
  else:
    break


if Usuario["nivel"] == "Administrador":
  adm.menu_admin()


elif Usuario["nivel"] == "Recepcionista":
  print("Tela da Recepcionista.")
  print("Tela do Felipe")

elif Usuario["nivel"] == "Médico":
  print("Tela do Médico")

