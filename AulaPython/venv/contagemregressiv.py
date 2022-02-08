def valor(n):
    from time import sleep
    if n == 0:
        print(0)
        print('fim')
    else:
        print(n)
        sleep(0.7)
        valor(n-1)


valor(int(input('digite um valor para a contagem: ')))
