def soma(x, y):
    soma = x + y
    return soma
try:
    x = int(input('Digite um número: '))
    y = int(input('Digite um número: '))
    print(soma(x, y))

except:
    print('Erro. Digite novamente ')