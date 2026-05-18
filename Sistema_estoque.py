class Farmacia:
    def __init__(self,nome,qtd):
        if qtd < 0:
            raise ValueError ("Valor invalido")
        
        self.qtd = qtd
        self.nome = nome

    
    def saque(self,valor):

        if 0 < valor <= self.qtd:
            self.qtd -= valor
            
        else:
            return "Valor invalido"

    
    def exibir(self):
        return f"Nome:{self.nome} | Quantidade:{self.qtd}"

    def deposito(self,valor):

        if valor > 0:
            self.qtd += valor
        
        else:
            return "Valor invalido"
    
    def alterar(self,valor):

        self.nome = valor

    def alterar_saldo(self, valor):
        
        if 0 < valor:
            self.qtd = valor
        
        else:
            return "Valor invalido"
        
    
    
         
        


estoque = {}

##logica##

def cadastrar(nome,qtd):

    p1 = Farmacia(nome,qtd)
    estoque[nome] = p1

def remover(nome):

    if nome in estoque:
        del estoque[nome]
        return True

    else:
        return False

def salvar():

    with open("Teste_log_inter.txt", "a", encoding = "utf-8") as arquivo:

        for chave, valor in estoque.items():
            linha = f"Nome:{chave} | Quantidade: {valor.qtd}\n"

            arquivo.write(linha)

##interface##

def cadastrar_item():

    try:
        nome = input("Nome:").strip().upper()
        qtd = int(input("Quantidade:"))
        cadastrar(nome,qtd)
        print("Cadastrado !!")
    
    except ValueError:
        print("Somente numeros")

def remover_item():

    nome = input("Digite o nome para encontrar !\n--->>>").strip().upper()

    if nome in estoque:
        remover(nome)
        print("Removido")
    
    else:
        print("Não encontrado")

def menu():
    
    print("=============================")

    try:
        return int(input("0 - Sair\n"
                         "1 - Adicionar\n" \
                         "2 - Remover\n" \
                         "3 - Exibir\n"
                         "4 - Salvar\n"
                         "5 - Saque de saldo\n" \
                         "6 - Adicionar saldo\n"
                         "7 - Procurar item\n"
                         "8 - Alterar item\n" \
                         "--->>>"))
    
    except ValueError:
        print("Somente numeros")
        return None

def exibir():
     
    for chave in estoque.values():
        print(chave.exibir())

def salvar_item():
    salvar()
    print("Item Salvo com sucesso")

def buscar_item():

    valor = input("Digite o nome que deseja encontrar:").strip().upper()

    if valor in estoque:
        return valor
    
    else:
        print("Nome não encontrado")
        return None
    
def sacar_item():

    nome = buscar_item()

    if nome is not None:
            
        try:
            
            valor = int(input("Digite a quantidade que deseja sacar\n--->>>"))
            item = estoque[nome]
                ###ou estoque[nome].saque(valor)

            resultado = item.saque(valor)

            if resultado:
                print(resultado)
            
            else:
                print("Saque realizado")
                
        
        except ValueError:
            print("Somente numeros")

def exibir_unico():

    nome = buscar_item()

    if nome is not None:

        item = estoque[nome]
        print(item.exibir())

def depositar_item():

    nome = buscar_item()

    if nome is not None:

        try:
            valor = int(input("Digite o quando deseja depositar\n--->>>"))

            item = estoque[nome]

            resultado = item.deposito(valor)

            if resultado:
                print(resultado)
            
            else:
                print("Deposito realizado")
                
        
        except ValueError:
            print("Valor invalido")
            return None
        
def alterar_nome_qtd():

    nome = buscar_item()

    if nome:

        try:    
            opcao = int(input("Alterar nome [1] | Alterar quantidade [2]\n--->>>"))
        
        except ValueError:
                print("Valor invalido")


        if opcao == 1:
            nome_atualizado = input("Novo nome:").strip().upper()
            estoque[nome_atualizado] = estoque.pop(nome)
            estoque[nome_atualizado].alterar(nome_atualizado)
            
            print("Nome alterado com sucesso")
                
        if opcao == 2:

            try:    
                valor_qtd = int(input("Digite a quantidade para alterar"))
                estoque[nome].alterar_saldo(valor_qtd)
                print("Alterado com sucesso")
                    
            except ValueError:
                print("Valor invalido")
                return None
                
while True:

    opcao = menu()

    if opcao == None:
        continue

    if opcao == 0:
        print("Finalizando")
        break

    if opcao == 1:

        cadastrar_item()
      
    elif opcao == 2:

        remover_item()

    elif opcao == 3:

        exibir()

    elif opcao == 4:
       
       salvar_item()

    elif opcao == 5:
      
      sacar_item()
    
    elif opcao == 6:

        depositar_item()
    
    elif opcao == 7:

        exibir_unico()
    
    elif opcao == 8:

        alterar_nome_qtd()


            
            


