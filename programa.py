def define_posicoes(linha, coluna, orientacao, tamanho):
    nlista=[]
    i=0
    while i<tamanho:

        if orientacao=='vertical':
            
                nlista.append([linha, coluna])
                linha=linha+1
        else:
            
                nlista.append([linha, coluna])
                coluna=coluna+1
        i=i+1
    return nlista
def preenche_frota(frotadic, nome, linha, coluna, orientacao, tamanho):
     
    resultado = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frotadic:
        frotadic[nome] = []
    frotadic[nome].append(resultado)
    return frotadic
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    coordenadas = define_posicoes(linha, coluna, orientacao, tamanho)
    for i, j in coordenadas:
        if i > 9 or i < 0 or j > 9 or j < 0:
            return False
    for lista_posicao in frota.values():
        for itens in lista_posicao:
            for localizacoes in itens:
                if localizacoes in coordenadas:
                    return False
    return True
def posiciona_frota(dicnav):
    ntab=[]
    for i in range(10):
         linha=[]
         for j in range(10):
                linha.append(0)
         ntab.append(linha)


    for nome, navios in dicnav.items():
         for navio in navios:
                for posicao in navio:
                    linha= posicao[0]
                    coluna= posicao[1]
                    ntab[linha][coluna]=1


    return ntab
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
def faz_jogada (tabuleiro, linha, coluna):
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
        
    else:
        tabuleiro[linha][coluna] = '-'
    

        
    return tabuleiro
def afundados (dicnav, tabuleiro):
    afundados=0
    for nome, navios in dicnav.items():
        for navio in navios:
            afundado=True
            for posicao in navio:
                linha= posicao[0]
                coluna= posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado=False
                    break
            if afundado:
                afundados+=1
    return afundados
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
            print('Esta posição não está válida!')
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
            print('Linha inválida!')
            i = 0
        else:
            i += 1
    j = 0
    while j < 1:
        colunajogo = int(input())
        if colunajogo > 9 or colunajogo < 0:
            print('Coluna inválida!')
            j = 0
        else: j += 1
    if [linhajogo, colunajogo] in jogadas:
        print(f'A posição linha {linhajogo} e coluna {colunajogo} já foi informada anteriormente!')
        pessoa = 'jogando'
    else:
        taboponente = faz_jogada(taboponente, linhajogo, colunajogo)
        verificacao = afundados(frota_oponente, taboponente)
        pessoa = 'jogando'
        tabuleiro = monta_tabuleiros(tabjogador, taboponente)
        jogadas.append([linhajogo, colunajogo])
    if verificacao == 10:
        pessoa = 'ganhou'
        tabuleiro = monta_tabuleiros(tabjogador, taboponente)
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
# print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')