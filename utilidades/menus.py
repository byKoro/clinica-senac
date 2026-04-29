import utilidades.cores as Cores

def menu_admin_usuario():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Cadastrar usuario: "))
      print(Cores.verde("2. Editar usuarios: "))
      print(Cores.verde("3. Listar usuario: "))
      print(Cores.verde("4. Resetar senha do usuario: "))
      print(Cores.verde("5. Excluir usuario: "))
      print(Cores.verde("6. Sair"))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
     
      while opcao not in ['1','2','3','4','5','6']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

def menu_admin_medico():
      
      print(Cores.amarelo("\n ---Menu --- "))
      print(Cores.verde("1. Cadastrar medico: "))
      print(Cores.verde("2. Editar medico: "))
      print(Cores.verde("3. Lista listar medico: "))
      print(Cores.verde("4. Excluir medico: "))
      print(Cores.verde("5. Sair"))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4','5',]:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao
     

def menu_admin_paciente():

      print(Cores.amarelo("\n---Menu ---"))
      print(Cores.verde("1. Visualizar pacientes: "))
      print(Cores.verde("2. Buscar pacientes: "))
      print(Cores.verde("3. Ver historico: "))
      print(Cores.verde("4. Sair"))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

     
def menu_recep_paciente():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Cadastrar paciente: "))
      print(Cores.verde("2. Editar paciente: "))
      print(Cores.verde("3. Listar paciente: "))
      print(Cores.verde("4. Buscar paciente: "))
      print(Cores.verde("5. Visualizar dados: "))
      print(Cores.verde("6. Sair"))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4','5','6']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

def menu_recep_consultas():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Marcar colsulta para o medico: "))
      print(Cores.verde("2. Escolher data e hora: "))
      print(Cores.verde("3. Reagenadar paciente: "))
      print(Cores.verde("4. Confirmar presenca do paciente: "))
      print(Cores.verde("5. Listar consultas do dia: "))
      print(Cores.verde("6. Listar consultas futuras: "))
      print(Cores.verde("7. Cancelar consulta: "))
      print(Cores.verde("8. Sair"))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4','5','6','7',"8"]:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

def menu_recep_historico():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Visualizar consultas anteriores: "))
      print(Cores.verde("2. Ver datas de atendimento anteriores: "))
      print(Cores.verde("3. Sair: "))      
     
      opcao = input(Cores.azul("Digíte sua opção: "))
     
      while opcao not in ['1','2','3']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

def menu_recep_relatorios():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Agenda do dia: "))
      print(Cores.verde("2. Consulta po data: "))
      print(Cores.verde("3. Pacientes atendidos do dia: "))
      print(Cores.verde("4. Consultas canceladas do periodo: "))
      print(Cores.verde("5. Sair: "))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4','5']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao


def menu_med_agenda():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Visualizar agenda do dia "))
      print(Cores.verde("2. Listar consultas marcadas: "))
      print(Cores.verde("3. Visualizar agenda futura: "))
      print(Cores.verde("4. Sair: "))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao

def menu_med_historico():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Buscar paciente por nome: "))
      print(Cores.verde("2. Ver historico de consultas anteriores: "))
      print(Cores.verde("3. Ver prontuarios anteriores do paciente: "))
      print(Cores.verde("4. Sair: "))      
     
      opcao = input(Cores.azul("Digíte sua opção: "))
     
      while opcao not in ['1','2','3',"4"]:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao


def menu_med_relatorios():
      print(Cores.amarelo(f"\n   ----Menu----  "))
      print(Cores.verde("1. Pacientes atendidos no me: "))
      print(Cores.verde("2. Quantidade de consultas pedentes: "))
      print(Cores.verde("3. Total de atendimentos realizados: "))
      print(Cores.verde("4. Sair: "))
      
      opcao = input(Cores.azul("Digíte sua opção: "))
      
      while opcao not in ['1','2','3','4']:
            print(Cores.vermelho("Opção invalida!"))
            opcao = input(Cores.azul("Digite opcao: "))
      return opcao
