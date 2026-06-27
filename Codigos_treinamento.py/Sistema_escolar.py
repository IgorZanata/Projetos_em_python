class Calculadora:
    def __init__(self):
        self.historico = []
    
    def somar(self,x1,x2):
        resultado =  x1 + x2
        self.historico.append(resultado)
        return resultado
    
    def subtrair(self,x1,x2):
        resultado = x1 - x2
        self.historico.append(resultado)
        return resultado
    
    def mult(self,x1, x2):
        resultado = x1 * x2
        self.historico.append(resultado)
        return resultado

    def dividir(self,x1,x2):
        try:
            resultado =  x1 / x2
            self.historico.append(resultado)
            return resultado
        
        except ZeroDivisionError:
            print("Não se pode dividir por zero")
            return
          
calc = Calculadora()

def salvar(resultado):

    with open ("Resultados_Contas.txt", "a", encoding = "utf8") as arquivo: 
        arquivo.write(str(resultado) + "\n")




def menu():

    try:
        return int(input("1 - Somar\n" \
                        "2 - Subtrair\n" \
                        "3 - Multipilcar\n" \
                        "4 - Dividir\n"
                        "0 - Sair\n" \
                        "--->>>"))
    except ValueError:
        print("Somente numeros")
        return None
    
while True:

    print("=====================")
    opcao = menu()

    if opcao == None:
        continue

    if opcao == 0:
        print("Encerrando")
        break


    try:
        x1 = int(input("Digite um numero\n--->>>"))
        x2 = int(input("Digite outro numero\n--->>>"))
    
    except ValueError:
        print("Somente numeros")
        continue

    if opcao == 1:

        valor = calc.somar(x1,x2)
        texto = f"{x1} + {x2} = { valor}"
        print(texto)
        salvar(texto)
    
    elif opcao == 2:

        valor = calc.mult(x1,x2)
        texto = f"{x1} x {x2} = { valor}"
        print(texto)
        salvar(texto)

    elif opcao == 3:

        valor = calc.subtrair(x1,x2)
        texto = f"{x1} - {x2} = { valor}"
        print(texto)
        salvar(texto)

    elif opcao == 4:

        valor = calc.dividir(x1,x2)
        texto = f"{x1} / {x2} = { valor}"
        print(texto)
        salvar(texto)









        