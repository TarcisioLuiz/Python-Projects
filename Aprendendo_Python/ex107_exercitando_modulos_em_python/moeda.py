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