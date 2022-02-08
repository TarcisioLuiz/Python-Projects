def fatorial(valor):
    f = 1
    for x in range(valor, 0, -1):
        f = x * f
    return f