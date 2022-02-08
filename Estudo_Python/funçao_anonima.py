def contador_letras(lista):
    contador =[]
    for x in lista:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


contador_letras2 = lambda lista: [len(x) for x in lista]

print(contador_letras(['cachorro', 'gato', 'papagaio']))
print(contador_letras2(['cachorro', 'gato', 'papagaio']))

calculadora = {
    'soma' : lambda a, b: a + b,
    'subtração' : lambda a, b: a - b,
    'multiplicação' : lambda a, b: a * b,
    'divisão' : lambda a, b: a / b
}

soma = calculadora['soma']
print(soma(10, 2))