# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 18:56:10 2018

@author: james
"""


import pygame,numpy,scipy,pylab,random,time,threading,tkinter
from PyDictionary import PyDictionary

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)

global deck,suits
deck = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'],['A','2','3','4','5','6','7','8','9','10','J','Q','K'],['A','2','3','4','5','6','7','8','9','10','J','Q','K'],['A','2','3','4','5','6','7','8','9','10','J','Q','K']]
suits = ['♠','♥','♦','♣']
def deal(playerCount):
    dealt = []
    for i in range(numberOfCards[playerCount-1]):
        if len(suits) != 1:
            suit = random.randint(0,len(suits)-1)
        else:
            suit = 0
        if len(deck[suit]) != 1:
            card = random.randint(0,len(deck[suit])-1)
        else:
            card = 0
        dealt.append([suits[suit],deck[suit][card]])
        del deck[suit][card]
        if len(deck[suit]) == 0:
            del suits[suit]
            del deck[suit]
    return dealt
        
class playerCards:
    playerCount = 0
    def __init__(self,player,deck,suits):
        playerCards.playerCount += 1
        self.player = player
        if playerCards.playerCount != numPlay:
            self.hand = deal(playerCards.playerCount)
        else:
            dealt = []
            for i in range(len(suits)):
                for j in range(len(deck[i])):
                    dealt.append([suits[i],deck[i][j]])
            self.hand = dealt
            deck = []
            suits = []
            
numPlay = int(input("Number of players: ")) 
global numberOfCards
numberOfCards = [int(52/numPlay) for x in range(numPlay)]
for l in range(52%numPlay):
    numberOfCards[l] = numberOfCards[l]+1   
for i in range(1,numPlay+1):
    locals()["player"+str(i)] = playerCards(input("What is the name of player "+str(i)+": "),deck,suits)
for j in range(1,numPlay+1):
    print(locals()['player'+str(j)].player+"'s hand:"+"\n",locals()['player'+str(j)].hand)
    