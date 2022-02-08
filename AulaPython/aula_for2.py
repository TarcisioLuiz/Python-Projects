a1=int(input('digite o número: '))
r=int(input('digite a razão: '))
n=int(input('número de elementos a ser exibidos: '))
resultado = a1 + (n-1)*r
for x in range(a1, resultado, r):
    print(x)