class carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = input('digite o modelo: ')
        self.cor = input('digite a cor: ')
        self.ano = input('digite o ano: ')

f1 = carro('','','')
print(f'O carro {f1.modelo}, {f1.cor} e {f1.ano}')
