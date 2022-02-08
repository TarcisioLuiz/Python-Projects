def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            break
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            break
        else:
            return n



num1 = leiaFloat('digite um valor real: ')
num2 = leiaInt('Digite um valor inteiro: ')
