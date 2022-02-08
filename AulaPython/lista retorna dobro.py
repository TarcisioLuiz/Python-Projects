def dobro(array):
    posição = 0
    while posição <len(array):
        array[posição] = array[posição]*2
        posição = posição + 1
    return array

a = [2, 4, 5, 6]
dobro(a)
print(dobro(a))