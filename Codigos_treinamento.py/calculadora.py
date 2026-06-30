class Calculadora:
    
    def somar(self,a,b):
        return a + b
    
    def subtrair(self,a,b):
        return a - b
    
    def multiplicar(self,a,b):
        return a * b
    
    def dividir(self,a,b):
        
        try:
            return a / b
        
        except ZeroDivisionError:
            return None
        
class Banco_Dados:
    def __init__(self):
        self.historico = []
        
    def exibir(self):
        print(f"Valores: {self.historico}")
        
class Interacao:
    def __init__(self,banco,calc):
        self.banco = banco
        self.calc = calc
    
    def adicionar(self):
        while True:
            try:
                a = int(input("Valor:"))
                b = int(input("Valor:"))
                return a,b
             
            except ValueError:
                print("Somente numeros")
            
    def menu(self):
        while True:
            try:
                return int(input("""
[0] SAIR                             
[1] +
[2] -
[3] *
[4] /
[5] EXIBIR VALORES
--->>>"""
))
            except ValueError:
                print("Somente Numeros")
                

ca = Calculadora()
bd = Banco_Dados()

interface = Interacao(calc = ca, banco = bd) 

while True:
    
    opcao = interface.menu()
    
    if opcao == 0:
        print("Encerrando !!!")
        break
    
    elif opcao in [1,2,3,4]:
        
        valor1, valor2 = interface.adicionar()
        
        if opcao == 1:
            resultado = interface.calc.somar(valor1,valor2)
            print(resultado)
        
        elif opcao == 2:
            resultado = interface.calc.subtrair(valor1,valor2)
            print(resultado)
        
        elif opcao == 3:
            resultado = interface.calc.multiplicar(valor1,valor2)
            print(resultado)
            
        elif opcao == 4:
            resultado = interface.calc.dividir(valor1,valor2)
            print(resultado)
        
        interface.banco.historico.append(resultado)
        
        
    elif opcao == 5:
        interface.banco.exibir()
        
    
    else:
        print("Escolha apenas entre 1 até 5")
                    
               
                
                
                
                