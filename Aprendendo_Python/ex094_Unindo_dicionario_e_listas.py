#lista = []
#count = 0
#totIdade = 0
#cadastro = dict()
#while (True) :
#    count= count + 1
#    cadastro.clear()
#    nome = str(input("Digite o nome: "))
#    sexo = str(input("Digite o genêro: "))
#    idade = int(input("Digite a idade: "))
#    totIdade = totIdade + idade
#    cadastro['nome'] = nome
#    cadastro['sexo'] = sexo
#    cadastro['idade'] = idade
#    lista.append(cadastro.copy())
#    escolha = int(input("Quer continuar adicionando pessoas? 1-sim\n2-não"))
#    if (escolha == 2):
#        break
#    else: continue
#print(lista)
#print(f"{count} foram cadastradas")
#print(f"A média de idade do grupo é {totIdade/count}")
#for x in lista:
#    if x['sexo'] == 'F':
#        print(f'{x["nome"]} ')
#for p in lista:
#    if p['idade'] >= totIdade/count:
#        print('   ')
#        for k, v in p.items():
#            print(f'{k} = {v}')
#        print()