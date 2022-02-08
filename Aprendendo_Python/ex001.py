# === PRIMEIRO E ÚLTIMO NOME ===
# nome = str(input('digite o seu nome completo ')).strip()
# x = nome.split()
# print(f'{x[0]} {x[len(x)-1]}')



# === JOGO DE ADVINHAÇÃO ===
#from random import randint
#num = randint(0,5)
#n1 = int(input('de 0 a 5 advinhe o número escolhido pelo computador '))
#if num == n1:
#    print('você acertou, parabêns!!')
#else: print(f'que pena você errou, o número era {num}')



# === RADAR ELETRÔNICO ===
#vel = int(input('digite a velocidade do carro '))
#if vel > 80:
#    x = (vel - 80)*7
#    print(f'você recebeu uma multa de {x} por excesso de velocidade')
#else: print('')



# === PAR OU IMPAR ===
#x = int(input('digite um número para saber se é par ou impar '))
#if x%2 == 0:
#    print('o número é par')
#else: print('o número é ímpar')



# === CUSTO DE VIAGEM ===
#x = int(input('digite a distância da sua viagem '))
#if x <= 200:
#    valor = x*0.5
#    print(f'o valor da viagem sera {valor}')
#else:
#    valor = x * 0.45
#valor = x *0.50 if x <= 200 else x * 0.45 #forma simplificada
#print(f'o valor da viagem será {valor}')




# === ANO BISSEXTO ===
#ano = int(input('digite o ano '))
#if ano%4== 0 and ano % 100 !=0 or ano % 400 == 0:
#   print(f'o ano {ano} é bissexto')
#else: print(f' o ano {ano} não é bissexto')



# === MAIOR E MENOR ===
#x = int(input('digite um valor '))
#y = int(input('digite um valor '))
#z = int(input('digite um valor '))
#if x > y and x > z:
#    print(f'{x} é o maior número')
#elif y > x and y>z:
#    print(f'{y} é o maior número')
#elif z > x and z>y:
#    print(f'{z} é o maior número')
#else: print('')
#if x < y and x < z:
#    print(f'{x} é o menor número')
#elif y < x and y<z:
#    print(f'{y} é o menor número')
#elif z < x and z<y:
#    print(f'{z} é o menor número')
#else: print('')



# === AUMENTOS MULTIPLOS ===
#sal = float(input('digite o valor do seu salário: '))
#if sal > 1250.00:
#    novosal = sal + sal*0.10
#else: novosal = sal + sal*0.15
#print(novosal)



# === ANALISANDO TRIANGULO ===
#x = float(input('digite o primeiro valor: '))
#y = float(input('digite o segundo valor: '))
#z = float(input('digite o terceiro valor: '))
#if x + y < z or x + z < y or y + z < x:
#    print('não é um triangulo')
#else: print('é um triangulo')



#print('\033[1;31;43mola mundo\033[m')



# === APROVANDO EMPRESTMIOS ===
#casa = float(input('Qual o valor da casa que vocÊ deseja comprar? '))
#tempo = int(input('Em quantos anos você deseja paga-la? '))
#salario = float(input('Qual o seu salario? '))
#meses = tempo * 12
#prestacao = casa/meses
#salario30 = salario * 0.30
#if prestacao > salario30:
#    print(f'O emprestimo sera negado pois a prestação de {prestacao} superou o limite de 30% do seu salário')
#elif prestacao <= salario30:
#    print(f'ParabÊns! seu emprestimo foi aprovado, as prestações serão de {prestacao} durante {meses} meses')



# === CONVERSOR DE BASES NUMÉRICAS ===
#x = int(input('digite o número para conversão '))
#escolha = int(input(f'você quer converter {x} para:\n1-binário\n2-octal\n3-hexadecimal '))
#if escolha == 1:
#    binary = bin(x)
#    print(binary[2:])
#elif escolha == 2:
#    cta = oct(x)
#    print(cta[2:])
#elif escolha == 3:
#    exa = hex(x)
#    print(exa[2:])
#else: print('erro')



# === COMPARANDO NÚMEROS ===
#x = int(input('digite um número '))
#y = int(input(' digite outro número '))
#if x > y:
#    print(f'{x} é maior que {y}')
#elif x < y:
#    print(f'{y} é maior que {x}')
#elif x == y:
#    print(f' os números {x} e {y} são iguais')



# === ALISTAMENTO MILITAR  ===
#from datetime import date
#ano = int(input('Qual o ano do seu nascimento? '))
#anoatual = date.today().year
#idade = anoatual - ano
#if idade == 18:
#    print('hora de se alistar')
#elif idade < 18:
#    restante = 18 - idade
#    print(f'ainda resta {restante} anos para se alistar')
#elif idade > 18:
#    passou = idade - 18
#    print(f'já passou {passou} anos do alistamento')



# === MÉDIA ===
#x = float(input('Digite a primeira nota: '))
#y = float(input('Digite a segunda nota: '))
#media = x + y / 2
#if media < 5.0:
#    print('reprovado')
#elif media == 5.0 and media <= 6.9:
#    print('recuperação')
#elif media >= 7.0:
#    print('aprovado')



# === CLASSIFICANDO ATLETAS ===
#from datetime import date
#x = int(input('Qual ano do seu nascimento? '))
#anoatual = date.today().year
#idade = anoatual - x
#if idade <= 9:
#    print('mirim')
#elif idade <= 14:
#    print('infantil')
#elif idade <= 19:
#    print('junior')
#elif idade == 20:
#    print('sênior')
#else: print('master')



# === ANALISANDO TRIANGULOS V2.0 ===
#x = float(input('digite o primeiro valor: '))
#y = float(input('digite o segundo valor: '))
#z = float(input('digite o terceiro valor: '))
#if x + y < z or x + z < y or y + z < x:
#    print('não é um triangulo')
#else: print('é um triangulo')
#if x == y == z:
#    print('Equilátero')
#elif x == y != z or x == z != y or y == z != x:
#    print('Isósceles')
#elif x != y != z:
#    print('Escaleno')



# === IMC ===
#altura = float(input('Qual a sua altura em cm? '))
#peso = float(input('Qual seu peso? '))
#IMC = peso/altura**2
#if IMC < 18.5:
#    print('abaixo do peso')
#elif IMC == 18.5 and IMC <= 25:
#    print('normal')
#elif IMC > 25 and IMC <= 30:
#    print('Sobrepeso')
#elif IMC > 30 and IMC <= 40:
#    print('Obesidade')
#elif IMC > 40:
#    print('Obesidade mórbida')



# === GERENCIADOR DE PAGAMENTOS ===
#x = float(input('Digite o valor do produto: '))
#escolha = int(input('Qual o formato de pagamento:'
#                    '\n1- dinheiro/cheque(10% de desconto)'
#                    '\n2- cartão(5% de desconto)'
#                    '\n3- 2x no cartão(preço nomral)'
#                    '\n4- 3x ou mais no cartão(20% de juros)\n'))
#if escolha == 1:
#    preço = x - x*0.10
#    print(preço)
#elif escolha == 2:
#    preço = x - x*0.05
#    print(preço)
#elif escolha == 3:
#    preço = x
#    print(preço)
#elif escolha == 4:
#    preço = x + x*0.2
#    print(preço)



# === PEDRA PAPEL OU TESOURA ===
#from random import randint
#x = int(input('0- pedra\n1- papel\n2- tesoura? '))
#y = randint(0,3)
#PEDRA = 0
#PAPEL = 1
#TESOURA = 2
#if x == y:
#    print(f'empate {x} {y}')
#elif x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
#    print('perdeu')
#else: print('ganhou')



# === CONTAGEM REGRESSIVA ===
#from time import sleep
#print('Contagem regressiva')
#for x in range(10, 0, -1):
#    print(x)
#    sleep(1)
#print('fim')



# === CONTAGEM PAR ===
#for x in range(0, 50):
#    if x %2 == 0:
#        print(x)
#print('fim')



# === SOMA ÍMPARES MULTIPLUS DE 3 ===
#soma = 0
#for x in range(0, 500):
#    if x %2 != 0:
#        if x %3 == 0:
#            soma = soma + x
#print(soma)



# === TABUADA ===
#n1 = int(input('digite um número de um a 10 '))
#for x in range(0, 11):
#    print(n1 * x)



# === SOMA DOS PARES ===
#soma = 0
#for x in range(0, 6):
#    n1 = int(input('digite um número: '))
#    if n1 %2 == 0:
#        soma = soma + n1
#print(soma)



# === PROGRESSÃO ARITMÉTICA ===
#a1 = int(input('digite o primeiro termo da sua progressão '))
#r = int(input('digite a razão da sua progressão '))
#for x in range(1, 10):
#    an = a1 + (x - 1) * r
#    print(an)



# === NÚMEROS PRIMOS ===
#n =int(input('digite um número: '))
#cont = 0
#for c in range(1,n + 1):
#    if n % c == 0 :
#        cont = cont + 1
#if cont > 2:
#    print('não é primo')
#else: print('é primo')




# === DECTOR DE PALINDROMO ===
#frase = str(input('digite uma frase: ')).lower().replace(" ","").strip()
#frase2 = frase[::-1]
#if frase == frase2:
#    print('é um palindromo')
#else: print("não é um palindromo")



# === GRUPO DA MAIORIDADE ===
#y =0
#z = 0
#count = 0
#while count < 7:
#    count = count + 1
#    x =int(input('digite um ano '))
#    if 2021 - x >=18:
#        y = y+1
#    else: z = z+1
#print(f'{y} deles são maior de idade e {z} não são')



# === MAIOR E MENOR DA SEQUÊNCIA ===
#count = 0
#ma = 0
#me = 0
#while count < 5:
#    count = count + 1
#    x = float(input('ponha um peso '))
#    if count == 1: #vai usar o primeiro valor como referência
#        ma = x
#        me = x
#    if x > ma:
#        ma = x
#    if x < me:
#        me = x
#print(f'o maior valor foi {ma} e o menor foi {me}')



# === ANALISADOR COMPLETO ===
#count = 0
#sidade = 0
#smulher = 0
#ma = 0
#velho = ''
#while count < 4:
#    count = count +1
#    nome = str(input('digite o nome: '))
#    idade = int(input('digite a idade: '))
#    gen = str(input('digite o genero: '))
#    sidade = idade + sidade
#    if gen == 'mulher':
#        if idade < 20:
#            smulher = smulher + 1
#    if count == 1:
#        if gen == 'homem':
#            ma = idade
#            velho = nome
#        if idade > ma:
#                ma = idade
#                velho = nome
#media = sidade /4
#print(f'a média de idade do grupo vai ser {media}, o homem mais velho é o {velho} e {smulher} mulheres tem menos de 20 anos')



# === VALIDAÇÃO DE DADOS ===
#x = str(input('digite o gênero desejado: (M) ou (F)'))
#while x != 'M' and x !='F':
#    print('digitação incorreta por favor insira novamente (M) ou (F)\n')
#    x = input()
#if x == 'M' or x == 'F':
#    print('Obrigado')



# === JOGO DE ADVINHAÇÃO V2.0 ===
#from random import randint
#num = randint(0, 10)
#x = int(input('tente advinhar o número escolhido pelo pc: '))
#c = 0
#while x != num:
#    c = c + 1
#    print('você errou, tente dnv ')
#    x = int(input())
#    if x == num:
#        print('parabéns vc acertou')
#        break
#print(c)



# === CRIANDO MENU DE OPÇÕES ===
#x = int(input('digite o primeiro valor: '))
#y = int(input('digite o segundo valor: '))
#print('1- somar\n'
#      '2- multiplicar\n'
#      '3-maior\n'
#      '4-novos números\n'
#      '5-sair do programa')
#escolha = int(input('escolha uma operação: '))
#while escolha == 4:
#    x = int(input())
#    y = int(input())
#    escolha= int(input('escolha uma operação: '))
#if escolha == 1:
#    print(x + y)
#if escolha == 2:
#    print(x * y)
#if escolha == 3:
#    if x > y:
#        print(x)
#    else: print(y)
#if escolha == 5:
#    print('FIM')



# === CÁLCULO DE FATORIAL ===
#x = int(input('Digite um número: '))
#c = x
#while c != 2:
#    x = x * (c-1)
#    c = c -1
#print(x)



# === PROGRESSÃO ARITMÉTRICA V2.0 ===
#a1 = int(input('digite o primeiro termo da sua progressão '))
#r = int(input('digite a razão da sua progressão '))
#x = 1
#while x != 11:
#    an = a1 + (x - 1) * r
#    print(an)
#    x = x + 1



# === SUPER PROGRESSÃO ARITMÉTRICA ===
#a1 = int(input('digite o primeiro termo da sua progressão '))
#r = int(input('digite a razão da sua progressão '))
#x = 1
#while x != 11:
#    an = a1 + (x - 1) * r
#    print(an)
#    x = x + 1
#escolha = int(input('Você deseja vÊ mais algum termo? se sim digite o número de termos se não digite 0: '))
#if escolha == 0:
#    print('fim')
#if escolha != 0:
#    x = 11
#    escolha = escolha + 11
#    while x != escolha:
#        an = a1 + (x - 1) * r
#        print(an)
#        x = x + 1



# === sequência de fibonacci v1.0
#n = int(input('digite o número desejado: '))
#c = 0
#y = 1
#x = 0
#z = 1
#while c != n:
#    c = c + 1
#    y = x + z
#    x = z
#    z = y
#    print(y)



# === TRATANDO VÁRIOS VALORES V1.0 ===
#n = (int(input('Digite um número: ')))
#c = 0
#x = 0
#while n != 999:
#    c = c + 1
#    x = x + n
#    n = int(input('digite outro número: para parar o programa tem que ser digitado 999 '))
#print(c)
#print(x - 999)



# === MAIOR E MENOR VALORES ===
#n = 0
#c = 0
#ma = 0
#me = 0
#escolha = 'sim'
#x = 0
#while escolha == 'sim':
#    n = int(input('digite um número: '))
#    if c == 0:
#        ma = n
#        me = n
#    if n > ma:
#        ma = n
#    if n < me:
#            me = n
#    c = c+1
#    x = n + x
#    med = x/c
#    escolha = str(input('quer continuar: '))
#print(f'a média dos números foi {med}, o maior número foi {ma} e  o menor foi {me}')



# === VÁRIOS NÚMEROS COM FLAG ===
#c = 0
#s = 0
#while True:
#    n = int(input('digite númros que serão somados:\npara parar digite 999\n'))
#    if n == 999:
#        break
#    c =+ 1
#    s =+ n
#print(f'{c} foram digitados e a soma é {s}')



# === TABUADA V3.0 ===
#while True:
#    c = 0
#    x = int(input('digite um número para sua tabuada: '))
#    if x < 0:
#        break
#    while c != 11:
#        print(x * c)
#        c = c + 1



# === JOGO PAR OU ÍMPAR ===
#from random import randint
#c = 0
#while True:
#    pc = randint(0, 10)
#    x = int(input('digite um número: '))
#    pi = str(input('você que par ou ímpar? [P/I]'))
#    resultado = 0
#    if pi == 'P' or pi == 'p':
#        resultado = (x + pc) %2
#        if resultado == 0:
#            print('parabêns você ganhou')
#            c = c+1
#        else:
#            print('você perdeu')
#            break
#    if pi == 'I' or pi == 'i':
#        resultado = (x + pc) %2
#        if resultado == 1:
#            print('parabêns você ganhou')
#            c = c+1
#        else:
#            print('você perdeu')
#            break
#print(f'você ganhou {c}')



# === ANÁLISE DE DADOS DO GRUPO ===
#c = 1
#cont = 0
#maioridade = 0
#menor20 = 0
#hm = 0
#while cont != 'não':
#    x = int(input(f'digite a idade da pessoa número {c}'))
#    s = str(input('digite o sexo dela: '))
#    c = c +1
#    if x > 18:
#        maioridade = maioridade + 1
#    if s == 'H':
#        hm = hm + 1
#    if s == 'M' and x < 20:
#        menor20 = menor20 + 1
#    cont = str(input('quer continuar? '))
#print(f'no total {maioridade} pessoas tem mais que 18 anos, {hm} homens foram cadastrados e {menor20} mulheres tem menos de 20 anos')



# === ESTATÍSTICAS EM PRODUTOS ===
#c = 0
#cont = 0
#soma = 0
#me = 0
#barato = 0
#caro = 0
#while cont != 'não':
#    c = c +1
#    nome = str(input(f'digite o nome do produto número {c} '))
#    preco = float(input('digite o preço dele: '))
#    soma = soma + preco
#    if preco >= 1000:
#        caro = caro + 1
#    if c == 1:
#        me = preco
#        barato = nome
#    if preco < me:
#        me = preco
#        barato = nome
#    cont = str(input('quer continuar? '))
#print(f'o total gasto foi de {soma}, {caro} produtos sairam por mais de 1000 reais e {barato} foi o produto mais barato')



# === SIMULADOR DE CAIXA ELETRÔNICO ===
#x = int(input('qual o valor a ser sacado: '))
#while True:
#    n50 = int(x / 50)
#    resto1 = x - (n50*50)
#    n20 = int(resto1 / 20)
#    resto2 = resto1 - (n20 * 20)
#    n10 = int(resto2 / 10)
#    resto3 = resto2 - (n10*10)
#    n1 = resto3
#    break
#print(f'serãp entregues {n50} notas de 50, {n20} notas de 20, {n10} notas de 10 e {n1} notas de 1')



# === NÚMERO POR EXTENSO ===
#extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
#x = int(input('digite o número: '))
#while x < 0 or x > 20:
#    print('número incorreto')
#    x = int(input('digite o número: '))
#print(extenso[x])



# === TUPLAS COM TIME DE FUTEBOL ===
#times = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
#print(times[0:5])
#x = len(times) - 4
#print(times[x:len(times)])



# === MAIOR E MENOR VALORES EM TUPLA ===
#from random import randint
#lista = []
#for c in range(0,5):
#    c = randint(0,10)
#    lista.append(c)
#lista.sort()
#print(lista)
#print(f"o Menor valor da lista é {lista[0]} e o maior é {lista[4]}")



# === ANÁLISE DE DADOS DE UMA TUPLA ===
#tupla = (int(input("insira um número: ")), int(input("insira um número: ")), int(input("insira um número: ")), int(input("insira um número: ")))
#print(tupla)
#print(f"o número 9 apareceu {tupla.count(9)} vezes")
#print(f"{tupla.index(3)} foi a primeira posição onde apareceu o número 3")
#for c in range(len(tupla)):
#    x = tupla[c] %2
#    if x == 0:
#      print(f"{tupla[c]} é par")



# === LISTA DE PREÇOS COM TUPLA ===
#listagem = ('Arroz', 3.50, 'Bacon', 4.00, 'Feijão', 2.00, 'vinho', 16.50)
#for pos in range(0, len(listagem)):
#    if pos % 2 == 0:
#        print(f'{listagem[pos]:.<30}', end='')
#    else:
#        print(f'R${listagem[pos]:>7.2f}')



# === CONTANDO VOGAIS EM TUPLA ===
#palavras = ('teste', 'casa', 'irmao', 'almoço', 'escola')
#for p in palavras:
#    print(f'Na palavra {p} temos ', end='')
#    for letra in p:
#        if letra.lower() in 'aeiou':
#            print(letra, end=' ')



# === MAIOR E MENOR VALORES NA LISTA ===
#lista = []
#ma = 0
#me = 0
#cont = 0
#while cont != 5:
#    x = int(input('Digite o número: '))
#    lista.append(x)
#    if cont == 0:
#        ma = x
#        me = x
#    if ma < x:
#        ma = x
#    if me > x:
#        me = x
#    cont = cont + 1
#print(f'A lista {lista} tem o seu maior valor {ma} na posição {lista.index(ma)} e o seu menor valor {me} na posição {lista.index(me)}')



# === VALORES ÚNICOS EM UMA LISTA ===
#list = []
#while True:
#    x = int(input("digite o número a ser inserido na lista: "))
#    if x not in list:
#        list.append(x)
#    else: print("Esse número ja foi adicionado")
#    escolha = int(input("deseja continuar? (0)Sim (1)Não "))
#    if escolha == 1:
#        list.sort()
#        break
#print(list)



# === LISTA ORDENADA SEM REPETIÇÕES ===
#lista = []
#for c in range (0,5):
#    n = int(input("digite um valor: "))
#    if c == 0 or n > lista[-1]:
#        lista.append(n)
#    else:
#        pos = 0
#        while pos < len(lista):
#            if n <= lista[pos]:
#                lista.insert(pos, n)
#                break
#            pos += 1
#print(lista)



# === EXTRAINDO DADOS DE UMA LISTA ===
#List = []
#count = 0
#while True:
#    x = int(input("Digite um número: "))
#    List.append(x)
#    count = count + 1
#    escolha = int(input("Quer continuar? (0)Sim (1)Não"))
#    if escolha == 1:
#        List.sort(reverse = True)
#        if 5 in List:
#            print("O número 5 está na lista")
#        else: print("O número 5 não está na lista")
#        break
#print(List, count)



# === DIVIDINDO VALORES EM VÁRIAS LISTAS ===
#Lista = []
#listapar =[]
#listaimpar = []
#while True:
#    x = int(input('Digite um número: '))
#    Lista.append(x)
#    if x % 2 == 0:
#        listapar.append(x)
#    else: listaimpar.append(x)
#    escolha = int(input("Quer continuar? (0)Sim (1)Não"))
#    if escolha == 1:
#        break
#print(Lista,"\n", listapar,"\n", listaimpar)



# === VALIDANDO EXPRESÕES MATEMÁTICAS ===
#x = str(input("digite a expressão númerica: "))
#num = x.count('(')
#num2 = x.count(')')
#y = num + num2
#if y % 2 == 0:
#    print('Expressão válida!')
#else: print("Expressão inválida")



# === LISTA COMPOSTA E ANÁLISE DE DADOS ===
#lista = []
#listaTemp = []
#ma = me =0
#
#while True:
#    nome = str(input("Digite um nome "))
#    listaTemp.append(nome)
#    peso = float(input("Digite um peso "))
#    listaTemp.append(peso)
#    if len(lista) == 0:
#        ma = me = listaTemp[1]
#    else:
#        if listaTemp[1] > ma:
#            ma = listaTemp[1]
#        if listaTemp[1] < me:
#            me = listaTemp[1]
#    lista.append(listaTemp[:])
#    listaTemp.clear()
#    escolha = int(input("quer continuar adicionando pessoas? 1-Sim 2-Não "))
#    if escolha == 2:
#        break
#print(f"{len(lista)} pessoas foram cadastradas")
#print(f"{ma} foi o maior peso. Que foi de ", end='')
#for p in lista:
#    if p[1] == ma:
#        print(f'{p[0]}', end=' ')
#print()
#print(f"{me} foi o menor peso. Que foi de ", end='')
#for p in lista:
#    if p[1] == me:
#        print(f'{p[0]}', end=' ')



# === LISTAS COM PARES E ÍMPARES ===
#listaGeral = [[], []]
#for c in range(1,8):
#    x = int(input(f"Digite o {c}o número: "))
#    if x %2 == 0:
#        listaGeral[0].append(x)
#    elif x %2 != 0:
#        listaGeral[1].append(x)
#listaGeral[0].sort()
#listaGeral[1].sort()
#print(listaGeral[0])
#print(listaGeral[1])



# === MATRIZ EM PYTHON ===
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#for l in range(0, 3):
#    for c in range(0, 3):
#        matriz[l][c] = int(input(f"Digita um valor para {l}, {c} "))
#for l in range(0, 3):
#    for c in range(0, 3):
#        print(f"[{matriz[l][c]:^5}]", end='')
#    print()



# === MAIS SOBRE MATRIZ EM PYTHON ===
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#spar = mai = scol = 0
#for l in range(0, 3):
#    for c in range(0, 3):
#        matriz[l][c] = int(input(f"Digita um valor para {l}, {c} "))
#for l in range(0, 3):
#    for c in range(0, 3):
#        print(f"[{matriz[l][c]:^5}]", end='')
#        if matriz[l][c] % 2 ==0:
#            spar += matriz[l][c]
#    print()
#print(f"a soma dos valorea pares é {spar}")
#for l in range(0,3):
#    scol += matriz[l][2]
#print(f"A soma dos valores da terceira coluna é {scol}")
#for c in range(0, 3):
#    if c == 0:
#        ma = matriz[1][c]
#    elif matriz[1][c] > ma:
#        ma = matriz[1][c]
#print(f"o maior valor da segunda linha foi {ma}")



# === PALPITES PARA MEGA SENA ===
#from random import randint
#numJogos = int(input("Quantos jogos serão feitos? "))
#ListaGeral = []
#tot = 1
#while tot <= numJogos:
#    Listax = []
#    cont = 0
#    while True:
#        x =randint(0,61)
#        if x not in Listax:
#            Listax.append(x)
#            cont += 1
#        if cont >= 6:
#            break
#    Listax.sort()
#    ListaGeral.append(Listax)
#    tot += 1
#print(ListaGeral)



# === BOLETIM COM NOTAS COMPOSTAS ===
#listaTemp = []
#lista = []
#escolha = 1
#while escolha == 1:
#    listaTemp.append(str(input("Digite o nome do aluno: ")))
#    listaTemp.append(int(input("Digite a primeira nota: ")))
#    listaTemp.append(int(input("Digite a segunda nota: ")))
#    lista.append(listaTemp[:])
#    listaTemp.clear()
#    escolha = int(input("Quer continuar adicionando? 1-sim 2-não "))
#print('-=' * 30)
#for x in lista:
#    media = (x[1] + x[2]) /2
#    x.append(media)
#count = 0
#for x in lista:
#    count = count + 1
#    print(f"O aluno {x[0]} número {count} teve a média {x[3]}")
#    x.append(count)
#print('-=' * 30)
#escolha = int(input("deseja vê as notas de algum aluno: "))
#for x in lista:
#    if escolha in x :
#        print(f"aluno: {x[0]}\n"
#              f"nota 1 {x[1]}\n"
#              f"nota 2 {x[2]}\n"
#              f"média {x[3]}")



# === DICIONÁRIO EM PYTHON ===
#dicionario = {}
#dicionario['nome'] = str(input("o nome do aluno: "))
#dicionario['media'] = float(input("média do aluno: "))
#if dicionario['media'] <= 6.9:
#    dicionario['situacao'] = "Reprovado"
#else: dicionario['situacao'] = "Aprovado"
#from time import sleep

#print(f"o {dicionario['nome']} está {dicionario['situacao']}")



# === JOGO DE DADOS EM PYTHON ===
#from random import randint
#from operator import itemgetter
#from time import sleep

#resultados = {'Jogador1': randint(1,6),
#              'Jogador2': randint(1,6),
#              'Jogador3': randint(1,6),
#              'Jogador4': randint(1,6)}
#ranking = list()
#print('Valores sorteados:')
#for k, v in resultados.items():
#    print(f'{k} tirou {v} no dado')
#    sleep(1)
#ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
#for i, v in enumerate(ranking):
#    print(f'{i+1}º lugar: {v[0]} com {v[1]}')



# === CADASTRO DE TRABALHADOR EM PYTHON ===
#cadastro = dict()
#cadastro['nome'] = str(input("Digite o seu nome: "))
#anoNascimento = int(input("Digite o seu ano de nascimento: "))
#cadastro['ano de nascimento'] = anoNascimento
#idade =2021 - anoNascimento
#cadastro['idade'] = idade
#ctps = int(input("Digite o número da sua carteira de trabalho: "))
#cadastro['CTPS'] = ctps
#if (ctps != 0):
#    cadastro['ano de contratação'] = int(input("Digite o ano da sua contratação: "))
#    cadastro['salario'] = float(input("Digite o seu salário: "))
#    cadastro['anos para se aposentar'] = cadastro['idade'] + ((cadastro['ano de contratação'] + 35) - 2021)
#print(cadastro)



# === CADASTRO DE JOGADOR DE FUTEBOL ===
'''cadastro = dict()
cadastro['nome'] = str(input("Digite o nome do jogador: "))
qntPartidas = int(input("Digite o número de partidas durante o campeonato: "))
totalGols = 0
for x in range(0, qntPartidas):
    qntGols = int(input(f"Quantos gols ele fez na partida{x+1}: "))
    totalGols = totalGols + qntGols
cadastro['Número de partidas jogadas'] = qntPartidas
cadastro['Total de gols'] = totalGols
print(cadastro)'''