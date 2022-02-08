#matriz = [[0, 0, 0, 0], [0, 0, 0, 0]]
#for l in range(0, 2):
    #for c in range(0,4):
    #    matriz[l][c] = input(f'digite o valor da posição {l}{c}: ')
    #    print(matriz[l][c], end=' ')
    #    print()
par=0
matriz = [[0, 0], [0, 0], [0, 0]]
for l in range(0, 3):
    for c in range(0,2):
        matriz[l][c] = int(input(f'digite o valor da posição {l}{c}: '))
        print('/' * 10)
        if matriz[l][c] % 2 == 0:
            par = par + 1
for l in range(0, 3):
    for c in range(0,2):
        print(matriz[l][c], end=' ')
    print()

print('a quantidade de par é: ',par)
