from random import randint

def sorteia(list):
    for x in range(0, 5):
        num = randint(0,10)
        numeros.append(num)
    print(numeros)

def somaPar(list):
    soma = 0
    for x in range(0, len(numeros)):
        if numeros[x]%2 == 0:
            soma = soma + numeros[x]
    print(soma)


numeros = list()
sorteia(numeros)
somaPar(numeros)
