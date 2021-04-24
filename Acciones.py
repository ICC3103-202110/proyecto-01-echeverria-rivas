from crerebro import *


class Actions:
    def __init__(self,D_accused,D_accusator,deck):
        self.__D_accused = D_accused
        self.__D_accusator = D_accusator
        self.__deck = deck
    
    def Income(self):
        self.__D_accusator['coins'] = Brain(self.__deck,self.__D_accusator).Change_coins('+',1)
        return self.__D_accusator['coins']

    def Foreign_aid(self):
        self.__D_accusator['coins'] = Brain(self.__deck,self.__D_accusator).Change_coins('+',2)
        return self.__D_accusator['coins']

    def Coup(self):
        nd = Brain(self.__deck,self.__D_accusator).Change_coins('-',7)
        self.__D_accusator['coins'] = nd
        print(self.__D_accused['name'], "Press to see your cards and chose the one to lose")
        input()
        for i in   range(len(self.__D_accused['cards'])):
            print(i+1,". ",self.__D_accused['cards'][i])
        card = int(input('Chose the one to lose: '))-1
        nda = Brain(self.__deck,self.__D_accused).Lost_card(card)
        self.__D_accused = nda
        return [self.__D_accusator['coins'],self.__D_accused]


    def Tax (self):
        self.__D_accusator['coins'] = Brain(self.__deck,self.__D_accusator).Change_coins('+',3)
        return self.__D_accusator['coins']

   
    def Exchange(self):
        EM= Brain(self.__deck, self.__D_accusator).Take_cards()
        self.__D_accusator=EM[0]
        self.__deck=EM[1]

        EM= Brain(self.__deck, self.__D_accusator).Take_cards()
        self.__D_accusator=EM[0]
        self.__deck=EM[1]
        print("Press any key to see your cards in the hand and chose the one to lose")
        input()
        a=1
        for i in self.__D_accusator['cards']:
            print(a,". ",i)
            a+=1
        card_to_eliminate=int(input("Write the number of the card to eliminate: "))-1

        EM= Brain(self.__deck, self.__D_accusator).Deposit_cards(self.__D_accusator['cards'][card_to_eliminate])
        self.__D_accusator=EM[0]
        self.__deck=EM[1]

        print("Select another card to eliminate")
        
        a=1
        for i in self.__D_accusator['cards']:
            print(a,". ",i)
            a+=1
        card_to_eliminate=int(input("Write the number of the card to eliminate: "))-1

        EM= Brain(self.__deck, self.__D_accusator).Deposit_cards(self.__D_accusator['cards'][card_to_eliminate])
        self.__D_accusator=EM[0]
        self.__deck=EM[1]

        return [self.__D_accusator,self.__deck]



    def Assassination(self):
        print(self.__D_accused['name'], "Press any key to see your cards and chose the one to lose")
        input()
        for i in range(len(self.__D_accused['cards'])):
            print(i+1,". ",self.__D_accused['cards'][i])
        card = int(input('Chose the card to lose: '))-1
        nda = Brain(self.__deck,self.__D_accused).Lost_card(card)
        self.__D_accused = nda
        return [self.__D_accusator['coins'],self.__D_accused]


    def Steal (self):
        x = 0
        if self.__D_accused['coins'] < 2:
            x = int(self.__D_accused['coins'])
            self.__D_accusator['coins']=Brain(self.__deck,self.__D_accusator).Change_coins("+",x)
            self.__D_accused['coins']=Brain(self.__deck,self.__D_accused).Change_coins('-',x)
        else:
            self.__D_accusator['coins']=Brain(self.__deck,self.__D_accusator).Change_coins("+",2)
            self.__D_accused['coins']=Brain(self.__deck,self.__D_accused).Change_coins('-',2)
        return [self.__D_accused,self.__D_accusator]
