def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if (idade < 16):
        return 'Não vota'
    elif (idade >= 16 and idade < 18 and idade >= 65):
        return 'opcional'
    elif (idade >= 18):
        return 'obrigatorio'

ano = int(input('Digite o ano de seu nascimento '))
print(voto(ano))