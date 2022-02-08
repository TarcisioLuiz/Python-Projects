x = int(input('numero inicial: '))
y = int(input('numero final: '))
par = 0
impar = 0
y = y+1

for z in range(x, y):
    if z % 2 == 0:
        par = par + 1
        print(z, 'o número é par')
    else:
        impar = impar + 1
        print(x, 'o numero é impar')
print('quantidade de numeros pares ',par,' e impar', impar)
