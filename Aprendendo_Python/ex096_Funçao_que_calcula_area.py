def area(a, b):
    area = a * b
    print(f'a área do terreno é {area}')

print('Digite as dimensões do terreno para receber a área')
a = float(input('LARGURA: '))
b = float(input('COMPRIMENTO: '))
area(a, b)
