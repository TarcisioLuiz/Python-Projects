def maior(* num):
    tam = len(num)
    print(f'foram passados {tam}')
    ma = 0
    for x in range(0, tam):
        if ma == 0:
            ma = num[x]
        if num[x] > ma:
            ma = num[x]
    print(f'O maior número foi {ma}')


maior(5, 8, 2)
maior(1, 9, 3, 6, 5, 10)
maior(56, 79, 36, 61, 83, 8)
