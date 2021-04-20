from numpy import *

class Deck:
    def __init__(self,deck):
        self.__deck=deck


    def shuffle(self):
        random.shuffle(self.__deck)
        return self.__deck


    
   ''' @property
    def sdeck(self):
        print('pasa por property')
        return self.__deck

    @sdeck.setter
    def sdeck(self,listarandom):
        print('entro al setter')
        self.__deck=listarandom'''







