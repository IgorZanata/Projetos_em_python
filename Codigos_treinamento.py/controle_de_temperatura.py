#controle_de_temperatura
#Crie uma classe chamada Termometro que simule o funcionamento de um aparelho de controle de temperatura.
#Atributos privados
#Ao criar um objeto, a temperatura inicial deve ser informada pelo usuário.
#O aparelho deve iniciar desligado.
#Implemente os seguintes métodos:
#ligar()
#Liga o aparelho.
#desligar()
#Desliga o aparelho.
#aumentar_temperatura()
#Aumenta a temperatura em 1 grau.
#Só pode funcionar se o aparelho estiver ligado.
#A temperatura não pode ultrapassar 30°C.
#diminuir_temperatura()
#Diminui a temperatura em 1 grau.
#Só pode funcionar se o aparelho estiver ligado.
#A temperatura não pode ficar abaixo de 16°C.
#mostrar_status()
#Exibe a temperatura atual.
#Exibe se o aparelho está ligado ou desligado.

class Termometro:
    def __init__(self,temperatura_inicial):   
            self.__temperatura = temperatura_inicial
            self.ligado = False
            
            
    @property
    def valor(self):
        return f"Temperatura {self.__temperatura }ºC"
    
    @property
    def valor_numerico(self):
        return self.__temperatura
    
    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            return "Termometro foi Ligado"
        else:
            return "Termometro já está ligado"

    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            return "Termometro Foi Desligado"     
        else:
            return "Termometro já está desligado"
        
    def situacao(self):
        if self.ligado == True:
            return "Termometro está ligado"   
        else:
            return "Termometro está desligado"
        
    def aumento(self): 
        if not self.ligado:
            return "Aparelho desligado" 
        elif self.__temperatura >= 30:
            return "Limite maximo 30°C"   
        else:
            self.__temperatura += 1
            return f"TEMPERATURA:{self.__temperatura}"

    def baixar(self):
        if not self.ligado:
            return "Aparelho desligado"  
        elif self.__temperatura <= 16:
            return "Limite minimo 16"
        else:
            self.__temperatura -= 1
            return f"{self.valor}"

class Interface:
    def __init__(self,conexao):
        self.conexao = conexao 

    def exibir_situação(self):
        print(f"======TEMPERATURA ATUAL======")
        print(self.conexao.situacao(), f"\n",self.conexao.valor)
    
    def menu_ligar(self):
        while True:
            try:
                return int(input("""
1 - LIGAR
2 - DESLIGAR
>>>"""))
            except ValueError:
                print("Somente a opcao 1 e 2")
                
    def menu_temperatura(self):
        while True:
            valor = input(" [+] AUMENTAR\n [-] BAIXAR\n [S] SAIR\n>>>").strip().upper()
            if valor in ["+", "-","S"]:
                return valor
            else:
                print("Somente os valores [+] | [-] | [S]")
        
    def aumentar_temperatura(self): 
        while True:
            opcao = input("[+] AUMENTAR\n[S] VOLTAR MENU\n:").strip().upper()
                
            if opcao =="+":
                self.conexao.aumento()
                print(self.conexao.valor)
                if self.conexao.valor_numerico == 30:
                    print("LIMITE MÁXIMO DE 30º ATINGIDO")
            elif opcao =="S":
                return
            else:
                print("Digite novamente as opcões [+] / [S] ")
       
    def baixar_temperatura(self):
        while True:
            opcao = input("[-] BAIXAR\n[S] VOLTAR MENU\n:").strip().upper()
            if opcao =="-":
                self.conexao.baixar()
                print(self.conexao.valor)
                if self.conexao.valor_numerico == 16:
                    print("LIMINE MINIMO DE 16 ºC ATINGIDO ")
            elif opcao =="S":
                return
            else:
                print("Digite novamente as opções [-] / [S]")

def valor_inicial_temperatura():
    while True:
        try:    
            valor = int(input("Valor temperatura inicial:"))  
            if valor >= 16 and valor <=30:   
                return valor
            else:
                print("Valores entre 15 °C até 30 ºC")
        except ValueError:
            print("Somente numeros") 

valor = valor_inicial_temperatura()
print("")
ter = Termometro(valor)
interacao = Interface(ter)

while True:
    interacao.exibir_situação()
    opcao = interacao.menu_ligar()
    print("")
    
    if opcao in [1,2]:
        if opcao == 2:
            print(interacao.conexao.desligar())
           
    
        elif opcao == 1:
            print(interacao.conexao.ligar())
            interacao.exibir_situação()
            print("")
            
            while True:
                opcao2 = interacao.menu_temperatura()
                if opcao2 =="+":
                    interacao.aumentar_temperatura()  
                elif opcao2 =="-":
                    interacao.baixar_temperatura()
                elif opcao2 =="S":
                    print("SAINDO")
                    break  
                else:
                    print("Valor invalido\nDigite Novamente")
    else:
        print("Somente valores entre 1 e 2\nDigite Novamente")
            











