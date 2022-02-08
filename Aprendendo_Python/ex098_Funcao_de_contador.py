def contador(inicio, fim, passo):
    for x in range (1, 11):
        print(x)
    print('-=' * 30)
    count = 10
    while (count != 0):
        if (count%2 == 0):
            print(count)
        count = count - 1
    print('-=' * 30)
    count2 = inicio
    while (count2 != fim):
        print(count2)
        count2 = count2 + passo

print('Digite os valores correspondetes a contagem: ')
inicio = int(input('Digite o valor incial:'))
fim = int(input('Digite o valor final: '))
passo = int(input('Digite o valor da passada '))
contador(inicio, fim, passo)