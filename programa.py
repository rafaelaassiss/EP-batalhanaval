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
naviosfrota = [('porta-aviões', 4, 1), ('navio-tanque', 3, 2), ('contratorpedeiro', 2, 3), ('submarino', 1, 4)]
for nome, tamanho, naviostot in naviosfrota:
    i = 0
    while i < naviostot:
        linha = int(input())
        coluna = int(input())
        if tamanho > 1:
            ori = int(input())
            if ori == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        else:
            orientacao = 'vertical'

        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            pass
        else:
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i += 1
taboponente = posiciona_frota(frota_oponente)
tabjogador = posiciona_frota(frota)
tabuleiro = monta_tabuleiros(tabjogador, taboponente)
pessoa = 'jogando'
jogadas = []
while pessoa == 'jogando':
    i = 0
    while i < 1:
        linhajogo = int(input())
        if linhajogo > 9 or linhajogo < 0:
            i = 0
        else:
            i += 1
    j = 0
    while j < 1:
        colunajogo = int(input())
        if colunajogo > 9 or colunajogo < 0:
            j = 0
        else: j += 1
    if [linhajogo, colunajogo] in jogadas:
        pessoa = 'jogando'
    else:
        taboponente = faz_jogada(taboponente, linhajogo, colunajogo)
        verificacao = afundados(frota_oponente, taboponente)
        pessoa = 'jogando'
        tabuleiro = monta_tabuleiros(tabjogador, taboponente)
        jogadas.append([linhajogo, colunajogo])
    if verificacao == 10:
        pessoa = 'ganhou'
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
# print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')