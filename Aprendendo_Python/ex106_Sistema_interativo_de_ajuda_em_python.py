def ajuda(funcao):
    help(funcao)


while True:
    funcao = str(input('Digite a função python: (digite fim para encerrar) '))
    if funcao.upper() == "FIM":
        break
    else:
        ajuda(funcao)