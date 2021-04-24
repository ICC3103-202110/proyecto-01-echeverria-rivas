from numpy import *
from crerebro import *
from Acciones import *
from intervenciones import *
import sys

class Start_Game:
    def __init__(self,Maze,Lplayers,turn):
        self.__Maze = Maze
        self.__Lplayers = Lplayers
        self.__turn = turn
    
    def print_menu(self):
        
        for i in range(len(self.__Lplayers)):
            if self.__Lplayers[i]["influence"] > 0 :
                for n,d in self.__Lplayers[i].items():
                    if n != 'log':
                        if n== 'name':
                            print(n,d,sep=':  ',end='\t\t')
        print('\n')
        for i in range(len(self.__Lplayers)):
            if self.__Lplayers[i]["influence"] > 0 :
                for n,d in self.__Lplayers[i].items():
                    if n != 'log':
                        if n== 'cards':
                            print(n,len(d),sep=': ',end='\t\t')
        print('\n')    

        for i in range(len(self.__Lplayers)):
            if self.__Lplayers[i]["influence"] > 0 :
                for n,d in self.__Lplayers[i].items():
                    if n != 'log':
                        if n== 'coins':
                            print(n,d,sep=': ',end='\t\t')
        print('\n')

        for i in range(len(self.__Lplayers)):
            if self.__Lplayers[i]["influence"] > 0 :
                for n,d in self.__Lplayers[i].items():
                    if n != 'log':
                        if n== 'influence':
                            print(n,d,sep=': ',end='\t\t')
        print('\n')

        for i in range(len(self.__Lplayers)):
            if self.__Lplayers[i]["influence"] > 0 :
                for n,d in self.__Lplayers[i].items():
                    if n != 'log':
                        if n== 'lostcards':
                            print(n,d,sep=': ',end='\t\t')
        print('\n')                            
                        
        print('\n')
        
        print("Select one option: ")
        print("1. Execute an action")
        print("2. See Cards")
        print("3. See log")
        return int(input())

    def print_actions(self):
        print('Select one option:')
        print('1. Income')
        print('2. Foreign Aid')
        print('3. Coup')
        print('4. Tax')
        print('5. Assassinate')
        print('6. Steal')
        print('7. Exchange')
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
            if i["influence"] > 0 and i['name'] !=self.__Lplayers[self.__turn]['name']:
                print(a,". ",i["name"],"Cards:", len(i["cards"]), "Lost Cards:",i["lostcards"],
                "Coins:",i["coins"],"Influence:",i["influence"])
            a+=1
        return int(input())


    def Question_d(self, JD):
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

    def Question_c(self, JC):
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

        JA = self.__Lplayers[self.__turn]["name"]
        print('\n','------------------------',JA,"is your turn------------------------------------")
        selection = Start_Game(self.__Maze,self.__Lplayers,self.__turn).print_menu()
        
        
        
        
        if selection == 1:
            for i in self.__Lplayers:
                i['log'].append(f'{JA} turn has started ')
            
            
            if self.__Lplayers[self.__turn]["coins"] >= 10:
                print("You have 10 or more coins, you must launch Coup")
                c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turn],self.__Maze).Coup()
                self.__Lplayers[self.__turn]['coins'] = coup[0]
                self.__Lplayers[c-1] = coup[1]
                for i in self.__Lplayers:
                    cp1 = self.__Lplayers[c-1]['name']
                    i['log'].append(f'{JA} has been forced to use Coup on {cp1}')
                
            
           
            selection = Start_Game(self.__Maze,self.__Lplayers,self.__turn).print_actions()
           
            if selection == 1:
                print('The player ',self.__Lplayers[self.__turn]['name'],"has bee used 'Income'(+1 coin)")
                nd = Actions("",self.__Lplayers[self.__turn],self.__Maze).Income()
                self.__Lplayers[self.__turn]['coins'] = nd 
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Income ')
            
            
            if selection == 2:
                print('Player ',self.__Lplayers[self.__turn]['name'],"has used 'Foreign Aid'")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Foreign Aid ')
                d =False
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_c(self.__Lplayers[self.__turn])
                    if c == False:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} has executed Foreign Aid successfully ')
                        nd = Actions("",self.__Lplayers[self.__turn],self.__Maze).Foreign_aid()
                        self.__Lplayers[self.__turn]['coins'] = nd
                    else:
                        for i in self.__Lplayers:
                            c1 = c['name']
                            i['log'].append(f'{c1} Blocked Foreign Aid from {JA}')
                        print(self.__Lplayers[self.__turn]['name'],"has been blocked by",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(c)

                        if d == False:
                            print("Nobody challenged the Block ")
                            pass
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                c1 = c['name']
                                i['log'].append(f'{d1} has Challenged {c1} Block ')
                            a = Interventions(c,d,self.__Maze).Challenge('Duke')
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
                                nd = Actions("",self.__Lplayers[self.__turn],self.__Maze).Foreign_aid()
                                self.__Lplayers[self.__turn]['coins'] = nd
                                

    
           
           
           
            if selection == 3:
                if self.__Lplayers[self.__turn]["coins"] >= 7:

                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has executed Coup ')
                    coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turn],self.__Maze).Coup()
                    self.__Lplayers[self.__turn]['coins'] = coup[0]
                    self.__Lplayers[c-1] = coup[1]
                else:
                    print("not enough coins to execute Coup")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turn).game()
            
            
            
            
            if selection == 4:
                print(JA,"has used Tax")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Tax ')
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(self.__Lplayers[self.__turn])
                if d == False:
                    nd = Actions(" ",self.__Lplayers[self.__turn],self.__Maze).Tax()
                    self.__Lplayers[self.__turn]['coins'] = nd
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has executed Tax successfully ')
                else:
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenged {JA} ')
                    a = Interventions(self.__Lplayers[self.__turn],d,self.__Maze).Challenge('Duke')
                    if a[3] == 0:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge and executed Tax successfully ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        nd = Actions("",self.__Lplayers[self.__turn],self.__Maze).Tax()
                        self.__Lplayers[self.__turn]['coins'] = nd
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins the challenge Tax not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]


            
            if selection == 5:


                if self.__Lplayers[self.__turn]["coins"] >= 3:
                    print(JA,"has used Assassinate")
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has used Assessinate ')
                    self.__Lplayers[self.__turn]['coins'] += -3
                    d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(self.__Lplayers[self.__turn])
                    if d == False:
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_c(self.__Lplayers[self.__turn])
                        if c == False:
                            
                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()

                            for i in self.__Lplayers:
                                ff=self.__Lplayers[cp-1]['name']
                                i['log'].append(f'{JA} executed Assessinate on {ff} ')
                            asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Assassination()
                            self.__Lplayers[cp-1] = asse[1]
                        else:
                            for i in self.__Lplayers:
                                c1 = c['name']
                                i['log'].append(f'{c1} has blocked Assassination ')
                            print(self.__Lplayers[self.__turn]['name'],"has been blocked by",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(c)
                            if d == False:
                                print("Assassination has been blocked")
                                
                                pass
                            else:
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    c1 = c['name']
                                    i['log'].append(f'{d1} challenged {c1} block ')
                                a = Interventions(c,d,self.__Maze).Challenge('Contessa')
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
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                                    asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Assassination()
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        ff=self.__Lplayers[cp-1]['name']
                                        i['log'].append(f'{d1} wins challenge and {JA} Assassinates {ff}')
                                    self.__Lplayers[cp-1] = asse[1]
                    else: 
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} challenges Assassination ')
                        a = Interventions(self.__Lplayers[self.__turn],d,self.__Maze).Challenge('Assassin')
                        if a[3] == 0:
                            for i in self.__Lplayers:
                                i['log'].append(f'{JA} wins challenge')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turn] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                            c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_c(self.__Lplayers[self.__turn])
                            if c!= False:
                                for i in self.__Lplayers:
                                    c1 = c['name']
                                    i['log'].append(f'{c1} blocks Assassination ')
                                print(self.__Lplayers[self.__turn]['name'],"has been blocked by",c["name"])
                                d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(c)
                                if d == False:
                                    print("nobody challenges the block")
                                    
                                else:
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        c1 = c['name']
                                        i['log'].append(f'{d1} challenges {c1} block ')
                                    a = Interventions(c,d,self.__Maze).Challenge('Contessa')
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
                                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                                        for i in self.__Lplayers:
                                            d1 = d['name']
                                            ff=self.__Lplayers[cp-1]['name']
                                            i['log'].append(f'{d1} wins the challenge, {JA} assassinated {ff}')
                                        asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Assassination()
                                        self.__Lplayers[cp-1] = asse[1]
                            else:
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                                asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Assassination()
                                for i in self.__Lplayers:
                                    ff=self.__Lplayers[cp-1]['name']
                                    i['log'].append(f'{JA} assessinated {ff} ')
                                self.__Lplayers[cp-1] = asse[1]
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                i['log'].append(f'{d1} wins challenge ')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turn] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                else:
                    print("Not enough coins to use assessination, press any key to go back")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turn).game()






           
            if selection == 6:
                print(JA,"has used Steal")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(self.__Lplayers[self.__turn])
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_c(self.__Lplayers[self.__turn])
                    if c == False:
                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                        for i in self.__Lplayers:
                            cp1 = self.__Lplayers[cp-1]['name']
                            i['log'].append(f'{JA} stealed from {cp1}')
                        nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Steal()
                        self.__Lplayers[self.__turn]= nd[1]
                        self.__Lplayers[cp-1] = nd[0]
                    else:
                        for i in self.__Lplayers:
                            c1 = c['name']
                            i['log'].append(f'{c1} blocks Steal ')
                        print(self.__Lplayers[self.__turn]['name']," has been blocked by ",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(c)
                        if d == False:
                            print("nobody challenges the block")
                            pass
                        else:
                            for i in self.__Lplayers:
                                d1 = d['name']
                                c1 = c['name']
                                i['log'].append(f'{d1} challenges {c1} ')
                            a = Interventions(c,d,self.__Maze).Special_challenge()
                            if a[3] == 0: 
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
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    cp1 = self.__Lplayers[cp-1]['name']
                                    i['log'].append(f'{d1} wins the challenge, {JA} steals from {cp1} ')
                                nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Steal()
                                self.__Lplayers[self.__turn]= nd[1]
                                self.__Lplayers[cp-1] = nd[0]
                else: 
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenged {JA} ')
                    a = Interventions(self.__Lplayers[self.__turn],d,self.__Maze).Special_challenge()                        
                    if a[3] == 0: 
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_c(self.__Lplayers[self.__turn])
                        if c != False: 
                            for i in self.__Lplayers:
                                c1 = c['name']
                                i['log'].append(f'{c1} blocked Steal ')
                            print(self.__Lplayers[self.__turn]['name'],"has been blocked by ",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(c)
                            if d == False:
                                print("nobody challenges the block")
                                pass
                            else:
                                for i in self.__Lplayers:
                                    d1 = d['name']
                                    c1 = c['name']
                                    i['log'].append(f'{d1} challenged {c1} block ')
                                a = Interventions(c,d,self.__Maze).Special_challenge()
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
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                                    for i in self.__Lplayers:
                                        d1 = d['name']
                                        cp1 = self.__Lplayers[cp-1]['name']
                                        i['log'].append(f'{d1} wins challenge, {JA} steals from {cp1} ')
                                    nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Steal()
                                    self.__Lplayers[self.__turn]= nd[1]
                                    self.__Lplayers[cp-1] = nd[0]
                        else:

                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turn).chose_player()
                            nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turn],self.__Maze).Steal()
                            for i in self.__Lplayers:
                                cp1 = self.__Lplayers[cp-1]['name']
                                i['log'].append(f'{JA} steals from {cp1} ')
                            self.__Lplayers[self.__turn]= nd[1]
                            self.__Lplayers[cp-1] = nd[0]
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins challenge, Steal not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
            
            
            if selection == 7:
                print(JA," used Exchange")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Exchange ')
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turn).Question_d(self.__Lplayers[self.__turn])
                if d == 0:
                    change = Actions(" ",self.__Lplayers[self.__turn],self.__Maze).Exchange()
                    self.__Lplayers[self.__turn] = change[0]
                    self.__Maze = change[1]
                else:
                    for i in self.__Lplayers:
                        d1 = d['name']
                        i['log'].append(f'{d1} challenges {JA} ')
                    a = Interventions(self.__Lplayers[self.__turn],d,self.__Maze).Challenge('Ambassador')
                    if a[3] == 0:
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        change = Actions('',self.__Lplayers[self.__turn],self.__Maze).Exchange()
                        self.__Lplayers[self.__turn] = change[0]
                        self.__Maze = change[1]
                    else:
                        for i in self.__Lplayers:
                            d1 = d['name']
                            i['log'].append(f'{d1} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turn] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]

            self.__Lplayers[self.__turn]['log']=[]
            self.__turn += 1
            if self.__turn > len(self.__Lplayers)-1:
                self.__turn = 0
            while self.__Lplayers[self.__turn]['influence'] <= 0:
                self.__turn += 1
                if self.__turn > len(self.__Lplayers)-1:
                    self.__turn = 0
            Start_Game(self.__Maze,self.__Lplayers,self.__turn).game()


        if selection == 2:
            print(self.__Lplayers[self.__turn]["cards"])
            print('press any key to continue')
            input()
            Start_Game(self.__Maze,self.__Lplayers,self.__turn).game()
        

        if selection == 3:
            for i in self.__Lplayers[self.__turn]["log"]:
                print(i)
            print('press any key to continue')
            input()
            Start_Game(self.__Maze,self.__Lplayers,self.__turn).game()

