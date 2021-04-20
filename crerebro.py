from numpy import *





class Brain:
    def __init__(self,Deck,diccionario):
        self.__Deck = Deck
        self.__diccionario = diccionario

    def Change_coins (self,operation,amount):
        if operation=='+':
            self.__diccionario['coins']+=int(amount)




        if operation=='-':
            self.__diccionario['coins']+= int(amount)*-1
        return self.__diccionario

    def Deposit_cards(self,card):
        carta_retirada=self.__diccionario['cards'][card]

        self.__Deck.append(carta_retirada)

        self.__diccionario['cards'].pop(card)
        
        random.shuffle(self.__Deck)

        return [self.__diccionario,self.__Deck]









    def Take_cards(self,amount):