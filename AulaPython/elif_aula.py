casa = float(input('qual o valor da casa adquirida? '))
salario = float(input('Qual o seu salário? '))
tempo = input('em quantos anos quer pagar?')
if salario >2000 or salario < 3000:
    print('A prestação será dividida em 240 meses')

elif salario >3000 or salario < 4000:
    print('A prestação será dividida em 180 meses')

elif salario >4000:
    print('A prestação será dividida em 120 meses')

else:
    print('Empréstimo negado')
