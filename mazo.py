from numpy import *

class Deck:
    def __init__(self,deck):
        self.__deck=deck


    def shuffle(self):
        random.shuffle(self.__deck)
        return self.__deck