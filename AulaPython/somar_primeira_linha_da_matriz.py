a=[[0, 0, 0], [0, 0, 0]]
plinha = 0
for l in range(0,2):
    for c in range(0,3):
        a[l][c] = int(input(f'digite um n para a posição {l}{c}: '))
    for c in range(0,3):
        plinha=plinha + a[0][c]
    print(f'a soma dos valores da primeira linha é: {plinha}')
    for l in range(0,2):
        for c in range(0,3):
            print(f'{a[l][c]:^4}',end='')
        print()