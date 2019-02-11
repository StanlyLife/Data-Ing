#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:15:11 2018

@author: Stian
"""


from tkinter import *
from PIL import Image,ImageFilter
from PIL import ImageTk
import Bj_3
import time
import chipModule as cm


pmove = 0
dmove = 0
cmove = 0


root = Tk()
root.geometry('1280x780')
root.configure(bg='green')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

myFrame = Frame(root,bg='red',width=1280, height=780)
#Create Canvas
canvas = Canvas(root,width=1280,height=700,bg='GRAY',highlightthickness=0)
#Title of application
root.title('BJ Boys')


bjlogo2 =  Image.open('assets/bjlogo.png')
pilImage = Image.open("assets/bjtable.png")
bjlogo = Image.open('assets/bjlogo.png')

rez = pilImage.resize((1280,750))
rezbjlogo = bjlogo.resize((250,175))

imagebjbg = ImageTk.PhotoImage(rez,master=root)
imagebjlogo = ImageTk.PhotoImage(rezbjlogo,master=root)

cardPath = Image.open('assets/cards/s13.png')
resCard = cardPath.resize((100,100))
CardVar = ImageTk.PhotoImage(resCard,master=root)


#slider
w = Scale(myFrame, from_=0, to=50,orient=HORIZONTAL,tickinterval=10,length=600)
w.grid(sticky='nw',row=1, column=1)


#___________________put an image on main canvas________________________________
cardList=[]
def createImg(x,y,inputImage,anc):
    global newCard
    global cardList
    cardList.append(inputImage)
    imagesprite = canvas.create_image(x,y,image=cardList[-1],anchor=anc)
#_______________________draw card in correct position__________________________

    
createImg(0,0,imagebjbg,NW)
createImg(0,-45,imagebjlogo,NW)
    
def civ(plyr, key): #create image variables
    global cardPath
    global resCard
    global CardVar
    global pmove
    global dmove
    global cmove
    import Bj_3
    
    getDict=str(key[0])
    card_value = key[:0] + key[1:]
    card_value = int(card_value)-1
    newKey = getDict + str(card_value)
    
    
    cardPath = Image.open('assets/cards/%s.png' %(newKey))
    resCard = cardPath.resize((100,100))
    CardVar = ImageTk.PhotoImage(resCard,master=root)
    if plyr[0].lower() == 'p':
           createImg(600+pmove,500,CardVar,CENTER)
           pmove = pmove + 75
    elif plyr[0].lower() == 'd':
            createImg(600+dmove,210,CardVar,CENTER)
            dmove = dmove + 75

    else:
        print('broken inside civ() couldnt find plyr')
        
def chipCreate(num):
        global cmove
        chipPath = Image.open('assets/chip.png')
        resChip =  chipPath.resize((65,65))
        chipImg = ImageTk.PhotoImage(resChip,master=root)
        x=0
        while x < num:
            createImg(516+(cmove/5),547 - cmove,chipImg,CENTER)
            cmove = cmove + 5
            x = x + 1
   
def obank():
    import bank as bk
    bank = Tk()
    bank.geometry('428x378')
    
    loginFrame = Frame(bank,width=628,height=678)
        
    entry1 = Entry(loginFrame)
    entry2 = Entry(loginFrame)
    entry3 = Entry(loginFrame)
    
    
    Label(loginFrame, text="user name").grid(row=1,column=2)
    Label(loginFrame, text="password").grid(row=3,column=2)
    Label(loginFrame, text="password").grid(row=3,column=2)

    T = Text(bank, height=2, width=30)
    T.pack()

    enBtn = Button(loginFrame, text='login', command=lambda:  T.insert(CURRENT,bk.login_output(entry1.get(),entry2.get())))   
    enBtn.config(fg='black',height=4,width=7)
    enBtn.grid(sticky='nW',row=2,column=3)
    
    enBtn_2 = Button(loginFrame, text='get saldo', command=lambda:  T.insert(CURRENT,str(bk.get_saldo_output()+'\n')))   
    enBtn_2.config(fg='black',height=4,width=7)
    enBtn_2.grid(sticky='nW',row=2,column=4,rowspan=2)
    
    enBtn_3 = Button(loginFrame, text='Buy chips', command=lambda:  T.insert(CURRENT,bk.buychips(bk.current_user,int(entry3.get()))))   
    enBtn_3.config(fg='black',height=4,width=7)
    enBtn_3.grid(sticky='nW',row=13,column=2)
    
    enBtn_4 = Button(loginFrame, text='Sell chips', command=lambda:  T.insert(CURRENT,bk.cashInChips(bk.current_user,int(entry3.get()))))   
    enBtn_4.config(fg='black',height=4,width=7)
    enBtn_4.grid(sticky='nW',row=13,column=3)
     
    entry1.grid(row=2,column=2)
    entry2.grid(row=4,column=2)
    entry3.grid(row=14,column=2)
    loginFrame.pack(side="top",fill="both",expand=True)
    bank.mainloop()
    
global chipsOnTable 
chipsOnTable = 0       
        
#____________________________Calling start in Bj_3________________________________
def startBJ():
    import Bj_3
    import chipModule as cm
    print('starting BJ')
    tcommand('place your bet\n')
    tcommand('Chips: %d\n' %(cm.ChipWallet()) )
    betBtn.config(state="normal")
    startBtn.configure(state="disabled")
    hitBtn.config(state="normal")
    standBtn.config(state="normal")
    resetBtn.configure(state='disabled')
    Bj_3.start()
    
#__________________________Draws text to table on canvas_______________________    
textList = [0]

def drawText(person,txt):
        try:
            print('drawText(): deleted: %d' %(textList[0]))
            canvas.delete(textList[0])
            textList.pop()
        except IndexError:
            print('list was empty did not pop')
        finally:
            if person[0].lower() == 'd':
                a = canvas.create_text(625,130,fill="black",font="Arial 25",text=txt)
                textList.append(a)
            
#__________________________Draws text to table on canvas_______________________    
textList = [0]

def drawText(person,txt):
        try:
            canvas.delete(textList[0])
            textList.pop()
        except IndexError:
            print('list was empty did not pop')
        finally:
            if person[0].lower() == 'd':
                a = canvas.create_text(625,130,fill="black",font="Arial 25",text=txt)
                textList.append(a)


    
#______________________________________________________________________________

#________________hit or stand function_________________________________________
def hors(choice):
    import Bj_3
    if choice == 'hit': #player wants to hit, get a new card
        Bj_3.drawCard('player','hit')
    elif choice == 'stand': #player does not want to hit, dealer hits
        Bj_3.drawCard('player','stand')
    else:
        print('broke inside hors() function')
#__________________resets table and game_______________________________________        
def reset():
    print('\n\n\n RESETTING \n\n\n')
    global pmove
    global dmove
    global cmove
    global cardList
    hitBtn.config(state="normal")
    for i in cardList:
        cardList.pop()
    canvas.delete("all")
    createImg(0,0,imagebjbg,NW)
    createImg(0,-45,imagebjlogo,NW)
    startBtn.config(state='normal')
    betBtn.config(state='normal')
    hitBtn.config(state='disabled')
    standBtn.config(state='disabled')
    resetBtn.config(state='disabled')
    
    pmove = 0
    dmove = 0
    cmove = 0
    import Bj_3
    Bj_3.reset()
#___________________Closes application_________________________________________
def closeApp():
    root.destroy()
    
def callback(event):
    print('X: %d, Y: %d' %(event.x,event.y) )
    drawText('Dealer','mullar krekar 123 fire fem')
 
canvas.bind("<Button-1>", callback)    
    
    
    
#___________________creates buttons____________________________________________    

def command(count):
    tbox.insert(CURRENT,'Player score: %d\n'%(count))
def tcommand(tekst):
    tbox.insert(CURRENT,str(tekst))



def bjWin():
    global chipsOnTable
    print('called bjWin')
    tcommand('you won: %d chips\n' %(chipsOnTable))
    cm.getChips(chipsOnTable)
    tcommand('you have: %d chips\n' %(cm.ChipWallet()))
    chipsOnTable = 0
    standBtn.configure(state='disabled')
    resetBtn.configure(state='normal')
    
def bjLoose():
    global chipsOnTable
    print('called bjLoose')
    tcommand('you lost: %d chips\n' %(chipsOnTable))
    cm.removeChips(chipsOnTable)
    tcommand('you have: %d chips\n' %(cm.ChipWallet()))
    chipsOnTable = 0
    resetBtn.configure(state='normal')
    standBtn.configure(state='disabled')



def bet():
    import chipModule as cm
    global chipsOnTable
    betBtn.configure(state='disabled')
    bs = w.get()
    chipsOnTable = bs
    w.set(1)
    chipCreate(chipsOnTable)
    totalChips = cm.ChipWallet() - chipsOnTable
    cm.removeChips(bs)
    tcommand('betted %d, %d left\n' %(chipsOnTable,totalChips))
    return bs

#buttons
betBtn = Button(myFrame, text='bet',command=lambda: bet())
betBtn.config(fg='black',height=4,width=7,state="disabled")
betBtn.grid(sticky='nW',row=1,column=2,rowspan=5)

bankBtn = Button(myFrame, text='Bank', command=lambda: obank())
bankBtn.config(fg='black',height=4,width=7)
bankBtn.grid(sticky='sW',row=1,column=3,rowspan=5)


hitBtn = Button(myFrame, text='Hit',command=lambda: hors('hit'))
hitBtn.config(fg='black',height=4,width=7,state="disabled")
hitBtn.grid(sticky='sW',row=1,column=4,rowspan=5)

standBtn = Button(myFrame, text='Stand',command=lambda: hors('stand'))
standBtn.config(fg='black',height=4,width=7,state="disabled")
standBtn.grid(sticky='sW',row=1,column=5,rowspan=5)


startBtn = Button(myFrame, text='Start',command=lambda: startBJ())
startBtn.config(fg='black',height=4,width=6)
startBtn.grid(sticky='se',row=1,column=8,rowspan=5)

resetBtn = Button(myFrame, text='Reset',command=lambda: reset())
resetBtn.config(fg='black',height=4,width=6,state="disabled")
resetBtn.grid(sticky='se',row=1,column=9,rowspan=5)

endBtn = Button(myFrame, text='Exit', command=lambda: closeApp())
endBtn.config(fg='black',height=4,width=6, highlightbackground='#3E4149')
endBtn.grid(sticky='se',row=1,column=10,rowspan=5)

tbox = Text(myFrame, height=4, width=20)
tbox.grid(sticky='se',row=1,column=20,rowspan=5)

wbox = Text(myFrame, height=4, width=12)
wbox.configure(bg='lightgray')
wbox.grid(sticky='se',row=1,column=19,rowspan=5)
canvas.pack(side="top", fill="both", expand=True)
myFrame.pack(side="top", fill="both", expand=True)
root.mainloop()



