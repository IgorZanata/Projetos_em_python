class Conta:
    def __init__(self,cpf, titular, saldo):
        self.cpf = cpf
        self.titular = titular
        self.__saldo = saldo
    
    def saldo(self):
        return self.__saldo
    
    def alterar_saldo(self,valor):
        self.__saldo = valor
    
    
class BancoDados:
    def __init__(self):
        self.historico = {}
        
    def exibir_clientes(self):
        if not self.historico:
            print("SEM CLIENTES CADASTRADOS")
        else:
            print("====== CLIENTES CADASTRADOS ======")
            for chave, valor in self.historico.items():
                print(f"CPF: {chave} | Cliente:{valor.titular} | Saldo R$ {valor.saldo()}")
                print("===============================")
        
        
class Interface:
    def __init__(self,banco):
        self.banco = banco
        
    def buscar(self, cpf):
        
        if cpf  in self.banco.historico:
            return self.banco.historico[cpf]
        else:
            return None
    
    def adicionar_cliente(self):
        while True:    
            while True:
                try:
                    cpf = int(input("CPF:"))
                    if cpf >0:
                        break
                    else:
                        print("Valor Invalido\nTente Novamente")
                except ValueError:
                    print("Somente numeros\nTente Novamente")
            
            if not self.buscar(cpf):
                while True:
                    try:
                        titular = input("Nome:").strip().upper()
                        saldo = float(input("Saldo:"))   
                        if saldo > 0:
                            self.banco.historico[cpf] = Conta(cpf, titular, saldo)
                            print("Cadastrado com sucesso !!")
                            break     
                        else:
                            print("Valor invalido")
                            print("Digite novamente")         
                    except ValueError:
                        print("Somente numeros")
                        print("Digite novamente")             
                break
            else:
                print("Usuario ja cadastrado !!!\nTente novamente")
                    
    def menu(self):
        while True:
            try:
                return int(input("""
[0] SAIR
[1] ADICIONAR
[2] EXIBIR TODOS OS CLIENTES
[3] PROCURAR CLIENTE
[4] DEPOSITO
[5] SAQUE
--->>>"""))
            except ValueError:
                print("Somente numeros\nDigite Novamente")
                
                
    def deposito(self):
        while True:
            while True:
                try:
                    buscar_cpf = int(input("Digite o CPF para realizar o deposito:"))
                    buscador = self.buscar(buscar_cpf)
                    break
                except ValueError:
                    print("Somente Numeros\nDigite novamente")
            
            if buscador:
                while True:
                    try:    
                        valor = float(input("Valor para deposito:"))
                        if  valor >= 0:
                            buscador.alterar_saldo(buscador.saldo() + valor)
                            
                            print(f"Deposito realizado com sucesso")
                            break
                        else:
                            print ("Valor invalido")
                    except ValueError:
                        print("Somente Numeros\nDigite Novamente")
            else:
                print("Usuario não encontrado")
                
                while True:
                    try:
                        opcao = int(input("Dejesa 1 - SAIR | 2 - CONTINUAR A PROCURAR?\n--->>>:"))
                        if opcao == 1:
                            print("Encerrando")
                            return
                        elif opcao == 2:
                            break
                        else:
                            print("Opção invalida ! Somente 1 ou 2")
                    except ValueError:
                        print("Somente Numeros entre 1 e 2")                  
                
    def saque(self):
        while True:
            while True:
                try:
                    cpf_buscar = int(input("Digite o CPF para realizar o saque\n--->>>"))
                    cpf_saque = self.buscar(cpf_buscar)
                    break
                except ValueError:
                    print("Somente Numeros\nDigite Novamente")
            
            if cpf_saque:  
                while True:
                    try:
                        valor_saque = float(input("Valor do Saque:"))
                        
                        if 0 < valor_saque <= cpf_saque.saldo():
                            cpf_saque.alterar_saldo(cpf_saque.saldo() - valor_saque)
                            print(f"Saque de R$ {valor_saque}, realizado com sucesso ")
                            return                       
                        else:
                            print("Valor de saque invalido")                            
                    except ValueError:
                        print("Somente Numeros\nDigite Novamente")                       
            else:
                print("Usuario não encontrado") 
                
                while True:
                    try:
                        opcao = int(input("1 - CONTINUAR | 2 - SAIR\n--->>>"))         
                        if opcao == 1:
                            break                               
                        elif opcao == 2:
                            return                               
                        else:
                            print("Somente valores 1 e 2")                                                                     
                    except ValueError:
                        print("Somente numeros")


bd = BancoDados()
interacao = Interface(bd)


while True:  
    opcao = interacao.menu()
    if opcao in [0,1,2,3,4,5]: 
          
        if opcao == 0:
            print("Encerrando\nOBRIGADO !!")
            break   
        if opcao == 1:
            interacao.adicionar_cliente()
        elif opcao == 2:
            bd.exibir_clientes()
        elif opcao == 4:
            interacao.deposito()
        elif opcao == 5:
            interacao.saque()    
    else:
        print("Somente valores entre 0 até 5")
        
       
