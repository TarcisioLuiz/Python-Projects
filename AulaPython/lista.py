numeros = []
for x in range(0,5):
    numeros.append(int(input('escreva 5 números: ')))
x=input('deseja alterar algo? ')
if x== 'sim':
    posicao = int(input('qual posição você quer mudar: '))
    numeros[posicao-1]=int(input('digite novo número: '))
else:
    print(numeros)
print(numeros)





