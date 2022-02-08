import random

a = []
b = 0
for y in range(0, 5):
    sorteio = random.randint(0, 10)
    for x in range(0, len(a)):
        if a[x] == sorteio:
                b = 1
    if b == 0:
            a.append(sorteio)

from random import sample

try:
    print(sample(a, 5))

except ValueError:
    print('Erro')