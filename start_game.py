from numpy import *
from crerebro import *

class Start_Game:
    def __init__(self,Maze,Lplayers,turno):
        self.__Maze = Maze
        self.__Lplayers = Lplayers
        self.__turno = 0
    
    def print_menu(self): #Menu Turno
        print("")
        for i in self.__Lplayers:
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
            print(a,". ",i["name"],"Cartas:", len(i["cards"]), "Cartas Perdidas:",i["lostcards"],
             "Monedas:",i["coins"],"Influencia:",i["influence"])
            a+=1
        return int(input())

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
            selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_actions()
           
           
           
            if selection == 1:#ingresos
                print('El jugador ',self.__Lplayers[self.__turno],"ha usado 'Ingresos'(+1 moneda)")
                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Ingreso()
                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
            
            
            
            if selection == 2:#ayuda extranjera
                print('El jugador ',self.__Lplayers[self.__turno],"ha usado 'Ayuda Extranjera'(+1 moneda)")


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
                nd = Actions("",self.__Lplayers[self.__turno],self.__Maze).Tax()
                self.__Lplayers[self.__turno]['coins'] = nd #cambio de moneda del jugador de turno
            
            
            if selection == 5:#asesino


                if self.__Lplayers[self.__turno]["coins"] >= 3:
                    c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
                    asse = Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Asesino()
                    self.__Lplayers[self.__turno]['coins'] = asse[0]
                    self.__Lplayers[c-1] = asse[1]
                else:
                    print("No tienes monedas suficientes para hacer asesinato, aprete cualquier tecla para volver al menu")
                    input()
                    Start_Game(self.__Maze,self.__Lplayers,self.__turno).game()






           
            if selection == 6:#extorsion
            nd=Actions("",self.__Lplayers[self.turno],self.__Maze).Extorison()
            self.__Lplayers[self.__turno]= nd[0]
            self.__Maze=nd[1]
            
            
            if selection == 7:#Cambio

            c = Start_Game(self.__Maze,self.__Lplayers,self.__turno).chose_player()
            extorsion=Actions(self.__Lplayers[c-1],self.__Lplayers[self.__turno],self.__Maze).Cambio()
            self.__Lplayers[c-1]=extorsion[0]
            self.__Lplayers[self.__turno]=extorsion[1]




            
            if self.__turno +1 <= len(self.__Lplayers):
                self.__turno += 1
            else:
                self.__turno = 0
        
        
        
        if selection == 2:
            print(self.__Lplayers[self.__turno]["cards"]) #acceder a cartas del jugador actual




























