def aumentar(preco, porcent):
    porcent = porcent/100
    return preco + (preco * porcent)


def diminuir(preco, porcent):
    porcent = porcent/100
    return preco - (preco * porcent)


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco/2


def resumo(preco, aumento, diminui):
    print('RESUMO VALOR')
    print('-=' *30)
    print(f'Preço analisado: R${preco}')
    print(f'Dobro R${dobro(preco)}')
    print(f'Metade R${metade(preco)}')
    print(f'{aumento}% de aumento R${aumentar(preco, aumento)}')
    print(f'{diminui}% de redução R${diminuir(preco, diminui)}')