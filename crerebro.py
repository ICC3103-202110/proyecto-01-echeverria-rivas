from numpy import *


class Brain:
    def __init__(self,Deck,dictionary):
        self.__Deck = Deck
        self.__dictionary = dictionary

    @property
    def dictionary(self):
        return self.__dictionary

    @dictionary.setter
    def dictionary(self,value):
        self.__dictionary['coins'] = value
        if self.__dictionary['coins'] < 0:
            self.__dictionary['coins'] = 0

    @dictionary.setter
    def dictionary(self,value):
        self.__dictionary['influence'] = value
        if self.__dictionary['influence'] < 0:
            self.__dictionary['influence'] = 0


    def Change_coins (self,operation,amount):
        if operation=='+':
            self.__dictionary['coins']+=int(amount)
        if operation=='-':
            self.__dictionary['coins']+= int(amount)*-1
        return self.__dictionary['coins']

    def Deposit_cards(self,card):
        self.__dictionary['cards'].index(card)
        carta_retirada=self.__dictionary['cards'][self.__dictionary['cards'].index(card)]

        self.__Deck.append(carta_retirada)

        self.__dictionary['cards'].pop(self.__dictionary['cards'].index(card))
        
        random.shuffle(self.__Deck)

        return [self.__dictionary,self.__Deck]




    def Take_cards(self):
        taken_card=self.__Deck[0]

        self.__dictionary['cards'].append(taken_card)

        self.__Deck.pop(0)
        
        random.shuffle(self.__Deck)

        return [self.__dictionary,self.__Deck]

    def Lost_card(self,card):
        self.__dictionary['lostcards'].append(self.__dictionary['cards'][card])
        self.__dictionary['cards'].pop(card)
        self.__dictionary['influence']+= -1
        return self.__dictionary

    





    