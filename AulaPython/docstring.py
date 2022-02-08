def matriz():
    """
    esse código tem o proposito de inserir dados dentro de uma matriz 3 por 4
    :return: ele retornar o resultado da função em que está inserido (matriz())
    """
    matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for l in range(0,3):
        for c in range (0, 4):
            matriz[l][c] = int(input('digite os números: '))
    return (matriz)
a = matriz()
for x in a:
    print(x)