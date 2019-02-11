#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:41:17 2018

@author: Adam
"""

import math
import random

playerCount = 0
dealerCount = 0
dcn = 0 #dealer card number
pcn = 0 #player card number
cDict = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Fivee",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King",14:"Ace"}

def start():
    print("Welcom to black jack")
    print("Dealer: Let me draw a card, and see what i get")
    dealer()
#######PLAYER
def player(yorn):
    print('\n')
    global playerCount
    #yes
    if yorn.lower() == "yes":
        counter = drawCard("player")
        if counter == 21:
            print("Black Jack motherfucker!")
        elif counter > 21:
            print("You lost, fuck you")
        elif counter < 21:
            answer = input('Do you want to draw another card, yes or no?: ')
            player(answer)
        else:
            print("Good job... you broke my game, ERROR! - player count weird")
    #no
    elif yorn.lower() == "no":
        print("good choice!, now let me handle this")
        dealer()
    #error
    else:
        print("Good job... you broke my game, ERROR! - did not answer correctly YORN")

#####DEALER
def dealer():
    print('\nDEALER: time for me to draw a card \n')
    global dealerCount
    global playerCount
    global dcn
    global answer
    if dcn == 0:
        dcn = dcn + 1
        drawCard("dealer")
        answer = input('Do you want to draw a card, yes or no?: ')
        player(answer)
   # elif dcn == 1 & pcn == 0
    else:
        drawCard("Dealer")
        if dealerCount == 21:
                print("Black Jack motherfucker! Get out of here!")
                
        elif (dealerCount > playerCount) & (dealerCount <= 21):
                print("You lost, That's right, i Win!")
        elif (dealerCount > playerCount) & (dealerCount > 21):        
                print("Get out, you win!")
                
        elif (dealerCount <= playerCount) & (21 >= dealerCount):# & (answer.lower() == "no"):
                print('Dealer draws another card')
                dealer()
        #elif (playerCount > dealerCount) & player 
        else:
                print("Good job... you broke my game, ERROR! - player count weird")
                print("dealerCount %d : playerCount %s" % (dealerCount, playerCount))
                print("asnwer is: %s" % (answer))
                
def cardGui(cn):
    if cn >= 10:
        monkey = str(cDict[cn])[0]
        print('|-----|')
        print('|  '+' '+'  |')
        print('|  '+str(monkey)+'  |')
        print('|  '+' '+'  |')
        print('|-----|')
    else:
        print('|-----|')
        print('|  '+' '+'  |')
        print('|  '+str(cn)+'  |')
        print('|  '+' '+'  |')
        print('|-----|')
        
        
    
def drawCard(user):
    global dealerCount
    global playerCount
    plyr = str(user)
    card = random.randint(1,14)
    cardName = cDict[card]
    print('%s drew a card and its a %s! ' % ((plyr), (cardName)))
    if plyr.lower() == "dealer":      
        dealerCount = dealerCount + card 
        print('total score for dealer is %d ' % (dealerCount))
        cardGui(card)
        return dealerCount
    elif plyr.lower() == "player":
        playerCount = playerCount + card
        print('total score for player is %d ' % (playerCount))
        cardGui(card)
        return playerCount
    cardGui(card)
    return card

def reset():
    global dealerCount
    global playerCount
    global dcn
    
    playerCount = 0
    dealerCount = 0
    dcn = 0
    start()

start()