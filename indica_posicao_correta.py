def indica_posicao(sorteada, chute):
    saida = []
    if len(sorteada) != len(chute):
        return []
    for i in range(len(chute)):
        letra_c = chute[i]
        letra_s = sorteada[i]
        if letra_c in sorteada:
            if letra_c == letra_s:
                saida.append(0)
            else:
                saida.append(1)
        else:
            saida.append(2)
    return saida