from funcoes import *
frota = {'porta-aviões' : [], 'navio-tanque' : [], 'contratorpedeiro' : [], 'submarino' : []}
frota_oponente = {
     'porta-aviões': [
         [[9, 1], [9, 2], [9, 3], [9, 4]]
     ],
     'navio-tanque': [
         [[6, 0], [6, 1], [6, 2]],
         [[4, 3], [5, 3], [6, 3]]
     ],
     'contratorpedeiro': [
         [[1, 6], [1, 7]],
         [[0, 5], [1, 5]],
         [[3, 6], [3, 7]]
     ],
     'submarino': [
         [[2, 7]],
         [[0, 6]],
         [[9, 7]],
         [[7, 6]]
     ]
}
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

taboponente = posiciona_frota(frota_oponente)
tabjogador = posiciona_frota(frota)

jogando = True
jogadas = []
print(monta_tabuleiros(tabjogador, taboponente))

while jogando:
    
    linhajogo = int(input('Em qual linha você deseja atacar?'))
    while linhajogo > 9 or linhajogo < 0:
        print('Linha inválida!')
        linhajogo = int(input('Em qual linha você deseja atacar?'))
        
    colunajogo = int(input('Em qual coluna você deseja atacar?'))
    while colunajogo > 9 or colunajogo < 0:
        print('Coluna inválida!')
        colunajogo = int(input('Em qual coluna você deseja atacar?'))

    if [linhajogo, colunajogo] in jogadas:
        print(f'A posição linha {linhajogo} e coluna {colunajogo} já foi informada anteriormente!')
    else:
        jogadas.append([linhajogo, colunajogo])
        taboponente = faz_jogada(taboponente, linhajogo, colunajogo)
        
        if afundados(frota_oponente, taboponente) == 10:
            jogando = False
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
        else:
            print(monta_tabuleiros(tabjogador, taboponente))