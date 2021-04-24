from mazo import *

class Player:
    def __init__(self, name):
        self.__name = name
    
    def Dic(self):
        D = {"name": self.__name , "cards":[], "coins":2, "log":[], "influence":2, "lostcards":[]}
        return D

    def create_player(self,L,J): 
        for i in range(J):
            print("Write player #",i+1,"name: ")
            name = input()
            aux=Player(name).Dic()
            
            L.append(aux)
        return L