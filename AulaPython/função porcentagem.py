salario = float(input('digite seu salario? ').replace(".","").replace(",","."))
def desconto():
    desconto = (salario*7.5/100)
    x = salario - desconto
    return desconto

def inss():
    desconto = (salario*7.5/100)
    x = salario - desconto
    return x

print(f'seu salario liquido é {inss()} e o desconto do INSS é {desconto()}')
