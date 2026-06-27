class Calculadora:
    
    def somar(self,a,b):
        return a + b
    
    def subtrair(self,a,b):
        return a - b
    
    def mult(self,a,b):
        return a * b
    
    def dividir(self,a,b):
        
        try:
            return a / b
        
        except ZeroDivisionError: ("erro")




def valor():

    try:
        a = int(input("Digite um valor:"))
        b = int(input("Digite outro valor:"))
        

    except ValueError:
        print("Somente numeros")
        return None


def menu():

    try:
        return int(input("1 - SOMAR\n" \
                        "2 - SUBTRAIR\n" \
                        "3 - MULTIPLICAR\n" \
                        "4 - DIVIDIR\n" \
                        "--->>>"))
    except ValueError:
        print("Somente Numeros")
        return None
    

while True:

    print("===================")

    opcao = menu()

    if opcao == 1:

        p1.somar(valor())
        print(p1.somar())
    
    elif opcao == 2:

        valor(p1.subtrair())

