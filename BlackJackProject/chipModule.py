#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:34:46 2018

@author: Stian
"""
def changeAmountOfChips(chips):
    new_line=""
    with open ('assets/chips.txt', 'r') as in_file: 
        for line in in_file:            
            new_line=int(line)+chips
    with open ('assets/chips.txt', 'a') as in_file:
        in_file.seek(0)
        in_file.truncate()
        in_file.write(str(new_line))


def buychips(brukernavn,chips):
    saldo=0
    line_2=""
    elements=[]
    with open ('assets/bjdb.txt', 'rt') as in_file: 
        for line in in_file:
            if brukernavn in line:
                #creat useful varibals
                line_2=line #used to creat replacment 
                line_3=line #used to find and replace current line 
                i=len(brukernavn)
                
                #find saldo in line
                line_3=line
                pos = max(line_3.find(brukernavn), 0)     
                line_3=line_3[pos+i+1:]
                pos = max(line_3.find(';'), 0)      
                saldo=int(line_3[pos+1:])
                print(line_3)
                #find new saldo with math
                new_saldo=saldo-(10*chips)
                pos = line_2.find(str(saldo)) 
                   
                    #remove old saldo and append to line_2
                line_2=line_2[:pos]
                line_2=line_2+str(new_saldo)
    
                    #replace text in bjdb.txt
                    #in_file.write(line.replace(line_3, line_2))
                
                
                 
                        
            else:
                elements.append(line)
    with open ('assets/bjdb.txt', 'w') as in_file: 
        in_file.seek(0)
        in_file.truncate()
        for y in range(len(elements)):
            in_file.write(elements[y])
            in_file.write("\n")
        in_file.write(line_2)
    changeAmountOfChips(chips)
    return chips
            
def cashInChips(brukernavn,chips):
    saldo=0
    line_2=""
    elements=[]
    with open ('assets/bjdb.txt', 'rt') as in_file: 
        for line in in_file:
            if brukernavn in line:
                #creat useful varibals
                line_2=line #used to creat replacment 
                line_3=line #used to find and replace current line 
                i=len(brukernavn)
                        
                        #find saldo in line
                line_3=line
                pos = max(line_3.find(brukernavn), 0)     
                line_3=line_3[pos+i+1:]
                pos = max(line_3.find(';'), 0)      
                saldo=int(line_3[pos+1:])
                print(line_3)
                        #find new saldo with math
                new_saldo=saldo+(10*chips)
                pos = line_2.find(str(saldo)) 
                           
                        #remove old saldo and append to line_2
                line_2=line_2[:pos]
                line_2=line_2+str(new_saldo)
            
                            #replace text in bjdb.txt
                            #in_file.write(line.replace(line_3, line_2))
                        
                         
                                
            else:
                elements.append(line)
    with open ('assets/bjdb.txt', 'w') as in_file: 
        in_file.seek(0)
        in_file.truncate()
        for y in range(len(elements)):
            in_file.write(elements[y])
            in_file.write("\n")
        in_file.write(line_2)
        changeAmountOfChips(-chips)
        
def getChips(betted_chips):
     changeAmountOfChips(betted_chips*2)
     
def removeChips(betted_chips):
     changeAmountOfChips(-betted_chips)

def ChipWallet():
    with open ('assets/chips.txt', 'r') as in_file: 
        for line in in_file:            
            return int(line)












