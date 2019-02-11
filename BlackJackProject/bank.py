# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:08:45 2018

@author: Hans
"""



import hashlib

def get_saldo_output():
    return str(str(saldocheck(current_user)) +  "\n")


def login_output(userName,password):
    x,y=inlog(userName,password)
    if x == True:
        global current_user
        current_user=userName
    login_status=x
    print("Login status: " + str(login_status))
    current_user=userName
    return y


def hash_password(password):
    # uuid blir brukt til å generere et tilfeldig tall
    return hashlib.sha256(password.encode()).hexdigest()




def inlog(Username,Password):
    with open("assets/bjdb.txt", "a") as bjdb:#åpner txt fil aka "databasen"      
        bnavn =Username
        pord =Password
        
        #hashe passordet for sinnsykt nødvendig sikkerhet
        hashedpassword = hashlib.sha256(pord.encode()).hexdigest()
        #sjekke om brukernavn er i databasen
        returned_value = usercheck(bnavn)#variabel for utfall av usercheck
        returned_value1 = passcheck(hashedpassword)#--------------"------- passchec
        if returned_value == True and returned_value1 == False:
            return False, "Dette brukernavnet er tatt\n"
        elif returned_value == True and returned_value1 == True:
            return True, "Velkommen tilbake\n"
        elif len(pord) < 4:
            return False, "Passord er for Kort\n"
        else:
            bjdb.write("\n%s;%s;%d" %(bnavn,hashedpassword,1000))#legger inn brukernavn og passord i databasen (og startsaldo)
            return True, "Velkommen ny bruker\n"
        
        


#funksjon for å sjekke om brukernavn allerede finnes i database
def usercheck(username):
    found = False
    with open("assets/bjdb.txt", "rt") as fil:#åpner txt fil og leser
        for line in fil:
            if username in line:#sjekker om brukernavnet finnes i filen
                found = True
                
    return found

def saldocheck(brukernavn):
    with open ('assets/bjdb.txt', 'rt') as in_file: 
        for line in in_file:
            if brukernavn in line:
                i=len(brukernavn)
                pos = max(line.find(brukernavn), 0)     
                line=line[pos+i+1:]
                pos = max(line.find(';'), 0)      
                return int(line[pos+1:])

#funksjon for å sjekke om passordet eksisterer 
def passcheck(password):
    found = False
    with open("assets/bjdb.txt", "rt") as fil:#åpner txt fil og leser
        for line in fil:
            if password in line:#sjekker om passordet finnes i filen
                found = True
    return found

    
def ChipWallet():
    with open ('assets/chips.txt', 'r') as in_file: 
        for line in in_file:            
            return int(line)
            

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
   
            