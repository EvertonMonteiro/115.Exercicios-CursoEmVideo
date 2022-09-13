def notas(*n, sit=False):
    '''
    :param n: Notas do Aluno
    :param sit: valor opcional que mostra a situação da média do aluno
    :return: dicionário com informações das notas do aluno.
    '''
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] = sum(n)/len(n)
    if sit:
        if boletim['media'] > 7:
            boletim['situação:'] = 'BOA'
        if boletim['media'] >= 5:
            boletim['situação:'] = 'RAZOAVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim
resp = notas(9, 9, 10, sit=True)
print(resp)
