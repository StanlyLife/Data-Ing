# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:14:42 2018

@author: Hans
"""
import random
global key

def madafakka():
    import os
    os.system('afplay assets/bj.wav&')
       

playerCount = 0 #variable for players score 
dealerCount = 0 #variable for computers score
dcn = 0 #dealer card number
pcn = 0 #player card number
#dictornary for cards 
cHDict = {"H0":"Zero", "H1" :"one", "H2":"two", "H3":"Three","H4":"Four","H5":"Five","H6":"Six","H7":"Seven","H8":"Eight","H9":"Nine","H10":"Ten","H11":"Jack","H12":"Queen","H13":"King","H14":"Ace"}
cSDict = {"S0":"Zero", "S1" :"one", "S2":"two", "S3":"Three","S4":"Four","S5":"Five","S6":"Six","S7":"Seven","S8":"Eight","S9":"Nine","S10":"Ten","S11":"Jack","S12":"Queen","S13":"King","S14":"Ace"}
cDDict = {"D0":"Zero", "D1" :"one", "D2":"two", "D3":"Three","D4":"Four","D5":"Five","D6":"Six","D7":"Seven","D8":"Eight","D9":"Nine","D10":"Ten","D11":"Jack","D12":"Queen","D13":"King","D14":"Ace"}
cCDict = {"C0":"Zero", "C1" :"one", "C2":"two", "C3":"Three","C4":"Four","C5":"Five","C6":"Six","C7":"Seven","C8":"Eight","C9":"Nine","C10":"Ten","C11":"Jack","C12":"Queen","C13":"King","C14":"Ace"}
#function which runs at the start at the program




def start():
    print("start() running, going into drawCard()")
    drawCard('dealer')
#helper for cardValue when cards value is > 10
def valueOfcard(cardName, scoreCount): ##
    if str(cardName) == "Ace":
        print('Found ACE')
        if (scoreCount + 11) > 21:
            print('returning: 1 for Ace')
            return 1
        else:
            print('returning: 11 for Ace')
            return 11
#    elif
    else:
        print('didnt find ace, returning 10')
        return 10
#returns the amount of points for each card
def cardValue(scoreCount, key):
    key2 = key.upper()
    print('STARTING CARDVALUE() with key: %s' %(key2))
    card_value = key2[:0] + key2[1:]
    card_value = int(card_value) 
    dict_value = key[0].upper()
    getDict=str(key2[0])
    newKey = getDict + str(card_value)
    find_cardName_command="c" + str(dict_value.upper()).upper() + "Dict[" + "'" + str(newKey) + "'" + "]"
    cardName=eval(find_cardName_command)
    print("CARDVALUE: %s, cardname: %s" %(card_value,cardName))
    
    if int(card_value) > 13:
        print(cardName)
        finalValue = valueOfcard(cardName,scoreCount)
        print('CARDVALUE(): going in valueOfcard to get: %s' %(finalValue))
        return finalValue
    elif int(card_value) > 10 and int(card_value) < 14:
        print('CARDVALUE(): returning 10')
        return 10
    print('CARDVALUE(): returning %s' %(card_value))
    return int(card_value)


def doKeyExist(key):
    key_2 = key.upper()
    cardType=key_2[0]
    if cardType == "H" and key_2 in cHDict.keys():
        return True
    elif cardType == "D" and key_2 in cDDict.keys():
        return True    
    elif cardType == "S" and key_2 in cSDict.keys():
        return True       
    elif cardType == "C" and key_2 in cCDict.keys():
        return True    
    else:
        print('error in doKeyExist()')
        return False


def deleteCard(key):
    key1 = key.upper()
    card_liability = doKeyExist(key1)
    #modify key1 to go up a notch
    getDict=str(key1[0])
    card_value = key1[:0] + key1[1:]
    card_value = int(card_value) 
    newKey = getDict + str(card_value)
    if card_liability:    
        command="del c" + str(getDict) + "Dict[" + "'" + newKey + "'" + "]"
        print(command)
        exec(command)
    else:
        print('a card that doesnt exist fucking tried to delete')
        
def isDictEmpty():
    if bool(cHDict)==False and bool(cDDict)==False and bool(cCDict)==False and bool(cSDict)==False:
        return True
    else:
        return False        
        
def createCard():#Creates and returns card to drawCard func
    ctDict = {1:"H",2:"D",3:"S",4:"C"}
    cardType = random.randint(1,4)
    card = random.randint(2,14)
    key = str(ctDict[cardType]).lower() + str(card)
    print('checking if key exists')
    key_liability = doKeyExist(key)
    x = 0
    while key_liability != True and isDictEmpty() == False:
        cardType = random.randint(1,4)
        card = random.randint(2,14)
        key = str(ctDict[cardType]).lower() + str(card)
        print('created new key %s' %(key))
        key_liability = doKeyExist(key)
    return key    
        
def pWin():
    import blackJackGUI
    print('DISABLING HIT')
    blackJackGUI.hitBtn.config(state="disabled")
    blackJackGUI.drawText('dealer','player wins!')
    blackJackGUI.bjWin()
def pLoose():
    import blackJackGUI
    print('DISABLING: HIT')
    blackJackGUI.hitBtn.config(state="disabled")
    blackJackGUI.drawText('dealer','House wins!')
    print('calling bjloose()')
    blackJackGUI.bjLoose()
    print('called bjloose()')
    

    
        
def drawCard(user, *args):
    global dealerCount
    global playerCount
    plyr = str(user)
    import blackJackGUI
    try:
            print('\n\n\n ARGS: %s \n\n\n')
            print(args[0])
            a = str(args[0])
    except IndexError:
        a = ''
        print('no args')
# ===========================create card=======================================
    key = createCard()
            
    print('n/CARD DRAW HAS STARTED FOR: %s' %(plyr[0].lower()))
# =============================================================================
    

#___player____________________________________________________________________________________________________________         
    if plyr[0].lower() == 'p':
        print('started drawCard() for %s and the count is: %d' %(plyr,playerCount))
        add_value_player = cardValue(playerCount,key)#Card Value is a function that counts the value of the card drawn
        if playerCount == 0:
            playerCount = playerCount + add_value_player
            blackJackGUI.command(playerCount)
            blackJackGUI.civ('player',key)
            blackJackGUI.drawText('dealer','Do you perhaps want to hit it?')
        else:
            if playerCount <= 21:
                blackJackGUI.drawText('dealer','HIT OR STAND?')
#_______________________________player HIT_______________________________________________
                if a == 'hit':
                    blackJackGUI.civ('player',key) #Paints Card to Canvas
                    playerCount += add_value_player
                    print('PLAYER HIT: playerCount is: %d ' %(playerCount))
                    blackJackGUI.command(playerCount)
                    if playerCount > 21:
                        #player loose
                        #TODO
                        #remove chips
                        pLoose()
                    elif playerCount == 21:
                        madafakka()
                        pWin()
                        
#_______________________________player STAND_______________________________________________
                elif a == 'stand':
                    blackJackGUI.hitBtn.config(state="disabled")
                    print('\n\n\n PLAYER STANDS \n\n\n')
                    drawCard('dealer','stand')
                    
#______________________________________________________________________________
                elif args is None:
                    blackJackGUI.drawText('dealer','Do you want to hit or stand?')
                    print('no arguments passed to drawCard(key,*args), waiting for hit or stand')
                else:
                    print('this error happened because stian is an idiot and drawCard() cant determine hit or stand')
            elif playerCount > 21:
                pLoose()
            else:
                print('error inside drawCard() on player side')
                
#___dealer____________________________________________________________________________________________________________         
    elif plyr[0].lower() == 'd':
        print('started drawCard() for %s and the count is: %d' %(plyr,dealerCount))
        add_value_dealer = cardValue(dealerCount,key)
        
        #FIRST CARD FOR DEALER#
        if dealerCount == 0:
            print('dealer count = 0')
            dealerCount = dealerCount + add_value_dealer
            blackJackGUI.civ('dealer',key)
            print('\nDEALER: drew a card, its a %s, total dealerCount is: %d' %(key,dealerCount))
            blackJackGUI.drawText('dealer', 'press hit to get your first card')
        #IF PLAYER IS ON STAND
        elif dealerCount > 0 and a == 'stand':
            print('dealercount is more than 0 and player is on stand')
            if dealerCount > 0 and dealerCount <= playerCount and dealerCount < 21:
                dealerCount = dealerCount + add_value_dealer
                blackJackGUI.civ('dealer',key)
                #draw another card
                print('/n DEALER: drew a card, its a %s, total dealerCount is: %d' %(key,dealerCount))
                drawCard('dealer','stand')
            elif dealerCount > playerCount and dealerCount <= 21:
                pLoose()
            elif dealerCount > 21:
                pWin()
                #TODO
                #give money to player
            else:
                print('an error occoured inside of drawCard on dealer side, ERROR: %s' %(plyr.lower()))
        
    else:
        print('broken inside drawCard() could not find user')
    
    print('playerCount: %s' %(playerCount))
    print('dealerCount: %s' %(dealerCount))
    deleteCard(key)
    #end of DrawCard

#function to reset the game. All values are set to zero and the games beginnes from the start
def reset():
    global dealerCount
    global playerCount
    global dcn
    playerCount = 0
    dealerCount = 0
    dcn = 0
#    start()
    
  

#only non function code 
#the function start is called and the game begins