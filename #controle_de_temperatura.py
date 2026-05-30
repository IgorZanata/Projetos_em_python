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
    def __init__(self, temperatura):

        if temperatura >= 16 and temperatura <= 30:
            self.__temperatura = temperatura
            self.ligado = False
        
        else:
            raise ValueError ("erro")

        
        
       

    
    def get_valor(self):
        return f"Temperatura {self.__temperatura }ºC"


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
            return f"{self.get_valor()}"

    
    def baixar(self):

        if not self.ligado:
            return "Aparelho desligado"
        
        elif self.__temperatura <= 16:

            return "Limite minimo 16"
        
        else:

            self.__temperatura -= 1
            return f"{self.get_valor()}"

        



p1 = Termometro(9)


print(p1.get_valor())











