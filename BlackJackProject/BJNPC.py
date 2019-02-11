#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 08:23:46 2018

@author: Stian
"""
import random


def npc(npcNames): #Liste med spiller npc navn sendes inn, ment på for testing  
    amountOfPlayers=len(npcNames)#mengden spillere blir satt lik amountOfPlayers
    playerscoresList=[]#oppretter liste som skall holde poengscoren 
    for i in range(0,amountOfPlayers):#for-løke som kjøre en gang for hver spiller 
        state=0#state blir satt som null for å la while kjøre x-antall ganger
        playerScore=0#spiller score
        while state != 0:
#            playerScore=playerScore+drawCard(npcNames[i])#trekker kort for spiller-x
            chanche =random.randint(0,100)#et tilfeldig number mellom 0 og 100 blir trekkt og blir satt lik chanche
            if playerScore <= 10:#if test som tester om scoren er mindre en 10
                if chanche <= 5:#teser om chanche er mindre en 5. 5% sjansje for det
                    state=1#state blir satt 1 og while løkken hopper ut
            if playerScore > 10 and playerScore <= 15:
                if chanche <= 18:#teser om chanche er mindre en 18. 18% sjansje for det
                    state=1
            if playerScore > 15 and playerScore <= 18:
                if chanche <= 23:#teser om chanche er mindre en 23. 23% sjansje for det
                    state=1
            if playerScore > 18 and playerscore < 19:
                if chanche <=43:#teser om chanche er mindre en 43. 43% sjansje for det
                    state=1
            if playerScore == 20:
                if chanche <= 95:#teser om chanche er mindre en 95. 95% sjansje for det
                    state=1
        
        playerscoresList.append(playerScore)
        print(playerscoresList)


ConstructCommand= "c" + 'c' +  "Dict[""'" + 'c' + str('9') + "'""]"
#cardName=eval(ConstructCommand)
            
print(  ' ' + str(ConstructCommand))