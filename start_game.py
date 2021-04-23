from numpy import *
from crerebro import *
from Acciones import *
from intervenciones import *
import sys

class Start_Game:
    def __init__(self,Maze,Lplayers,turno):
        self.__Maze = Maze
        self.__Lplayers = Lplayers
        self.__turno = turno
    
    def print_menu(self):
        print("")
        for i in self.__Lplayers:
            if i["influence"] > 0 :
                print(i["name"],"Cards:", len(i["cards"]), "Lost Cards:",i["lostcards"],
                "Coins:",i["coins"],"Influence:",i["influence"])
        print("")
        print("Select one option: ")
        print("1. Executed an action]")
        print("2. See Cards")
        print("3. See log")
        return int(input())

    def print_actions(self):
        print('\nSelect one option:')
        print('1. Income')
        print('2. Foreign Aid')
        print('3. Coup')
        print('4. Duke')
        print('5. Assassinate')
        print('6. Extorsion')
        print('7. Change')
        return int(input())
    
    def chose_player(self):
        a = 1
        


        LV = []
        for i in self.__Lplayers:
            if int(i['influence']) != 0:
                LV.append(i)
        if len(LV) == 1:
            print(LV[0]["name"],'WINS THE GAME') 
            sys.exit()
        print("Chose a player to executed the action:")
        
        
        for i in self.__Lplayers:
            if i["influence"] > 0:
                print(a,". ",i["name"],"Cards:", len(i["cards"]), "Lost Cards:",i["lostcards"],
                "Coins:",i["coins"],"Influence:",i["influence"])
            a+=1
        return int(input())


    def pregunta_d(self, JD):
        L = []
        LD = []
        for i in self.__Lplayers:
            if i['name'] == JD['name']:
                continue

            if i["influence"]<=0:
                continue

            else:
                print(i['name'],'press 1 to challenge, 2 to pass')
                n = int(input())
                L.append([i,n])
        for k in L:
            if k[1] == 1:
                LD.append(k[0])
        random.shuffle(LD)
        if len(LD)>0:
            return LD[0]
        else:
            return False

    def pregunta_c(self, JC):
        L = []
        LC = []
        for i in self.__Lplayers:
            if i['name'] == JC['name']:
                continue

            if i["influence"]<=0:
                continue

            else:
                print(i['name'],'press 1 to counteraction, 2 to pass')
                n = int(input())
                L.append([i,n])
        for k in L:
            if k[1] == 1:
                LC.append(k[0])
        random.shuffle(LC)
        if len(LC)>0:
            return LC[0]
        else:
            return False

    def game(self):
        LV = []
        for i in self.__Lplayers:
            if int(i['influence']) != 0:
                LV.append(i)
        if len(LV) == 1:
            print(LV[0]["name"],'WINS THE GAME') 
            sys.exit()

        JA = self.__Lplayers[self.__turno]["name"]
        print('\n',JA,"is your turn")
        selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_menu()
        
        
        
        
        if selection == 1:
            for i in self.__Lplayers:
                i['log'].append(f'{JA}`s turn has started ')
            
            
            if self.__Lplayers[self.__turno]["coins"] >= 10:
                print("You have 10 or more coins, you must launch Coup")
                c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Golpe()
                self.__Lplayers[self.__turno]['coins'] = coup[0]
                self.__Lplayers[c-1] = coup[1]
                for i in self.__Lplayers:
                    cp1 = self.__Lplayers[c-1]['name']
                    i['log'].append(f'{JA} has been forced to use Coup on {cp1}')
                
            
           
            selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_actions()
           
            if selection == 1:
                print('The player ',self.__Lplayers[self.__turno]['name'],"has bee used 'Income'(+1 coin)")
                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ingreso()
                self.__Lplayers[self.__turno]['coins'] = nd 
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Income ')
            
            
            if selection == 2:
                print('Player ',self.__Lplayers[self.__turno]['name'],"has used 'Foreign Aid'")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Foreign Aid ')
                d =False
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                    if c == False:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} has executed Foreign Aid successfully ')
                        nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ayuda_Extrangera()
                        self.__Lplayers[self.__turno]['coins'] = nd
                    else:
                        for i in self.__Lplayers:
                            c1 = c['name']
                            i['log'].append(f'{c1} Blocked Foreign Aid from {JA}')
                        print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)

                        if d == False:
                            print("Nobody challenged the Block ")
                            pass
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                c1 = c['name']
                                i['log'].append(f'{d1} has Challenged {c1} Block ')
                            a = Intervenciones(c,d,self.__Maze).Desafio('Duke')
                            if a[3] == 0:
                                for i in self.__Lplayers:
                                    c1 = c['name']
                                    i['log'].append(f'{c1} wins challenge ')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]

                            else:
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    i['log'].append(f'{d1} wins challenge ')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                                for i in self.__Lplayers:
                                    i['log'].append(f'{JA} has executed Foreign Aid successfully ')
                                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ayuda_Extrangera()
                                self.__Lplayers[self.__turno]['coins'] = nd
                                

    
           
           
           
            if selection == 3:
                if self.__Lplayers[self.__turno]["coins"] >= 7:

                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has executed Coup ')
                    coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Golpe()
                    self.__Lplayers[self.__turno]['coins'] = coup[0]
                    self.__Lplayers[c-1] = coup[1]
                else:
                    print("not enough coins to execute Coup")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
            
            
            
            
            if selection == 4:
                print(JA,"has used Tax")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Tax ')
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == False:
                    nd = Actions(" ",self.__Lplayers[self.__turno],self.__Maze).Tax()
                    self.__Lplayers[self.__turno]['coins'] = nd
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has executed Tax successfully ')
                else:
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenged {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Duke')
                    if a[3] == 0:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge and executed Tax successfully ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Tax()
                        self.__Lplayers[self.__turno]['coins'] = nd
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins the challenge Tax not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]


            
            if selection == 5:


                if self.__Lplayers[self.__turno]["coins"] >= 3:
                    print(JA,"has used Assassinate")
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has used Assessinate ')
                    self.__Lplayers[self.__turno]['coins'] += -3
                    d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                    if d == False:
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                        if c == False:
                            
                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()

                            for i in self.__Lplayers:
                                i['log'].append(f'{JA} executed Assessinate on {self.__Lplayers[cp-1]} ')
                            asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                            self.__Lplayers[cp-1] = asse[1]
                        else:
                            for i in self.__Lplayers:
                                c1 = c['name']
                                i['log'].append(f'{c1} has blocked Assassination ')
                            print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                            if d == False:
                                print("Assassination has been blocked")
                                
                                pass
                            else:
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    c1 = c['name']
                                    i['log'].append(f'{d1} challenged {c1}`s block ')
                                a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                if a[3] == 0:
                                    for i in self.__Lplayers:
                                        c1 = c['name']
                                        i['log'].append(f'{c1} wins challenge Assassination not executed')
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                else:
                                    
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                    asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        i['log'].append(f'{d1} wins challenge and {JA} Assassinates {self.__Lplayers[cp-1]}')
                                    self.__Lplayers[cp-1] = asse[1]
                    else: 
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} challenges Assassination ')
                        a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Assassin')
                        if a[3] == 0:
                            for i in self.__Lplayers:
                                i['log'].append(f'{JA} wins challenge')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                            c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                            if c!= False:
                                for i in self.__Lplayers:
                                    c1 = c['name']
                                    i['log'].append(f'{c1} blocks Assassination ')
                                print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                                if d == False:
                                    print("nobody challenges the block")
                                    
                                else:
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        c1 = c['name']
                                        i['log'].append(f'{d1} challenges {c1}`s block ')
                                    a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                    if a[3] == 0:
                                        for i in self.__Lplayers:
                                            c1 = c['name']
                                            i['log'].append(f'{c1} wins the challenge ')
                                        self.__Maze = a[2]
                                        ind = self.__Lplayers.index(c) 
                                        self.__Lplayers[ind] = a[0]
                                        ind = self.__Lplayers.index(d) 
                                        self.__Lplayers[ind] = a[1]
                                    else:
                                        
                                        self.__Maze = a[2]
                                        ind = self.__Lplayers.index(c) 
                                        self.__Lplayers[ind] = a[0]
                                        ind = self.__Lplayers.index(d) 
                                        self.__Lplayers[ind] = a[1]
                                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                        for i in self.__Lplayers:
                                            d1 = d['name']
                                            i['log'].append(f'{d1} wins the challenge, {JA} assassinated {self.__Lplayers[cp-1]}')
                                        asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                        self.__Lplayers[cp-1] = asse[1]
                            else:
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                for i in self.__Lplayers:
                                    i['log'].append(f'{JA} assessinated {self.__Lplayers[cp-1]} ')
                                self.__Lplayers[cp-1] = asse[1]
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                i['log'].append(f'{d1} wins challenge ')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                else:
                    print("Not enough coins to use assessination, press any key to go back")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()






           
            if selection == 6:
                print(JA,"has used Steal")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                    if c == False:
                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                        for i in self.__Lplayers:
                            cp1 = self.__Lplayers[cp-1]['name']
                            i['log'].append(f'{JA} stealed from {cp1}')
                        nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                        self.__Lplayers[self.__turno]= nd[1]
                        self.__Lplayers[cp-1] = nd[0]
                    else:
                        for i in self.__Lplayers:
                            c1 = c['name']
                            i['log'].append(f'{c1} blocks Steal ')
                        print(self.__Lplayers[self.__turno]['name']," has been blocked by ",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                        if d == False:
                            print("nobody challenges the block")
                            pass
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                c1 = c['name']
                                i['log'].append(f'{d1} challenges {c1} ')
                            a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                            if a[3] == 0: #gana c
                                for i in self.__Lplayers:
                                    c1 = c['name']
                                    i['log'].append(f'{c1} wins challenge, Stealing not executed')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                            else: 
                                
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    cp1 = self.__Lplayers[cp-1]['name']
                                    i['log'].append(f'{d1} wins the challenge, {JA} steals from {cp1} ')
                                nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                self.__Lplayers[self.__turno]= nd[1]
                                self.__Lplayers[cp-1] = nd[0]
                else: 
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenged {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio_esp()                        
                    if a[3] == 0: 
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                        if c != False: 
                            for i in self.__Lplayers:
                                c1 = c['name']
                                i['log'].append(f'{c1} blocked Steal ')
                            print(self.__Lplayers[self.__turno]['name'],"has been blocked by ",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                            if d == False:
                                print("nobody challenges the block")
                                pass
                            else:
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    c1 = c['name']
                                    i['log'].append(f'{d1} challenged {c1}`s block ')
                                a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                                if a[3] == 0:
                                    for i in self.__Lplayers:
                                        c1 = c['name']
                                        i['log'].append(f'{c1} wins challenge, Steal not executed ')
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                else:

                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        cp1 = self.__Lplayers[cp-1]['name']
                                        i['log'].append(f'{d1} wins challenge, {JA} steals from {cp1} ')
                                    nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                    self.__Lplayers[self.__turno]= nd[1]
                                    self.__Lplayers[cp-1] = nd[0]
                        else:

                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                            nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                            for i in self.__Lplayers:
                                cp1 = self.__Lplayers[cp-1]['name']
                                i['log'].append(f'{JA} steals from {cp1} ')
                            self.__Lplayers[self.__turno]= nd[1]
                            self.__Lplayers[cp-1] = nd[0]
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins challenge, Steal not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
            
            
            if selection == 7:
                print(JA," used Exchange")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Exchange ')
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == 0:
                    cambio = Actions(" ",self.__Lplayers[self.__turno],self.__Maze).Cambio()
                    self.__Lplayers[self.__turno] = cambio[0]
                    self.__Maze = cambio[1]
                else:
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenges {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Ambassador')
                    if a[3] == 0:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        cambio = Actions('',self.__Lplayers[self.__turno],self.__Maze).Cambio()
                        self.__Lplayers[self.__turno] = cambio[0]
                        self.__Maze = cambio[1]
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]

            self.__Lplayers[self.__turno]['log']=[]
            self.__turno += 1
            if self.__turno > len(self.__Lplayers)-1:
                self.__turno = 0
            while self.__Lplayers[self.__turno]['influence'] <= 0:
                self.__turno += 1
                if self.__turno > len(self.__Lplayers)-1:
                    self.__turno = 0
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()


        if selection == 2:
            print(self.__Lplayers[self.__turno]["cards"])
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
        

        if selection == 3:
            print(self.__Lplayers[self.__turno]["log"])
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()

