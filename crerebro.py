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
        return self.__diccionario['coins']

    def Deposit_cards(self,card):
        carta_retirada=self.__diccionario['cards'][card]

        self.__Deck.append(carta_retirada)

        self.__diccionario['cards'].pop(card)
        
        random.shuffle(self.__Deck)

        return [self.__diccionario,self.__Deck]




    def Take_cards(self):
        carta_tomada=self.__Deck[0]

        self.__diccionario['cards'].append(carta_tomada)

        self.__Deck.pop(0)
        
        random.shuffle(self.__Deck)

        return [self.__diccionario,self.__Deck]

    def Lost_card(self,card):
        self.__diccionario['lostcards'].append(self.__diccionario['cards'][card])
        self.__diccionario['cards'].pop(card)
        self.__diccionario['influence']+= -1
        return self.__diccionario