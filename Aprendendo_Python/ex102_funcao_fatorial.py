def fatorial(x, show=False):
    c = x
    while c != 2:
        if (show == True):
            print(f'{x}x{c-1}={x * (c-1)}')
        x = x * (c - 1)
        c = c -1
    print(x)


x = int(input('Digite um número: '))
escolha = str(input('Você quer vê a conta do fatorial? [S/N] '))
if (escolha in 'SN'):
     if (escolha == 'S'):
         show = True
     else: show = False

fatorial(x, show)