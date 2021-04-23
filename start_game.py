from numpy import *
from crerebro import *
from Acciones import *
from intervenciones import *

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

        JA = self.__Lplayers[self.__turno]["name"] #acceder al nombre del jugador actual
        print('\n',"turno de: ",JA)
        selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_menu()
        if selection == 1:
            
            
            
            if self.__Lplayers[self.__turno]["coins"] >= 10:
                print("Tienes 10 o mas monedas, debes hacer coup")
                c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Golpe()
                self.__Lplayers[self.__turno]['coins'] = coup[0]
                self.__Lplayers[c-1] = coup[1]
            
           
           
           
            if selection == 1:#ingresos
                print('El jugador ',self.__Lplayers[self.__turno]['name'],"ha usado 'Ingresos'(+1 moneda)")
                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ingreso()
                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
            
            
            
            if selection == 2:#ayuda extranjera
                print('El jugador ',self.__Lplayers[self.__turno]['name'],"ha usado 'Ayuda Extranjera'")
                d =False
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                    if c == False:
                        nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ayuda_Extrangera()
                        self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                    else:
                        print(self.__Lplayers[self.__turno]['name'],"has sido contraatacado por",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                        if d == False:
                            print("Nadie desafio el contraataque")
                            pass
                        else:
                            a = Intervenciones(c,d,self.__Maze).Desafio('Duke')
                            if a[3] == 0: #gana c
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
                                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ayuda_Extrangera()
                                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                                

    
           
           
           
            if selection == 3:#golpe
                if self.__Lplayers[self.__turno]["coins"] >= 7:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                    coup = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Golpe()
                    self.__Lplayers[self.__turno]['coins'] = coup[0]
                    self.__Lplayers[c-1] = coup[1]
                else:
                    print("No tienes monedas suficientes para hacer coup, aprete cualquier tecla para volver al menu")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
            
            
            
            
            if selection == 4:#impuesto
                print(JA,"juega Duke")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == 0:
                    nd = Actions(" ",self.__Lplayers[self.__turno],self.__Maze).Tax()
                    self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                else:
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Duke')
                    if a[3] == 0: #gana JA
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Tax()
                        self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
                    else: #gana d
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]


            
            if selection == 5:#asesino


                if self.__Lplayers[self.__turno]["coins"] >= 3:
                    print(JA,"ha usado asesino")
                    self.__Lplayers[self.__turno]['coins'] += -3
                    d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                    if d == False:
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                        if c == False:
                            cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                            asse = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                            self.__Lplayers[cp-1] = asse[1]
                        else:
                            print(self.__Lplayers[self.__turno]['name'],"has sido contraatacado por",c["name"])
                            d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                            if d == False:
                                print("Nadie desafio el contraataque")
                                pass
                            else:
                                a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                if a[3] == 0: #gana c
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
                                    self.__Lplayers[cp-1] = asse[1]
                    else: 
                        a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Assassin')
                        if a[3] == 0: #gana JA
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                            c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                            if c!= False:
                                print(self.__Lplayers[self.__turno]['name'],"has sido contraatacado por",c["name"])
                                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                                if d == False:
                                    print("Nadie desafio el contraataque")
                                    
                                else:
                                    a = Intervenciones(c,d,self.__Maze).Desafio('Contessa')
                                    if a[3] == 0: #gana c
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
                                        self.__Lplayers[cp-1] = asse[1]
                        else: #gana d
                            self.__Maze = a[2]
                            self.__Lplayers[self.__turno] = a[0]
                            ind = self.__Lplayers.index(d) 
                            self.__Lplayers[ind] = a[1]
                else:
                    print("No tienes monedas suficientes para hacer asesinato, aprete cualquier tecla para volver al menu")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()






           
            if selection == 6:#extorsion
                print(JA,"ha usado capitan")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == False:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                    if c == False:
                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                        nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                        self.__Lplayers[self.__turno]= nd[1]
                        self.__Lplayers[cp-1] = nd[0]
                    else:
                        print(self.__Lplayers[self.__turno]['name'],"has sido contraatacado por",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                        if d == False:
                            print("Nadie desafio el contraataque")
                            pass
                        else:
                            a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                            if a[3] == 0: #gana c
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
                                nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                self.__Lplayers[self.__turno]= nd[1]
                                self.__Lplayers[cp-1] = nd[0]
                else: 
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio_esp()                        
                    if a[3] == 0: #gana JA
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_c(self.__Lplayers[self.__turno])
                        print(self.__Lplayers[self.__turno]['name'],"has sido contraatacado por",c["name"])
                        d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(c)
                        if d == False:
                            print("Nadie desafio el contraataque")
                            pass
                        else:
                            a = Intervenciones(c,d,self.__Maze).Desafio_esp()
                            if a[3] == 0: #gana c
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
                                nd=Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Extorison()
                                self.__Lplayers[self.__turno]= nd[1]
                                self.__Lplayers[cp-1] = nd[0]
                    else: #gana d
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
            
            
            if selection == 7:#Cambio
                print(JA,"juega Embajador")
                d = Start_Game(self.__Maze,self.__Lplayers,self.__turno).pregunta_d(self.__Lplayers[self.__turno])
                if d == 0:
                    cambio = Actions(" ",self.__Lplayers[self.__turno],self.__Maze).Cambio()
                    self.__Lplayers[self.__turno] = cambio[0]
                    self.__Maze = cambio[1]
                else:
                    a = Intervenciones(self.__Lplayers[self.__turno],d,self.__Maze).Desafio('Ambassador')
                    if a[3] == 0: #gana JA
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]
                        cp = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                        cambio = Actions(self.__Lplayers[cp-1],self.__Lplayers[self.__turno],self.__Maze).Cambio()
                        self.__Lplayers[cp-1] = cambio[0]
                        self.__Lplayers[self.__turno] = cambio[1]
                    else: #gana d
                        self.__Maze = a[2]
                        self.__Lplayers[self.__turno] = a[0]
                        ind = self.__Lplayers.index(d) 
                        self.__Lplayers[ind] = a[1]

            self.__turno += 1
            if self.__turno > len(self.__Lplayers)-1:
                self.__turno = 0
            while self.__Lplayers[self.__turno]['influence'] <= 0:#hay que cambiar esto porque ir subiendo el numero del turno no va a aumentar la influencia del jugador del turno, entonces le suma 1 infinitamente hasta salirse del rango
                if self.__Lplayers[self.__turno]['influence'] <= 0:
                
                    self.__turno += 1
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()

        if selection == 2:
            print(self.__Lplayers[self.__turno]["cards"]) #acceder a cartas del jugador actual
            Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()
        

        #if selection == 3: #ver log
