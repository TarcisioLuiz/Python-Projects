class produto:
    def __init__(self):
        self.codigo: codigo
        self.nome: nome
        self.preco: preco
        self.quantidade: quantidade
codigo = int(input('digite o código: '))
nome = str(input('digite o nome: '))
preco = float(input('digite o preço: '))
quantidade = int(input('digite a quantidade: '))
print(codigo, nome, preco, quantidade)
mudar = int(input('deseja alterar? se sim digite (1) se não digite (2) '))
if mudar == 2:
    print(f'seu produto final é: {codigo, nome, preco, quantidade}')
elif mudar == 1:
    escolha = int(input('qual você deseja mudar:\n 1- codigo\n 2-nome\n 3-preco\n 4-quantidade '))
    if escolha == 1:
        codigo = int(input('digite o código: '))
        print(codigo, nome, preco, quantidade)
    elif escolha == 2:
        nome = str(input('digite o nome: '))
        print(codigo, nome, preco, quantidade)
    elif escolha == 3:
        preco = float(input('digite o preço: '))
        print(codigo, nome, preco, quantidade)
    elif escolha == 4:
        quantidade = int(input('digite a quantidade: '))
        print(codigo, nome, preco, quantidade)
    else:
        print('erro')





