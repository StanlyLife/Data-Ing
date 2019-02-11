#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:07:57 2018

@author: Stian

"""

from tkinter import *
from PIL import Image,ImageFilter
from PIL import ImageTk



def mainApp():
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
    
    createImg(0,0,imagebjbg,NW)
    createImg(0,-45,imagebjlogo,NW)
    
    #slider
    w = Scale(myFrame, from_=0, to=42,orient=HORIZONTAL,tickinterval=10,length=600)
    w.grid(sticky='nw',row=1, column=1)
    
    #buttons
    prntBtn = Button(myFrame, text='print it')
    prntBtn.config(fg='black',height=4,width=7)
    prntBtn.grid(sticky='nW',row=1,column=2,rowspan=5)
    
    bankBtn = Button(myFrame, text='Bank', command=lambda: bjg.obank())
    bankBtn.config(fg='black',height=4,width=7)
    bankBtn.grid(sticky='sW',row=1,column=3,rowspan=5)
    
    
    hitBtn = Button(myFrame, text='Hit',command=lambda: bjg.hors('hit'))
    hitBtn.config(fg='black',height=4,width=7)
    hitBtn.grid(sticky='sW',row=1,column=4,rowspan=5)
    
    standBtn = Button(myFrame, text='Stand',command=lambda: bjg.hors('stand'))
    standBtn.config(fg='black',height=4,width=7)
    standBtn.grid(sticky='sW',row=1,column=5,rowspan=5)
    
    aFriendBtn = Button(myFrame, text='Add Friend')
    aFriendBtn.config(fg='black',height=4,width=6)
    aFriendBtn.grid(sticky='se',row=1,column=7,rowspan=5)
    
    startBtn = Button(myFrame, text='Start',command=lambda: blackJackGUI.start())
    startBtn.config(fg='black',height=4,width=6)
    startBtn.grid(sticky='se',row=1,column=8,rowspan=5)
    
    endBtn = Button(myFrame, text='Exit', command=lambda: bjg.closeApp())
    endBtn.config(fg='black',height=4,width=6, highlightbackground='#3E4149')
    endBtn.grid(sticky='se',row=1,column=9,rowspan=5)
    #packing
    canvas.pack(side="top", fill="both", expand=True)
    myFrame.pack(side="top", fill="both", expand=True)
    root.mainloop()