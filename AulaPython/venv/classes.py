class NomeClass:
    '''Docstrings'''
    dado = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def soma (self):
        soma = self.x + self.y + self.dado
        return ('o valor da soma é: ',soma)
soma = NomeClass(4, 5)
print(soma.soma())