def ficha(nome='', gols=0):
    print('FICHA DO JOGADOR:')
    print(f'NOME: {nome}')
    print(f'GOLS: {gols}')


nome = str(input('Digite o nome do jogador: '))
gols = int(input('Digite o número de gols feitos: '))
ficha(nome, gols)
