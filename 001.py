class Estoque:
    def __init__(self,nome,qtd):
        self.nome = nome
        if qtd >= 0:
            self.qtd = qtd
        
        else:
            raise ValueError ("Valor invalido")


    
    def mostrar(self):
        print(f"Nome:{self.nome} | Quantidade: {self.qtd}")



estoque = {}

#=====================================
##logica###
##====================================

def adicionar(nome,qtd):

    estoque[nome] = Estoque(nome,qtd)
    
def remover(nome):

    if nome in estoque:
        del estoque[nome]
        return True
    
    return False

def salvar():

    with open ("Estoque_farmácia.txt", "w", encoding = "utf-8") as arquivo:

        for chave, valor in estoque.items():

            linha = f"{chave} || Quantidade: {valor.qtd}\n"

            arquivo.write(linha)



##=====================================
## Interface
##=====================================

def remover_item():

    nome = input("Digite o nome para encontrar:").strip().upper()

    if remover(nome):
        print("Removido")
    
    else:
        print("Item não enontrado")

def menu():
    
    try:

        return int(input("1 - Adicionar\n" \
                        "2 - Remover\n" \
                        "3 - Exibir\n" \
                        "4 - Salvar\n" \
                        "--->>>"))

    except ValueError:
        print("Somente numeros")
        return None
                      
def adicionar_dados():

    try:
        nome = input("NOME:").strip().upper()
        qtd = int(input("Quantidade:"))

        adicionar(nome,qtd)

        print("Cadastro realizado")
        
    
    except ValueError:
        print("Somente numeros")

def salvar_item():
    salvar()
    print("Salvo com sucesso")
    

while True:

    print("====================================")

    opcao = menu()

    if opcao == None:
        continue

    if opcao == 1:
        adicionar_dados()

    elif opcao == 2:
        remover_item()
    
    elif opcao == 3:
        for i in estoque.values():
            i.mostrar()

    elif opcao == 4:
        salvar_item()
        

                        

