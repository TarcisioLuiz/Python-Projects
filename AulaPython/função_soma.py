#def soma2(x, y):
#

#resultado = soma2(10, 11)
#print('o resultado: ', resultado)


def multiplo():
    x = int(input('digite o primeiro valor: '))
    y = int(input('digite o segundo valor: '))
    if x % y == 0:
        return True
    elif y % x == 0:
        return True
    else:
        return False

print(multiplo())
