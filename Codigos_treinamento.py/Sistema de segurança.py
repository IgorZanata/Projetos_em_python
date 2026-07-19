class BancoDados:
    def __init__(self,):
        self.__historico = {
            "IGOR" : 369,
            "JOSE" : 123,
            "MATEUS" : 852,
            "FELIPE" : 741
        }  
  
 
    
    def chave_valor (self,nome,senha):
        if nome in self.__historico and self.__historico[nome] == senha:
            return True
        else:
            return False
        
        
        
        
class Seguranca:
    def __init__(self,conexao,inter):
        self.conexao = conexao
        self.inter = inter
        self.tentativa = 0
        
    def entrar(self):
        while True:
            nome = interacao.adicionar_nome()
            senha = interacao.adionar_senha()
        
            if self.conexao.chave_valor(nome,senha):
                    print("AUTORIZADO...")
                    break
            else:
                self.tentativa +=1
                print(f"{self.tentativa}º Tentativa") 
                if self.tentativa >= 3:
                    print("Usuario Bloqueado...")
                    break
               
            

   
   
class Interface:
    
    def adicionar_nome(self): 
        nome = input("Nome")   
        return nome
    
    def adionar_senha(self):  
        while True:
            try:
                senha = int(input("SENHA:"))
                return senha
            except ValueError:
                print("Somente Numeros")
            
        
banco = BancoDados()
interacao = Interface()
protecao = Seguranca(conexao = banco, inter = interacao)
protecao.entrar()
