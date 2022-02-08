def notas(*n, sit):
    turma = dict()
    turma['Quantidade de notas'] = len(n)
    turma['Maior nota'] = max(n)
    turma['Menor nota'] = min(n)
    turma['Média da turma'] = sum(n)/len(n)
    if sit == True:
        if sum(n)/len(n) <= 5:
            situacaoTurma = "RUIM"
        if sum(n)/len(n) < 7:
            situacaoTurma = "RAZOÁVEL"
        if sum(n)/len(n) >= 7:
            situacaoTurma = "BOM"
    else: situacaoTurma = "Indisponivel"
    turma['Situação'] = situacaoTurma
    return turma


print(notas(6, 3, 6, 9, 10, 4, 9, 8, sit=True))