def fatorial():
    f =1
    n = int(input('digite um número: '))
    for x in range(n,0,-1):
        f = x*f
    return f
print(fatorial())