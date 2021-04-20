from numpy import *

class Deck:
    def __init__(self,deck):
        self.__deck=["Duke", "Duke", "Duke", "Assassin", "Assassin", "Assassin", 
        "Captain", "Captain", "Captain", "Ambassador", "Ambassador", "Ambassador", 
        "Contessa", "Contessa", "Contessa"]


    def shuffle(self):
        random.shuffle(self.__deck)
        return self.__deck


    
    @property
    def sdeck(self):
        print('pasa por property')
        return self.__deck

    @sdeck.setter
    def sdeck(self,listarandom):
        print('entro al setter')
        self.__deck=listarandom







