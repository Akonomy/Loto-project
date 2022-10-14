menu={
    "1":"Alege modul de joc 6/49 sau 5/40",
    "2":"cumpara bilet",
    "3":"joaca un bilet",
    "4":"joaca toate biletele",
    "5":"afiseaza monedele"
    }

money=500
bilet640=0
bilet540=0
cpy=0
def alegeMod(a,b):
     print("Va rugam sa alegeti intre",a,"si",b,)
     w=input("Alege:\n")
     if str(w) ==a:
         s=0
     elif str(w) ==b:
         s=1
     else:
         print("invalid")
     return s
    
def casierie(mod,money,bilet640,bilet540):
    if mod == 0:
        print("Bun venit la casierie, un bilet costa 15 monezi")
        buy=int(input("Cate bilete doriti sa cumparati?"))
        if buy > 0:
            for i in range(buy):
             if money >= 15:
                money-=15
                bilet640+=1
                
             else:
                 print("Nu mai ai destul credit pentru a cumpara bilete")
                 
            print("Acum aveti",bilet640,"de bilete si",money,"monezi")
             
            
    elif mod == 1:
        print("Bun venit la casierie, un bilet costa 20 monezi")
        buy=int(input("Cate bilete doriti sa cumparati?"))
        if buy > 0:
            for i in range(buy):
             if money >=20:
                money=money-20
                bilet540+=1
                
             else:
                 print("Nu mai ai destul credit pentru a cumpara bilete")
                 
                 
            print("Acum aveti",bilet540,"de bilete si",money,"monezi")
    cash=[money,bilet640,bilet540]        
    return cash


def joacaBilet(money,mod,bilet640,bilet540,cpy):
    choice640=[50,51,52,53,54,55]
    choice540=[50,51,52,53,54]
    verify640=[50,51,52,53,54,55]
    verify540=[50,51,52,53,54]
    counter=0
    valid=0
    print("Ai",bilet640,"bilete la 6/49 si",bilet540,"bilete la 5/40")
    if mod == 0:
        if bilet640>0:
            print("Bun venit la jucarea biletului:")
            cpy+=1
            bilet640=bilet640-1
            while(counter<6):
                    
             for x in range(1000):
                  
               choice640[counter]=int(input("Adaugati element : \t"))
               if choice640[counter]>=0 and choice640[counter]<=49:
                    verify640=choice640
                    verify640.sort()
                    valid=0
               if valid == 0:     
                if verify640[0]!=verify640[1] and verify640[1] != verify640[2]:
                   if verify640[2]!=verify640[3] and verify640[3] != verify640[4]:
                       if verify640[4]!=verify640[5]:
                        valid+=1
                        counter+=1
                        break
               else:
                 print("invalid")
                     
            
        else:
         print("credit insuficient")
        print(choice640,bilet640)        
        
    elif mod == 1:
        if bilet540>0:
            print("Bun venit la jucarea biletului:")
            bilet540-=1
            while(counter<5):
              for x in range(1000):
                  
               choice540[counter]=int(input("Adaugati element : \t"))
               if choice540[counter]>=0 and choice540[counter]<=40:
                    verify540=choice540
                    verify540.sort()
                    valid=0
               if valid == 0:     
                if verify540[0]!=verify540[1] and verify540[1] != verify540[2]:
                   if verify540[2]!=verify540[3] and verify540[3] != verify540[4]:
                       valid+=1
                       counter+=1
                       break
               else:
                 print("invalid")
        else:
           print("credit insuficient")
        print(choice540)
      
    else:
        print("null")
        
    cash=[money,bilet640,bilet540,choice640,choice540,cpy]
    return cash

#alegerea numerelor

def extragereNumere(cpy,choice640,choice540,mod,money):
    random640=[50,51,52,53,54,55]
    random540=[50,51,52,53,54]
    verify640=[50,51,52,53,54,55]
    verify540=[50,51,52,53,54]
    valid=1
    castig=0
    counter=0
    loss=0
    win=0
    if mod==0:
     if cpy<5:
        while(counter<6):
            import random
            for x in range(1000):
               random640[counter]=random.randint(0,49)
               
               verify640=random640
               verify640.sort()
               valid=0
               if valid == 0:     
                if verify640[0]!=verify640[1] and verify640[1] != verify640[2]:
                   if verify640[2]!=verify640[3] and verify640[3] != verify640[4]:
                       if verify640[4]!=verify640[5]:
                        valid+=1
                        try:
                          ty=bool(choice640.remove(random640[x])) 
                        except:
                          ty=True
                        if ty == True: 
                         counter+=1
                        break
        print("Ai pierdut, ne pare rau") 
        print("Numere extrase ",random640.sort(),"\n Numere jucate",choice640.sort())
        #cod de verificare
       
             
        #print("Numere extrase ",random640,"\n Numere jucate",choice640)
     elif cpy>=5:
        while(counter<6):
            import random
            for x in range(1000):
               random640[counter]=random.randint(0,49)
               
               verify640=random640
               verify640.sort()
               valid=0
               if valid == 0:     
                if verify640[0]!=verify640[1] and verify640[1] != verify640[2]:
                   if verify640[2]!=verify640[3] and verify640[3] != verify640[4]:
                       if verify640[4]!=verify640[5]:
                        valid+=1
                        counter+=1
                        break
            
        for x in range(6):
            ty=True
            try:
             ty=bool(choice640.remove(random640[x])) 
            except:
             ty=True
            if ty:
                loss+=1
            else:
                win+=1
        if win == 6:
            print("Ai castigat 100000 yuupi")
            money+=100000
            cpy=-5
            win=0
        elif win == 5:
            print("Ai castigat 5000 yey")
            money+=5000
            cpy=0
            win=0
        elif win == 4:
            print("Ai castigat 2000 yay")
            money+=2000
            cpy=0
            win=0
        else:
            print("Ai pierdut, ne pare rau")    
     print("Numere extrase",random640 ,"\nNumere jucate",choice640)
        
    #############    
    if mod==1:

     if cpy<5:
        while(counter<5):
            import random
            for x in range(1000):
               random540[counter]=random.randint(0,40)
               
               verify540=random540
               verify540.sort()
               valid=0
               if valid == 0:     
                if verify540[0]!=verify540[1] and verify540[1] != verify640[2]:
                   if verify540[2]!=verify540[3] and verify540[3] != verify540[4]:
                       if verify540[4]!=verify540[5]:
                        valid+=1
                        try:
                          ty=bool(choice540.remove(random540[x])) 
                        except:
                          ty=True
                        if ty == True: 
                         counter+=1
                        break
        cash=[money,cpy]            
        print("Ai pierdut, ne pare rau") 
        print("Numere extrase ",random540.sort(),"\n Numere jucate",choice540.sort())
        #cod de verificare
       
             
        #print("Numere extrase ",random540,"\n Numere jucate",choice540)
     elif cpy>=5:
        while(counter<6):
            import random
            for x in range(1000):
               random540[counter]=random.randint(0,49)
               
               verify540=random540
               verify540.sort()
               valid=0
               if valid == 0:     
                if verify540[0]!=verify540[1] and verify540[1] != verify540[2]:
                   if verify540[2]!=verify540[3] and verify540[3] != verify540[4]:
                       if verify540[4]!=verify540[5]:
                        valid+=1
                        counter+=1
                        break
            
        for x in range(5):
            ty=True
            try:
             ty=bool(choice540.remove(random540[x])) 
            except:
             ty=True
            if ty:
                loss+=1
            else:
                win+=1
        if win == 5:
            print("Ai castigat 100000 yuupi")
            money+=105000
            cpy=-5
            win=0
        elif win == 4:
            print("Ai castigat 5000 yey")
            money+=4000
            cpy=0
            win=0
        elif win == 3:
            print("Ai castigat 2000 yay")
            money+=1000
            cpy=0
            win=0
        else:
            print("Ai pierdut, ne pare rau")    
     print("Numere extrase",random540 ,"\nNumere jucate",choice540)
     cash=[money,cpy]         
    return cash
def print_menu():
    print("\--------MENIU---------/" )
    for x in menu.keys():
        print(x, "->",menu[x])
        #facem un while care v-a printa meniul apoi va cere o optiune
while(True):
 print_menu()
 option = input("Enter the option, please \n")
 
 if option == "1":
     mod=alegeMod("6/49","5/40")
     print("A fost ales modul",mod)
 elif option == "2":
     cash=casierie(mod,money,bilet640,bilet540)
     money=cash[0]
     bilet640=cash[1]
     bilet540=cash[2]
     
 elif option == "3":
     cash=joacaBilet(money,mod,bilet640,bilet540,cpy)
     #cash=[money,bilet640,bilet540,choice640,choice540,cpy]
     money=cash[0]
     bilet640=cash[1]
     bilet540=cash[2]
     choice640=cash[3]
     choice540=cash[4]
     cpy=cash[5]
     cash=extragereNumere(cpy,choice640,choice540,mod,money)
     money=cash[0]
     cpy=cash[1]
     print("Ai ramas cu ",money,"monezi")
 elif option == "4":
     while(True):
      cash=joacaBilet(money,mod,bilet640,bilet540,cpy)
      #cash=[money,bilet640,bilet540,choice640,choice540,cpy]
      money=cash[0]
      bilet640=cash[1]
      bilet540=cash[2]
      choice640=cash[3]
      choice540=cash[4]
      cpy=cash[5]
      cash=extragereNumere(cpy,choice640,choice540,mod,money)
      money=cash[0]
      cpy=cash[1]
      print("Ai ramas cu ",money,"monezi")
      if bilet640==0 and mod==0:
          print("Ai ramas fara bilete la 6/49")
          break
      elif bilet540==0 and mod==1:
          print("Ai ramas fara bilete la 5/40")
          break
 elif option == "5":
     print("Ai ",money,"monezi")
     
 elif option == "key":
     password=input("va rugam introduceti cheia de acces\n")
     if password == "":
         print("Ai ",cpy,"zona")
         cpy=int(input("Scan \n"))
         bilet540=2
         bilet640=2
         mod=0
     else:
         print("")
 
 else:
     print("Invalid, ca rugam sa alegeti un numar din meniu")
