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
    
    def print_menu(self): #Menu Turno
        print("")
        for i in self.__Lplayers:
            if i["influence"] > 0 :
                print(i["name"],"Cartas:", len(i["cards"]), "Cartas Perdidas:",i["lostcards"],
                "Monedas:",i["coins"],"Influencia:",i["influence"])
        print("")
        print("Selecione que quiere hacer: ")
        print("1. Ejecutar una accion")
        print("2. Ver mis cartas")
        print("3. Ver log")
        return int(input())

    def print_actions(self):
        print('\nSelecciona una opcion:')
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
            print(LV[0]["name"],'HAS GANADO') 
            sys.exit()
        print("Elige un jugador al que le quieras ejecutar la accion:")
        
        
        for i in self.__Lplayers:
            if i["influence"] > 0:
                print(a,". ",i["name"],"Cartas:", len(i["cards"]), "Cartas Perdidas:",i["lostcards"],
                "Monedas:",i["coins"],"Influencia:",i["influence"])
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
                print(i['name'],'oprime 1 para desafiar, 2 para no hacer nada')
                n = int(input())
                L.append([i,n])
        for k in L:
            if k[1] == 1: # 1 = desafio
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
                print(i['name'],'oprime 1 para contraacar, 2 para no hacer nada')
                n = int(input())
                L.append([i,n])
        for k in L:
            if k[1] == 1: # 1 = desafio
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
            print(LV[0]["name"],'HAS GANADO') 
            sys.exit()
            #SI ROMPE EL JUEGO HASTA AHORA

        JA = self.__Lplayers[self.__turno]["name"] #acceder al nombre del jugador actual
        print('\n',"turno de: ",JA)
        selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_menu()
        
        for i in self.__Lplayers:
            i['log'].append(f'{JA}`s turn has started ')
        
        
        if selection == 1:
            
            
            
            if self.__Lplayers[self.__turno]["coins"] >= 10:
                print("Tienes 10 o mas monedas, debes hacer coup")
                c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Golpe()
                self.__Lplayers[self.__turno]['coins'] = coup[0]
                self.__Lplayers[c-1] = coup[1]
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has been forced to use Coup on {self.__Lplayers[c-1]}')
                
            
           
            selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_actions()
           
            if selection == 1:#ingresos
                print('El jugador ',self.__Lplayers[self.__turno]['name'],"ha usado 'Ingresos'(+1 moneda)")
                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ingreso()
                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Income ')
            
            
            if selection == 2:#ayuda extranjera
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
                        self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                    else:
                        for i in self.__Lplayers:
                            i['log'].append("f'{c['name']} Blocked Foreign Aid from {JA}'")
                        print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)

                        if d == False:
                            print("Nobody challenged the Block ")
                            pass
                        else:
                            for i in self.__Lplayers:
                                i['log'].append(f'{d['name']} has Challenged {c['name']} Block ')
                            a = Intervenciones(c,d,self.__Maze).Desafio('Duke')
                            if a[3] == 0: #gana c
                                for i in self.__Lplayers:
                                    i['log'].append(f'{c['name']} wins challenge ')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]

                            else: #gana d
                                for i in self.__Lplayers:
                                    i['log'].append(f'{d['name']} wins challenge ')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                                for i in self.__Lplayers:
                                    i['log'].append(f'{JA} has executed Foreign Aid successfully ')
                                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ayuda_Extrangera()
                                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                                

    
           
           
           
            if selection == 3:#golpe
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
            
            
            
            
            if selection == 4:#impuesto
                print(JA,"has used Tax")
                for i in self.__Lplayers:
                    i['log'].append(f'{JA} has used Tax ')
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == False:
                    nd = Actions(" ",self.__Lplayers[self.__turno],self.__Maze).Tax()
                    self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                    for i in self.__Lplayers:
                        i['log'].append(f'{JA} has executed Tax successfully ')
                else:
                    for i in self.__Lplayers:
                        i['log'].append(f'{d['name']} challenged {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Duke')
                    if a[3] == 0: #gana JA
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge and executed Tax successfully ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Tax()
                        self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                    else: #gana d
                        for i in self.__Lplayers:
                            i['log'].append(f'{d['name']} wins the challenge Tax not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]


            
            if selection == 5:#asesino


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
                                i['log'].append(f'{c['name']} has blocked Assassination ')
                            print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                            if d == False:
                                print("Assassination has been blocked")
                                
                                pass
                            else:
                                for i in self.__Lplayers:
                                    i['log'].append(f'{d['name']} challenged {c['name']}`s block ')
                                a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                if a[3] == 0: #gana c
                                    for i in self.__Lplayers:
                                        i['log'].append(f'{c{'name'}} wins challenge Assassination not executed')
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                else: #gana d
                                    
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                    asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                    for i in self.__Lplayers:
                                        i['log'].append(f'{d['name']} wins challenge and {JA} Assassinates {self.__Lplayers[cp-1]}')
                                    self.__Lplayers[cp-1] = asse[1]
                    else: 
                        for i in self.__Lplayers:
                            i['log'].append(f'{d['name']} challenges Assassination ')
                        a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Assassin')
                        if a[3] == 0: #gana JA
                            for i in self.__Lplayers:
                                i['log'].append(f'{JA} wins challenge')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                            c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                            if c!= False: #contraatacan al JA despues de desafiar al JA y ganar JA
                                for i in self.__Lplayers:
                                    i['log'].append(f'{c['name']} blocks Assassination ')
                                print(self.__Lplayers[self.__turno]['name'],"has been blocked by",c["name"])
                                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                                if d == False:
                                    print("nobody challenges the block")
                                    
                                else:
                                    for i in self.__Lplayers:
                                        i['log'].append(f'{d['name']} challenges {c['name']}`s block ')
                                    a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                    if a[3] == 0: #gana c
                                        for i in self.__Lplayers:
                                            i['log'].append(f'{c['name']} wins the challenge ')
                                        self.__Maze = a[2]
                                        ind = self.__Lplayers.index(c) 
                                        self.__Lplayers[ind] = a[0]
                                        ind = self.__Lplayers.index(d) 
                                        self.__Lplayers[ind] = a[1]
                                    else: #gana d
                                        
                                        self.__Maze = a[2]
                                        ind = self.__Lplayers.index(c) 
                                        self.__Lplayers[ind] = a[0]
                                        ind = self.__Lplayers.index(d) 
                                        self.__Lplayers[ind] = a[1]
                                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                        for i in self.__Lplayers:
                                            i['log'].append(f'{d['name']} wins the challenge, {JA} assassinated {self.__Lplayers[cp-1]}')
                                        asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                        self.__Lplayers[cp-1] = asse[1]
                            else: #nadie contraataca al asesinato despues de desafiar y ganar asesinato por lo tanto se ejecuta la accion
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                                for i in self.__Lplayers:
                                    i['log'].append(f'{JA} assessinated {self.__Lplayers[cp-1]} ')
                                self.__Lplayers[cp-1] = asse[1]
                        else: #gana d
                            for i in self.__Lplayers:
                                i['log'].append(f'{d['name']} wins challenge ')
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                else:
                    print("No tienes monedas suficientes para hacer asesinato, aprete cualquier tecla para volver al menu")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()






           
            if selection == 6:#extorsion
                print(JA,"has used Steal")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                    if c == False:
                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} stealed from {self.__Lplayers[cp-1]}')
                        nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                        self.__Lplayers[self.__turno]= nd[1]
                        self.__Lplayers[cp-1] = nd[0]
                    else:
                        for i in self.__Lplayers:
                            i['log'].append(f'{c['name']} blocks Steal ')
                        print(self.__Lplayers[self.__turno]['name']," has been blocked by ",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                        if d == False:
                            print("nobody challenges the block")
                            pass
                        else:
                            for i in self.__Lplayers:
                                i['log'].append(f'{d['name']} challenges {c['name']} ')
                            a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                            if a[3] == 0: #gana c
                                for i in self.__Lplayers:
                                    i['log'].append(f'{c['name']} wins challenge, Stealing not executed')
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                            else: #gana d
                                
                                self.__Maze = a[2]
                                ind = self.__Lplayers.index(c) 
                                self.__Lplayers[ind] = a[0]
                                ind = self.__Lplayers.index(d) 
                                self.__Lplayers[ind] = a[1]
                                cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                for i in self.__Lplayers:
                                    i['log'].append(f'{d['name']} wins the challenge, {JA} steals from {self.__Lplayers[cp-1]} ')
                                nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                self.__Lplayers[self.__turno]= nd[1]
                                self.__Lplayers[cp-1] = nd[0]
                else: 
                    for i in self.__Lplayers:
                        i['log'].append(f'{d['name']} challenged {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio_esp()                        
                    if a[3] == 0: #gana JA
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]

                        #creo que no hay que igualar la linea de arriba porque el jugador
                        #que juega capitan y lo desafian y gana, pierde de su mano capitan
                        #siendo que todavia lo pueden contra atacar y si pierde el contraataque
                        #su mano ya no tendria capitan, sino otra

                        #si me contraatacan capitan y pierdo el contra ataque, pierdo cualquier carta?
                        #o pierdo capitan o no pierdo ninguna?

                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                        if c != False: #faltaba esto para ver si contraatacaban sino tiraba error
                            for i in self.__Lplayers:
                                i['log'].append(f'{c['name']} blocked Steal ')
                            print(self.__Lplayers[self.__turno]['name'],"has been blocked by ",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                            if d == False:
                                print("nobody challenges the block")
                                pass
                            else:
                                for i in self.__Lplayers:
                                    i['log'].append(f'{d['name']} challenged {c['name']}`s block ')
                                a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                                if a[3] == 0: #gana c
                                    for i in self.__Lplayers:
                                        i['log'].append(f'{c['name']} wins challenge, Steal not executed ')
                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                else: #gana d

                                    self.__Maze = a[2]
                                    ind = self.__Lplayers.index(c) 
                                    self.__Lplayers[ind] = a[0]
                                    ind = self.__Lplayers.index(d) 
                                    self.__Lplayers[ind] = a[1]
                                    cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                                    for i in self.__Lplayers:
                                        i['log'].append(f'{d['name']} wins challenge, {JA} steals from {self.__Lplayers[cp-1]} ')
                                    nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                    self.__Lplayers[self.__turno]= nd[1]
                                    self.__Lplayers[cp-1] = nd[0]
                        else: #nadie contraataca

                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                            nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                            for i in self.__Lplayers:
                                i['log'].append(f'{JA} steals from {self.__Lplayers[cp-1]} ')
                            self.__Lplayers[self.__turno]= nd[1]
                            self.__Lplayers[cp-1] = nd[0]
                    else: #gana d
                        for i in self.__Lplayers:
                            i['log'].append(f'{d['name']} wins challenge, Steal not executed ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
            
            
            if selection == 7:#Cambio
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
                    i['log'].append(f'{d['name']} challenges {JA} ')
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Ambassador')
                    if a[3] == 0: #gana JA
                        for i in self.__Lplayers:
                            i['log'].append(f'{JA} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        #cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player() deberia estar demas esto
                        #cambio = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Cambio() el self.__Lplayers[cp-1] debria estar demas
                        cambio = Actions('',self.__Lplayers[self.__turno],self.__Maze).Cambio()
                        #self.__Lplayers[cp-1] = cambio[0] esto retornar dic con cartas cambiadas
                        self.__Lplayers[self.__turno] = cambio[0]
                        #self.__Lplayers[self.__turno] = cambio[1] esto retornar maso de cartas
                        self.__Maze = cambio[1]
                    else: #gana d
                        for i in self.__Lplayers:
                            i['log'].append(f'{d['name']} wins the challenge ')
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]

#            self.__turno += 1
 #           if self.__turno > len(self.__Lplayers)-1:
  #              self.__turno = 0
   #         while self.__Lplayers[self.__turno]['influence'] <= 0:#hay que cambiar esto porque ir subiendo el numero del turno no va a aumentar la influencia del jugador del turno, entonces le suma 1 infinitamente hasta salirse del rango
    #            if self.__Lplayers[self.__turno]['influence'] <= 0:
     #               if self.__turno > len(self.__Lplayers)-1:
      #                  self.__turno = -1
       #             self.__turno += 1
#
 #           Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()''' 


            self.__Lplayers[self.__turno]['log']=[]
            self.__turno += 1
            if self.__turno > len(self.__Lplayers)-1:
                self.__turno = 0
            while self.__Lplayers[self.__turno]['influence'] <= 0:
                self.__turno += 1
                if self.__turno > len(self.__Lplayers)-1:
                    self.__turno = 0
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
            #lo que teniamos antes

        if selection == 2:
            print(self.__Lplayers[self.__turno]["cards"]) #acceder a cartas del jugador actual
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
        

        if selection == 3: #ver log
             print(self.__Lplayers[self.__turno]["log"])
             Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()

