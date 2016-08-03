# -*- coding: UTF-8 -*-
import random 

def alternativas (lista):
    '''função que recebe como parametro uma função de acordo com o nivel
    pega apenas as alternativas do primeiro elemento, adiciona em outra lista 
    e as retorna embaralhadas
    '''
    listaAux = []
    listaAux.append(lista[0][1][0])
    listaAux.append(lista[0][1][1])
    listaAux.append(lista[0][1][2])
    random.shuffle(listaAux)
    return listaAux

def pergunta(nivel):
    '''função que recebe como parametro uma função de acordo com o nivel passado
    e retorna apenas o elemento [0][0] que é a pergunta 
    '''
    return nivel[0][0]


def verificaResposta(respostaLista,prgEmbaralhada,resposta):
    
    alternativasLista = ["a","b","c"]
    respostaElemCorreto = respostaLista[0][1][0]
    
    posicaoCorreta = prgEmbaralhada.index(respostaElemCorreto)
    posicaoDeEntradaUsu = alternativasLista.index(resposta)
   
    if (posicaoCorreta == posicaoDeEntradaUsu):
        return True
    return False
    

def ranck(nome,pontuacao):
    arquivo = open('Ranking/arquivo.txt','r')
    outraLinha = arquivo.readlines()
    outraLinha.append(nome)
    outraLinha.append(" -> ")
    outraLinha.append(pontuacao)
    outraLinha.append("\n")
    arquivo.close()
    
    arquivo = open('Ranking/arquivo.txt','w')
    arquivo.writelines(outraLinha)
    arquivo.close()
    
def ordenaRanking():  
    arq = open('Ranking/arquivo.txt','r')
    ranking = []
    while True:
        linha = arq.readline()
        if not linha:
            break
        transformaLinhaEmLista = linha.split(" -> ")
        ultimoElementoDaLista = transformaLinhaEmLista[1]
        tiraOqueNaoEresposta = ultimoElementoDaLista[0:ultimoElementoDaLista.find("\n")]
        tranformaEmInteiro = int(tiraOqueNaoEresposta)
        transformaLinhaEmLista[1] = tranformaEmInteiro
        
        ranking.append(transformaLinhaEmLista)
      
  
    for i in range(len(ranking)):
        for x in range(len(ranking)):
            if ranking[x][1] > ranking[i][1]:
                ranking[i],ranking[x] = ranking[x],ranking[i]
              
    return ranking