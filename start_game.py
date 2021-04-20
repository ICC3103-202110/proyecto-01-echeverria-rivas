from numpy import *

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

    def game(self):
        JA = self.__Lplayers[self.__turno]["name"] #acceder al nombre del jugador actual
        print('\n',"turno de: ",JA)
        selection = Start_Game(self.__Maze,self.__Lplayers,self.__turno).print_menu()
        if selection == 1:
            pass
            if self.__turno != len(self.__Lplayers):
                self.__turno += 1
            else:
                self.__turno = 0
        if selection == 2:
            print(self.__Lplayers[self.__turno]["cards"]) #acceder a cartas del jugador actual




























