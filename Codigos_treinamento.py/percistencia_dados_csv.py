#1. Criar a Classe Venda
#Definir o método __init__ com os atributos: id_venda (int), data (str), produto (str), quantidade (int) e preco_unitario (float).
#Criar o método calcular_faturamento() que retorna a multiplicação de quantidade por preco_unitario.
#2. Criar a Classe GerenciadorDeVendas
#Inicializar o atributo vendas como uma lista vazia no __init__.
#Implementar o método carregar_csv(caminho_arquivo) para ler o CSV nativo (ex: csv.DictReader), converter os tipos numéricos e instanciar objetos Venda na lista.
#Implementar o método faturamento_total() para somar o faturamento de todas as vendas.
#Implementar o método produto_mais_vendido() para identificar o produto com maior quantidade acumulada.
#Implementar o método exportar_resumo_csv(caminho_saida) para gravar o novo arquivo CSV com as colunas Produto e Faturamento_Total_Produto usando csv.writer.
#3. Execução e Teste
#Criar o arquivo de entrada vendas.csv com os dados de teste fornecidos.
#Instanciar o GerenciadorDeVendas, carregar os dados e exibir o faturamento total e o produto mais vendido no terminal.
#Verificar se o arquivo resumo_vendas.csv foi gerado corretamente após a execução.

import csv

class Venda:
    def __init__(self, id_venda, produto, quantidade, preco):
        self.id_venda = id_venda
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        
    def calculad_faturamento(self):
        valor = self.quantidade * self.preco
        return valor
    
   
class GerenciadorVendas:
    def __init__(self):
        self.estoque = []
    

    def salvar(self):
            with open("saída_vendas.csv", "w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["ID_Venda", "Produto", "Quantidade", "Preço"])
                escritor.writerow(["ID_cocolate", "Preço"])
                for item in self.estoque:
                    escritor.writerow([
                        item.id_venda,
                        item.produto,
                        item.quantidade,
                        item.preco
                        ])
            print("Salvo")

class Interacao:
    def __init__(self,conexao):
        self.conexao = conexao
        
    def adicionar_id(self):
        while True:
            try:
                return int(input("id da venda:"))
            except ValueError:
                print("Somente numeros")    
        
    def adicionar_produto(self):
        while True:
            produto = input("Produto:").strip().upper()
            if produto:
                return produto
            else:
                print("Sem dados\nDigite algo")
    
    def adicionar_quantidade(self):
        while True:
            try:
                return int(input("Quantidade:"))
            except ValueError:
                print("Somente numeros")
    
    def adicionar_preco(self):
        while True:
            try:
                return float(input("Preço R$"))
            except ValueError:
                print("Somente numeros")
    
    
    
    
    def cadastrar(self):
        id_venda = self.adicionar_id()
        produto = self.adicionar_produto()
        quantidade = self.adicionar_quantidade()
        preco = self.adicionar_preco()
        self.conexao.estoque.append(Venda(id_venda,produto,quantidade,preco))
        print("Cadastro realizado com sucesso")
        
    def menu(self):
        while True:
            try:
                opcao = int(input("1 - CADASTRAR\n2 - SAIR\n--->>>"))
                if opcao == 1:
                    self.cadastrar()
                    self.conexao.salvar()
                elif opcao == 2:
                    return
                else:
                    print("Somente valores 1 e 2")
            except ValueError:
                print("Somente numeros")
           
                

teste = GerenciadorVendas()
interacao = Interacao(teste)

interacao.menu()