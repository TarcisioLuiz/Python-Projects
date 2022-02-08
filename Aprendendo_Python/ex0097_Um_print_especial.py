def escreva(mensagem):
    print('~' * (len(mensagem) + 4))
    print("  " + mensagem + "  ")
    print('~' * (len(mensagem) + 4))


mensagem = str(input('escreva a mensagem para ser editada '))
escreva(mensagem)