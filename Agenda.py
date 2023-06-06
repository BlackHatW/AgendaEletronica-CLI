import pickle
from os import path 

class Contato:  
    def __init__(self, nome,telefone, email, empresa):
        self.nome = nome 
        self.telefone = telefone
        self.email = email 
        self.empresa = empresa 


class Agenda:
    def __init__(self):
        self.lista = []
        self.atualizarDadosAgenda()

    def adicionarContato(self,nome,telefone,email,empresa): ## Adiciona Contato na agenda 
        ocorrencias = 0
        for i in self.lista:
            if i.telefone == telefone:
                ocorrencias += 1
                break 
        if ocorrencias == 0: 
            self.lista.append(Contato(nome,telefone,email,empresa))
        else:
            print("Este Numero de telefone ja existe na lista de contatos !")
         
    def excluirContato(self,contato): ## apagar primeira ocorrencia do contato da agenda 
        contador = 0 
        for i in self.lista:
           if i.nome == contato or i.telefone == contato:
               self.lista.remove(i)
               contador += 1
               break
           
        return True if contador>0 else False   
        

    def listarContatos(self): ## lista todos os contatos da agenda
         print("Listando Contatos...:")
         print("Agenda Não Possui Contatos") if not self.lista else None
         for i in self.lista:
             print("---------------------------------------------------------------------\n",
                      f'{i.nome} |   {i.telefone}  | {i.email} |{i.empresa}              \n',
                   "---------------------------------------------------------------------")
          

    def alterarContato(self,contato,nome,telefone,email,empresa):
       if self.excluirContato(contato) == True:
           self.adicionarContato(nome,telefone,email,empresa)
           return True 
       else:
           return False

    def listarContato(self,dado): ## pesquisa e lista os dados de um contato da agenda
       ocorrencias = 0
       for i in self.lista:
           if i.nome == dado or i.telefone == dado or i.email == dado or i.empresa == dado:
                print(f'{i.nome} , {i.telefone}, {i.email}, {i.empresa}')
                ocorrencias += 1
       if ocorrencias == 0 :
               print("Não foi encontrado nenhum contato de acordo com a informação especificada")     

    def salvarDadosAgenda(self):
        with open("dados.pck","wb") as f:
            pickle.dump(self.lista,f)
    
    def atualizarDadosAgenda(self):
        if path.exists("dados.pck"):
            with open("dados.pck","rb") as f:
                self.lista = pickle.load(f)



    