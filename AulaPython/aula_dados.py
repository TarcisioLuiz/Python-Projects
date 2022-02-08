dados= {}
dados['nome'] = str(input('qual o seu nome? \n'))
dados['idade'] = int(input('qual a sua idade? \n'))
dados['empresa'] = str(input('qual a sua empresa? \n'))
print(dados)
mudar = str(input('deseja alterar algo? '))
if mudar== 'sim':
    dados['nome'] = str(input('qual o seu nome? \n'))
    dados['idade'] = int(input('qual a sua idade? \n'))
    dados['empresa'] = str(input('qual a sua empresa? \n'))
else:
    print(dados,'\n cadastro finalizado')
print(dados,'\n cadastro finalizado')