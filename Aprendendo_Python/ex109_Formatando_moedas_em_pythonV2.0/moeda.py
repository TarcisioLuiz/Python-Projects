def aumentar(preco, porcent, format):
    porcent = porcent/100
    if format == 'S':
        return moeda(preco + (preco * porcent))
    else:
        return preco + (preco * porcent)


def diminuir(preco, porcent, format):
    porcent = porcent/100
    if format == 'S':
        return moeda(preco - (preco * porcent))
    else:
        return preco - (preco * porcent)


def dobro(preco, format):
    if format == 'S':
        return moeda(preco * 2)
    else:
        return preco * 2


def metade(preco, format):
    if format == 'S':
        return moeda(preco/2)
    else:
        return preco/2


def moeda(preco):
    moeda = 'R$' + str(preco)
    return moeda
