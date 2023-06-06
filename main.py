## Agenda Eletronica 1.0 
## Created by Welington Nogueira Silva 
## Data: 02/06/2023
from Agenda import *
from os import system
from time import sleep

flag = '0'
agenda = Agenda()

while (flag != '7'):
    if(flag == '0'):
        system("clear")
        print("Agenda Eletronica 1.0 \n",
              "(1)- Adicionar Contato \n",
              "(2)- Excluir Contato \n",
              "(3)- Listar todos os Contatos \n",
              "(4)- Alterar Contato \n",
              "(5)- Listar dados de um determinado contato \n",
              "(6)- Sair \n")
        flag =  input("Escolha uma das opções acima para prosseguir:").strip()
    elif(flag == '1'):
         system("clear")
         print(" Informe os dados do contato para cadastro (Numero de telefone/celular  é obrigatório:")
         nome = input("nome: ").strip()
         telefone = input("telefone/celular: ").strip()
         email = input("email: ").strip()
         empresa = input("empresa: ").strip()
         agenda.adicionarContato(nome,telefone,email,empresa)
         flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou Adicionar um novo Contato (1): ").strip()
    elif(flag == '2'):
         system("clear")
         print(" Informe o Nome ou Telefone/celular do contato que deseja Remover da Agenda:\n",
               "(Caso tenha 2 Contatos ou mais com o mesmo nome o sistema ira remover somente  primeira ocorrencia encontrada",
               " para ter precisão informe o Telefone/celular)")
         coringa = input("Nome ou Telefone/Celular: ").strip()
         status = agenda.excluirContato(coringa)
         if status == True:
             print(f'Contato: {coringa} Removido com Sucesso ')
             flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou Remover outro Contato (2): ").strip()
         else:
             print(f'Não foi possivel remover o contato especificado: ({coringa}) \n',
                   'Veirifique se as informações digitadas estão corretas. \n')
             flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou Tentar Novamente (2): ").strip()
    elif(flag == '3'):
        system("clear")
        agenda.listarContatos()
        flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou listar contatos novamente (3): ").strip()

    elif(flag == '4'):
         system("clear")
         print(" Informe o Nome ou Telefone/celular do contato que deseja Editar/Alterar da Agenda:\n",
               "(Caso tenha 2 Contatos ou mais com o mesmo nome o sistema ira alterar somente  primeira ocorrencia encontrada",
               " para ter precisão informe o Telefone/celular)")
         coringa = input("Nome ou Telefone/Celular: ")
         print(" Informe os dados que deseja Alterar: (Numero de telefone/celular  é obrigatório:")
         nome = input("nome: ").strip()
         telefone = input("telefone/celular: ").strip()
         email = input("email: ").strip()
         empresa = input("empresa: ").strip()
         status = agenda.alterarContato(coringa,nome,telefone,email,empresa)
         if status == True:
             print(f'Contato: {coringa} alterado com Sucesso ')
             flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou (4) Editar/Alterar outro Contato: ").strip()
             
         else:
             print(f'Não foi possivel Editar/Alterar o contato especificado: ({coringa}) \n',
                   'Veirifique se as informações digitadas estão corretas. \n')
             flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou Tentar Novamente (4): ").strip()

    elif(flag == '5'):
        system("clear")
        print(" Informe o Nome ou Telefone/celular do contato que deseja Verificar:\n",
               "(Caso tenha 2 Contatos com o mesmo nome seja mais especifico e informe o Telefone/celular)")
        coringa = input("Nome ou Telefone/Celular: ").strip()
        agenda.listarContato(coringa)
        flag = input("Se Deseja Voltar ao menu inicial Digite(0) ou (5) Pesquisar Novamente: ").strip()
    elif(flag == '6'):
        agenda.salvarDadosAgenda()
        system("clear")
        print("\n Encerrando Aplicativo.....")
        print("   Até Mais.. <3")
        flag = '7'
        sleep(2)

    else:
        print("Opção Invalida, Tente Novamente ! \n")
        sleep(2)
        system("clear")
        flag = '0'
        

    
