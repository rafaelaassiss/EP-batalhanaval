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

def faz_jogada (tabuleiro, linha, coluna):
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
        
    else:
        tabuleiro[linha][coluna] = '-'
    

        
    return tabuleiro

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto