class Conta:
    def __init__(self,titular, saldo, cpf):
        self.titular = titular
        self.__saldo = saldo
        self.cpf = cpf
       

    @property
    def saldo(self):
        return self.__saldo
    
    def saque(self,valor_saque):
        if 0 < valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            return True
        return False
            
    def deposito(self,valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            return True 
        return False
    
    
    def alterar(self,valor):
        self.titular = valor
        return 
    
        
class BancoDados:
    def __init__(self):
        self.historico = {}
        
    def exibir(self):
        if not self.historico:
            return False
        return True
    
   
class Interface:
    def __init__(self,conexao):
        self.conexao = conexao
        
    def menu(self):
        while True:
            try:    
                return int(input("""
0 - SAIR                   
1 - CADASTRAR
2 - EXIBIR
3 - SAQUE
4 - DEPOSITO
5 - ALTERAR NOME
6 - SALVAR
    --->>>"""))
            except ValueError:
                print("SOMENTE NUMEROS")
    
    def cadastrar_cpf(self):
        while True:
            try:
                valor_cpf = int(input("CPF:"))
                return valor_cpf
            except ValueError:
                print("Somente Numeros !")
                
    def buscar_somente_cadastro(self,valor):
        
        if valor in self.conexao.historico:
            return self.conexao.historico[valor]
        else:
            return None
          
    def buscar(self): 
        while True:
            valor_cpf_busca = self.cadastrar_cpf()
            if valor_cpf_busca in self.conexao.historico:
                return self.conexao.historico[valor_cpf_busca]
            else: 
                try:
                    opcao = int(input("1 - NÃO ENCONTRADO ! CONTINUAR A PROCURAR CPF ?\n2 - SAIR\n--->>>"))
                    if opcao == 1:
                        continue
                    elif opcao == 2:
                        return
                    else:
                        print("Somente numeros entre 1 e 2")
                except ValueError:
                    print("ERRO ! Somente Numeros entre 1 e 2")
                         
    def incluir_valor(self):
        while True:
            try:
                valor = float(input("Valor R$:"))                
                return valor
            except ValueError:
                print("Somente Numeros")
                
    def incluir_valor_saque(self):
        while True:
            try:
                valor = float(input("Valor de SAQUE R$:"))                
                return valor
            except ValueError:
                print("Somente Numeros")
    
    def incluir_valor_deposito(self):
        while True:
            try:
                valor = float(input("Valor de DEPOSITO R$:"))                
                return valor
            except ValueError:
                print("Somente Numeros")
                          
    def sacar(self):
        buscar_para_saque = self.buscar()
        if buscar_para_saque is None:
            print("USUARIO NÃO ENCONTRADO")
            return
        valor_saque = self.incluir_valor_saque()     
        if buscar_para_saque.saque(valor_saque):
            print(f"SAQUE DE R${valor_saque} REALIZADO ")
        else:
            print("Valor insuficiente")
                      
    def depositar(self):
        buscar_cpf_deposito = self.buscar()
        if buscar_cpf_deposito is None:
            print("Não encontrado")
            return
        valor_deposito = self.incluir_valor_deposito()
        if buscar_cpf_deposito.deposito(valor_deposito):
            print(f"Deposito R$ {valor_deposito} Realizado")
        else:
            print("Valor INVALIDO")
            
    def adicionar(self):
        titular = input("NOME:").strip().upper()
        saldo = self.incluir_valor()
        cpf = self.cadastrar_cpf()
        if not self.buscar_somente_cadastro(cpf):
            self.conexao.historico[cpf] = Conta(titular,saldo,cpf)
            print("CADASTRO REALIZADO COM SUCESSO !!")
        else:
           print("JÁ CADASTRADO")
                  
    def exibir_todos(self):
        if not self.conexao.historico:
            print("SEM USUARIOS CADASTRADOS") 
        else:
            print("=========USUARIOS CADASTRADOS ============")
            for chave, valor in self.conexao.historico.items():
                print(f"CPF:{chave}\nNOME:{valor.titular}\nSALDO R${valor.saldo}")
                print("=================================")
                
    def alterar_nome(self):
        cpf_buscar = self.buscar()
        if cpf_buscar is None:
            print("NÃO ENCONTRADO")
            return
        
        nome_atualizado = input("NOME ATUALIZADO:").strip().upper()   
        if cpf_buscar.alterar(nome_atualizado):
            print("Nome atualizado com sucesso")
    
    def salvar(self):
        with open("/home/igor/Projetos_em_python/Codigos_treinamento.py/Lista_Clientes.txt", "w", encoding = "utf=8") as arquivo:  
            for chave, valor in self.conexao.historico.items():
                linha = f"CPF: {chave}\nNome {valor.titular}\nSaldo R${valor.saldo}\n===============" 
                arquivo.write(linha)
        print("FINALIZADO")
              

bd = BancoDados()
interacao = Interface(bd)


while True:
    opcao = interacao.menu()
    if opcao == 0:
        print("Encerrando")
        break
    
    if opcao in [1,2,3,4,5,6]:
        if opcao == 1:
            interacao.adicionar()
        elif opcao == 2:
            interacao.exibir_todos()
        elif opcao == 3:
            interacao.sacar()
        elif opcao == 4:
            interacao.depositar()
        elif opcao == 5:
            interacao.alterar_nome()
        elif opcao == 6:
            interacao.salvar()
    else:
        print("Somente valores entre 0 até 6")
        
        
        