import random
def inicializa(lista_palavras):
    n=len(lista_palavras[0])
    sorteada=random.choice(lista_palavras)
    especuladas=[]
    tentativas=n+1
    dic={}
    dic['n']=n
    dic['sorteada']=sorteada
    dic['especuladas']=especuladas
    dic['tentativas']=tentativas

    return dic