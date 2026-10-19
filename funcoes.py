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




