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

class Interface:
    def __init__(self,banco):
        self.banco = banco
 
    def menu(self):
        
        while True:
            try:

                opcao = int(input("""
[0] SAIR                         
[1] ADICIONAR
[2] EXIBIR
[3] ALTERAR NOME
    --->>>"""))
                
                if opcao in [0,1,2,3]:
                    return opcao
                
                else:
                    print("Opcão invalida !\nSomente numeros entre [0 até 3]")
                
            except ValueError:
                print("Somente Numeros")
            

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
                    print("Cadastrado realizado com sucesso")
                        
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

p1 = Banco_dados()  
interacao = Interface(p1)

while True:

    opcao = interacao.menu()

    if opcao == None:
        continue

    if opcao == 0:
        print("Finalizando")
        break

    if opcao == 1:
        interacao.adicionar()
        
    elif opcao == 2:
        p1.exibir()
    
    elif opcao == 3:
        interacao.alterar_nome()



             
    
