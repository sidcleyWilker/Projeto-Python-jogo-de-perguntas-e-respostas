# -*- coding: UTF-8 -*-
from logicaPY import alternativas,pergunta,ranck,verificaResposta,ordenaRanking
from perguntas import procuraPergunta
import time

def imprimeRanking():
    print ""
    for i in range(len(ordenaRanking())-1,-1,-1):
        print ordenaRanking()[i]
    print ""
def cadastraUsuario():
    '''função que recebe do usuário seu apelhidio ou nome,
    verifica se o mesmo não ultrapassa de 20 caracteres 
    e devolve o mesmo que recebel caso o número seja menor do que 20 
    '''
    nome = raw_input("Nick ou Nome do usuário: ")
    while (len(nome) > 20) or (nome == ""):
        print "Nick ou Nome do usuário Invalido"
        nome = raw_input("Nick ou Nome do usuário: ")
    return nome
  
def usuario():
    '''função onde o usuário Informa seu (nick ou nome) e em seguida escolhe o nivel em que deseja jogar 
    ou ver o ranking
    '''
    print "PARA INICIAR O JOGO DIGITE SEU NOME E EM SEGUIDA ESCOLHA UM NÚMERO DE ACORDO COM O MENU"
    print " "*20,("="*26)
    print " "*20,("|       MENU DO JOGO     |")
    print " "*20,("="*26);
    print " "*20,("|   1 - NIVEL FACIL      |")
    print " "*20,("|   2 - NIVEL MEDIO      |")
    print " "*20,("|   3 - NIVEL DIFICIL    |")
    print " "*20,("|   4 - VER RANKING      |")
    print " "*20,("="*26)
    
    nome = cadastraUsuario()
    print ""
    for i in nome:
        time.sleep(0.50)
        print i,
    print "  >>>>> Seja Bem vindo ou Responda Se Pode <<<<<","\n"
    
    
    n = raw_input ("Imforme um numero de acordo com o menu: ")
    while (n != "1") and (n != "2") and (n != "3") and (n != "4"):
        print "Imforme um número de acordo com o nivel do jogo"
        n = raw_input ("Imforme um numero de acordo com o menu: ")
    n = int(n)
    
    escolhe(n,nome)
            
def escolhe(escolheNivel,nome):
    '''função que passa como paremetro o nivel que o usuário escolheu junto com seu nome ou nick
    '''
    if escolheNivel == 1:
        loop(procuraPergunta('Perguntas/perguntasFaceis.txt'),nome)
    elif escolheNivel == 2:
        loop(procuraPergunta('Perguntas/perguntasMedias.txt'),nome)
    elif escolheNivel == 3:
        loop(procuraPergunta('Perguntas/perguntasDificeis.txt'),nome)
    elif escolheNivel == 4:
        imprimeRanking()      
        
def continuar():
    '''função que verifica se o usuário deseja jogar o jogo novamente
    '''
    continuar = raw_input("Jogar Novamente s/n ? ")
    while continuar == ("s" or "S"):
        usuario()
        continuar = raw_input("Jogar Novamente s/n ? ")

def imprimeAlternativas(alternativasEmba):
    '''função que imprime as alternativas embaralhadas e as letras
    '''
    letras = ["a)","b)","c)"]
    for i in alternativasEmba:
        print letras[0], i
        letras.remove(letras[0])

def loop(nivel,nome):
    '''função principal onde imprime a pergunta as respostas, e verifica se a resposta esta certa ou errada.
    passando como parametro o nome do usuário e a sua pontuacão para o ranking 
    '''
    x,pontos, = 1,0
    while len(nivel) > 0 :
        print ""
        print str(x)+":)",pergunta(nivel)
        
        alternativasEmba = alternativas(nivel)
        imprimeAlternativas(alternativasEmba)
               
        n = raw_input("qual é a resposta:? ")
        
        while n != "a" and n!= "b" and n != "c":
            print "letra invalida"
            n = raw_input("qual é a resposta:? ")
        
        if verificaResposta(nivel,alternativasEmba,n):
            print "----->  certa resposta  <-----"
            pontos += 50
        else:
            print "----->  resposta errda  <-----"
            pontos -= 15
            
        nivel.remove(nivel[0])
        x += 1
    
    print ""
    print nome,"Sua pontuacao foi de",pontos,"pontos"
    pontos2 = str(pontos)
    ranck(nome,pontos2)
     
usuario()
continuar()