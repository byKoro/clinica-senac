import administrador.services.id_generator as id_generator
import administrador.database.json_manager as json_manager
import administrador.database.auth_service as auth_service
# Id Generator
id_gen = id_generator.id_generator("administrador/data/usuarios.json")
print(id_gen)

#json_manager
#lista = [{"id":1},{"id":2},{"id":3}]
#json_manager.salvar_json("administrador/data/usuarios.json",lista)
#lista = json_manager.carregar_json("administrador/data/usuarios.json")
#novos_dados = {"id": id_generator.id_generator("administrador/data/usuarios.json")}
#nova_lista = json_manager.adicionar_json("administrador/data/usuarios.json", novos_dados)
#print(nova_lista)

a = auth_service.auth_user("yuri","1234")
print(a)