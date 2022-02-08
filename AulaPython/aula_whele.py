x=int(input('digite o primeiro número '))
y=int(input('digite o segundo número '))
print('escolha uma opção\n1- soma:\n2- subtração\n3- digite novos números\n4- sair do programa')
escolha=int(input())
while escolha !=4:
    if escolha ==1:
        print(x + y)
        escolha = int(input())
    elif escolha == 2:
        print(x - y)
        escolha = int(input())
    elif escolha == 3:
        x = int(input('digite o primeiro número '))
        y = int(input('digite o segundo número '))
        escolha = int(input())
    else:print('fim do programa')



