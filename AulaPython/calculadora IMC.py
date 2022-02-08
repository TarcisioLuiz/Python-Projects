import math

def retornar_resultadoIMC(IMC):
   resultadoIMC = ''
   if IMC < 18.5:
       resultadoIMC ='magreza'
   elif IMC > 18.5 and IMC <24.9:
      resultadoIMC ='normal'
   elif IMC > 24.9 and IMC < 30.0:
      resultadoIMC ='sobrepeso'
   elif IMC > 30.0:
      resultadoIMC ='obesidade'
   else:
      resultadoIMC = 'erro no calculo'
   return resultadoIMC


resultados = {}
for x in range(0,1):
   nome = str(input('escreva o seu nome: '))
   peso = float(input('escreva o peso: '))
   altura = float(input('escreva a altura: '))
   IMC = (peso/altura**2)


   resultados [nome] =str(IMC) + ' = ' + retornar_resultadoIMC(IMC)
print('o resultado foi: {:.2f}'.format(resultados))



