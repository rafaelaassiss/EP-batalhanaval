frota = {'porta-aviões' : [], 'navio-tanque' : [], 'contratorpedeiro' : [], 'submarino' : []}

i = 0
while i < 1:
    print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
    linha = int(input('Quantas linhas?'))
    coluna = int(input('Quantas colunas?'))
    ori = int(input('Qual a orientação?'))
    if ori == 1:
        orientacao = 'vertical'
    else:
        orientacao = 'horizontal'
    tamanho = 4
    navio = posicao_valida(frota, linha, coluna, orientacao, tamanho)
    if navio == False:
         print('Esta posição não está válida!')
    else:
        posicao = define_posicoes(linha, coluna, orientacao, tamanho)
        preenchimento = preenche_frota(frota, 'porta-aviões', linha, coluna, orientacao, tamanho)
        i += 1

j = 0
while j < 2:
    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    linha = int(input('Quantas linhas?'))
    coluna = int(input('Quantas colunas?'))
    ori = int(input('Qual a orientação?'))
    if ori == 1:
        orientacao = 'vertical'
    else:
        orientacao = 'horizontal'
    tamanho = 3
    navio = posicao_valida(frota, linha, coluna, orientacao, tamanho)
    if navio == False:
         print('Esta posição não está válida!')
    else:
        posicao = define_posicoes(linha, coluna, orientacao, tamanho)
        preenchimento = preenche_frota(frota, 'navio-tanque', linha, coluna, orientacao, tamanho)
        j += 1

k = 0
while k < 3:
    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    linha = int(input('Quantas linhas?'))
    coluna = int(input('Quantas colunas?'))
    ori = int(input('Qual a orientação?'))
    if ori == 1:
        orientacao = 'vertical'
    else:
        orientacao = 'horizontal'
    tamanho = 2
    navio = posicao_valida(frota, linha, coluna, orientacao, tamanho)
    if navio == False:
         print('Esta posição não está válida!')
    else:
        posicao = define_posicoes(linha, coluna, orientacao, tamanho)
        preenchimento = preenche_frota(frota, 'contratorpedeiro', linha, coluna, orientacao, tamanho)
        k += 1

l = 0
while l < 4:
    print('Insira as informações referentes ao navio submarino que possui tamanho 1')
    linha = int(input('Quantas linhas?'))
    coluna = int(input('Quantas colunas?'))
    tamanho = 1
    orientacao = 'vertical'
    navio = posicao_valida(frota, linha, coluna, orientacao, tamanho)
    if navio == False:
         print('Esta posição não está válida!')
    else:
        posicao = define_posicoes(linha, coluna, orientacao, tamanho)
        preenchimento = preenche_frota(frota, 'submarino', linha, coluna, orientacao, tamanho)
        l += 1