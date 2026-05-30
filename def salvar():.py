def salvar():
    caminho = "Documentos/estrada/TCC_PYTHON.txt"
    with open (caminho, "w", encoding = "utf - 8") as arquivo: 
        dados = "Mãe 16 997664624\nIgor 16 997634624\n"
        arquivo.write(dados)

def ler():
    with open("Documentos/olho/Buscador.txt", "r", encoding = "utf-8") as documento:
        dados = documento.read()
        print(dados)


ler()


     

        


