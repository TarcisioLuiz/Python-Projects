# produtos = {'chave':'valor', 'dipirona':100}
# novoproduto = input('digite o produto: ')
# for x in produtos.values():
#    if x == novoproduto:
#        print('produto ja cadastrado')

alunos = {'Tarcisio':'Hivecloud', 'Matheus':'Cadan', 'Guilherme':'Nazaria','Pedro':'Senior'}
novoaluno = input('digite o aluno: ')
a = 0
for x in alunos.keys():
        if x == novoaluno:
            a = 1
if a != 1:
    alunos[novoaluno] = input('digite a empresa: ')
    print(alunos)
else:
    print('aluno ja cadastrado')

