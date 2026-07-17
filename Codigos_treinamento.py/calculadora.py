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
        
    def ler_arquivo(self):
        print("========| ITENS SALVOS |==========")
        with open ("Projetos_em_python/Codigos_treinamento.py/Resutados_Operações.txt", "r", encoding="utf-8") as arquivo:
            leitura = arquivo.read()
            print(leitura)
        print("==================================")
        
    def salvar(self,a,b,operacao,resultado):
        caminho = "Projetos_em_python/Codigos_treinamento.py/Resutados_Operações.txt"
        with open(caminho, "a",encoding="utf-8")as arquivo:
            linha = f"{a} {operacao} {b} = {resultado}\n------------\n"
            arquivo.write(linha)
        print("SALVO COM SUCESSO")
                
        
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
            operacao ="+"
            print(resultado)
        
        elif opcao == 2:
            resultado = interface.calc.subtrair(valor1,valor2)
            operacao ="-"
            print(resultado)
        
        elif opcao == 3:
            resultado = interface.calc.multiplicar(valor1,valor2)
            operacao ="*" 
            print(resultado)
            
        elif opcao == 4:
            operacao ="/"
            resultado = interface.calc.dividir(valor1,valor2)
            print(resultado)
        
        interface.banco.historico.append(resultado)
        interface.banco.salvar(valor1,valor2,operacao,resultado)
        
    elif opcao == 5:
        interface.banco.ler_arquivo()
        
    
    else:
        print("Escolha apenas entre 1 até 5")
                    
               
                
                
                
                