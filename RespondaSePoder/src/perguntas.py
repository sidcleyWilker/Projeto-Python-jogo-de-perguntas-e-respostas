import random

def procuraPergunta(local):
    listaTotal = [] # lista onde vai ser guardado todas as listas com a perguntas e as respostas
    arq = open(local,'r')
    continua = True
    
    while continua:
        linha = arq.readline()
        if not linha:
            continua = False
        else:        
            transformaLinhaEmLista = linha.split("-") #transforma a linha do arquivo em uma lista com 2 elentos a pergunta e as respostas
            listaDeResposta = transformaLinhaEmLista[1].split(",")# cria uma lista com 3 elementos que sao as resposta 
            
            ultimoElementoDaLista = listaDeResposta[2]# pega o ultimo elemento da lista de resposta 
            tiraOqueNaoEresposta = ultimoElementoDaLista[0:ultimoElementoDaLista.find("\n")]# remove os caracteres \n que estavao no final do ultimo elemento da lista de resposta
         
            listaDeResposta[2] = tiraOqueNaoEresposta #subistitue o ultimo elemento da lista de resposta pelo elemento que nao contem os caracteres \n
            transformaLinhaEmLista[1] = listaDeResposta #subistitue a lista de resposta que contia os caracteres \n no ultimo elemento por uma que nao tem mais 
             
            listaTotal.append(transformaLinhaEmLista)# adiciona a lista com a pergunta e as alternativas a uma outra lista que vai conter todas as perguntas ou final do loop
    arq.close()
    random.shuffle(listaTotal)   
    return listaTotal