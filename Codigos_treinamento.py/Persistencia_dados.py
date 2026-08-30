import pandas as pd

class Dados:
    def __init__(self):
        self.estoque = {}
        
class Dados_lista:
    def __init__(self):
        self.estoque_lista = []


class Produto:
    def __init__(self,cod, nome, qtd):
        self.cod = cod
        self.nome = nome
        self.qtd = qtd
        
    def para_dicionario(self):
        return {"Código" : self.cod, "Nome" : self.nome, "Quantidade" : self.qtd}   
         
class Interacao:
    def __init__(self):
        self.conexao = Dados()
        self.conexao_lista = Dados_lista()
        
    def buscar_lista(self,valor):
        for item in self.conexao_lista.estoque_lista:
            if valor == item.cod:
                return True
        else:
            return False
        
    def digitar_cod(self):
        while True:
            try:    
                return int(input("Código:"))
            except ValueError:
                print("Somente numeros")
            
    def digitar_qtd(self):
        while True:
            try:  
                return int(input("Quantidade:"))
            except ValueError:
                print("Somente numeros")            
            
    def digitar_nome(self):
        while True:
            nome = input("Nome:")  
            if nome:
                return nome
            else:
                print("Linha em branco\nDigite Novamente o Nome")
      
    def cadastrar(self):
        cod = self.digitar_cod()
        if not cod in self.conexao.estoque:
            nome = self.digitar_nome()
            qtd = self.digitar_qtd()
            self.conexao.estoque[cod] = Produto(cod, nome, qtd)
            print("Cadastro realizado") 
        else:
            print("Produto já cadastrado")
            
    def cadastrar_lista(self):
        cod = self.digitar_cod()
        if not self.buscar_lista(cod):
            nome = self.digitar_nome()
            qtd = self.digitar_qtd()
            produto = Produto(cod,nome,qtd)
            self.conexao_lista.estoque_lista.append(produto)
            print("Item cadastrado com Sucesso !!")
        else:
            print("Item já cadastrado")
           
    def exibir_lista(self):
        if not self.conexao_lista.estoque_lista:
            print("LISTA VAZIA !!")
        else:
            for item in self.conexao_lista.estoque_lista:
                print(f"Cod: {item.cod:<15} | Nome {item.nome:<15} | Quantidade {item.qtd:<15}")
        
    def menu(self):
        while True:
            try:
                return int(input("""
1 ADICIONAR EM DICIONARIO
2 SALVAR CSV DICIONARIO
3 EXIBIR CSV
4 ADICIONAR EM LISTA
5 SALVAR LISTA EM CSV
6 SALVAR TXT
--->>>"""))
            except ValueError:
                print("Somente numeros")
            
    def menu_principal(self):
        while True:
            try:
                opcao = self.menu()
                if opcao in [1,2,3,4,5,6,7]:
                    if opcao == 1:
                        self.cadastrar()
                    elif opcao ==2:
                        self.salvar()
                    elif opcao ==3:
                        self.ler()
                    elif opcao == 4:
                        self.cadastrar_lista()
                    elif opcao == 5:
                        self.salvar_lista()
                    elif opcao == 6:
                        self.salvar_txt()
                else:
                    print("Somente os numeros entre 1 e 6")
            except ValueError:
                print("Somente numeros")
        
    def salvar(self):    
        lista_itens = []
        for item in self.conexao.estoque.values():
            dicionario = item.para_dicionario()
            lista_itens.append(dicionario)
        escritor = pd.DataFrame(lista_itens)
        escritor.to_csv("salvos.py/estoque.csv", sep=";", index=False, encoding="utf-8-sig")
        print("Salvo")
    
    def ler(self):
        leitor = pd.read_csv("salvos.py/estoque.csv", sep=";", encoding="utf-8-sig")
        print(leitor.to_string(index=False))

    def salvar_lista(self):
        dados = [
            {
            "Código" : item.cod,
             "Nome" : item.nome,
             "Quantidade" : item.qtd
             }
            for item in self.conexao_lista.estoque_lista
        ]
        
        escritor = pd.DataFrame(dados) 
        escritor.to_csv("salvos.py/estoque_lista_para.csv", sep=";", index=False, encoding="utf-8-sig")    
        print("Salvo com Pandas !")
    
    def salvar_txt(self):
        dados = [
            {"Código" : item.cod,
             "Nome" : item.nome,
             "Quantidade" : item.qtd
             }
            for item in self.conexao_lista.estoque_lista
        ]        
        escritor = pd.DataFrame(dados)
        escritor.to_csv("salvos.py/estoque_lista.txt", sep="\t", index=False, encoding="utf-8-sig")
        print("Salvo em txt")







teste = Interacao()
teste.menu_principal()