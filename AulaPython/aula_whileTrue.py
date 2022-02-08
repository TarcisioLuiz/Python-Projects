login = input('login: ')
login1 =input('por favor confirme seu login: ')
while True:
    if login != login1:
        login1 = input("as informações são diferentes, por favor insira novamente seu login: ")
    else:
        break
print('cadastro concluido com sucesso')