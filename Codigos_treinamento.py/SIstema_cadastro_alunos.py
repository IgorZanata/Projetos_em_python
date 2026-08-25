import pandas as pd

class Banco_dados:
    def __init__(self):
        self.usuarios = {}
 
    def exibir(self):
        print("======USUARIOS======")
        for chave, valor in self.usuarios.items():
            print(f"RA: {chave} |Nome: {valor.nome} | Idade:{valor.idade}")
            print("===============")

    def buscar(self,ra):
        if ra in self.usuarios:
            return self.usuarios[ra] 
        else:
            return None
        
         
class Pessoa:
    def __init__(self,ra,nome,idade):
        self.ra = ra
        self.nome = nome
        self.idade = idade
        
    def para_dicionario(self):
        return {"RA" : self.ra, "NOME": self.nome, "IDADE" : self.idade }
        
    
class Interface:
    def __init__(self):
        self.banco = Banco_dados()
 
    def menu(self):
        while True:
            try:
                opcao = int(input("""
[0] SAIR                         
[1] ADICIONAR
[2] EXIBIR
[3] ALTERAR NOME
[4] LER CSV
    --->>>"""))
                
                if opcao in [0,1,2,3,4]:
                    return opcao
                else:
                    print("Opcão invalida !\nSomente numeros entre [0 até 3]")
            except ValueError:
                print("Somente Numeros")
            
    def salvar(self):
        lista_dados = []
        
        for pessoa in self.banco.usuarios.values():
            dicionario = pessoa.para_dicionario()
            lista_dados.append(dicionario)
            
        escritor = pd.DataFrame(lista_dados)
        escritor.to_csv("aula_006_dic.csv", sep=";", index=False, encoding="utf-8-sig")
        print("Salvo")
    
    
    def ler(self):
        leitor = pd.read_csv("aula_006_dic.csv", sep=";", encoding="utf-8-sig")
        print(leitor.to_string(index=False))
        print("Finalizado")
    
    
    
    def adicionar(self):
        try:
            ra = int(input("R.A:"))
        except ValueError:
            print("Somente Numeros")
            return None

        if ra in self.banco.usuarios:
            print("Aluno Já cadastrado")
        else:
            try:
                nome = input("Nome:")
                idade = int(input("Idade:"))
                
                if idade >= 0:
                    p1 = Pessoa(ra,nome,idade)
                    self.banco.usuarios[ra] = p1
                    self.salvar()  
                else:
                    print("IDADE INVALIDA")
            except ValueError:
                print("Somente Numeros")

    def alterar_nome(self):
        try:
            ra_busca = int(input("Digite o R.A para encontrar\n--->>>"))
        except ValueError:
            print("Somente Numeros")
            return None

        procurar = self.banco.buscar(ra_busca)

        if procurar:
            nome_atualizado = input("Digite o nome atualizado:")
            procurar.nome = nome_atualizado
            print("Nome atualizado com sucesso")
        else:
            print("Não encontrado")
         
    def menu_principal(self):      
        while True:
            opcao = self.menu()
            if opcao == None:
                continue
            if opcao == 0:
                print("Finalizando")
                break
            if opcao == 1:
                self.adicionar()
            elif opcao == 2:
                self.banco.exibir()
            elif opcao == 3:
                self.alterar_nome()   
            elif opcao == 4:
                self.ler()    
         
interacao = Interface()
interacao.menu_principal()
