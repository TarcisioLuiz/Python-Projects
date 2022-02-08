def aumentar(preco, porcent):
    porcent = porcent/100
    return moeda(preco + (preco * porcent))


def diminuir(preco, porcent):
    porcent = porcent/100
    return moeda(preco - (preco * porcent))



def dobro(preco):
    return moeda(preco * 2)

def metade(preco):
    return moeda(preco/2)

def moeda(preco):
    moeda = 'R$' + str(preco)
    return moeda
