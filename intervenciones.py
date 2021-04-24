from Acciones import *
from crerebro import *





class Interventions(Actions):
    def __init__(self,D_accusated,D_accusator,deck):
        self.__D_accusated = D_accusated
        self.__D_accusator = D_accusator
        self.__deck = deck
    

    def Challenge (self,card):
        print(self.__D_accusated["name"],'''has been challenge''',self.__D_accusator["name"],
        '''Press any key to see your cards''')
        input()
        
        
        for i in range(self.__D_accusated["influence"]):
            print("card ",i+1,' ',self.__D_accusated["cards"][i])

        print('Chose the number of the card to flip')
        
        fliped_card= int(input())-1
        print('\n''\n''\n''\n''\n','Player ',self.__D_accusated["name"]
            ,' has fliped the card ',self.__D_accusated["cards"][fliped_card])

        if self.__D_accusated["cards"][fliped_card] == card:
            DM=Brain(self.__deck,self.__D_accusated).Deposit_cards(self.__D_accusated["cards"][fliped_card])
            self.__D_accusated=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_accusated).Take_cards()
            self.__D_accusated=DM[0]
            self.__deck=DM[1]


            print(self.__D_accusator["name"],''' lost the challenge. 
            Press any key to see your cards''')
            input()
        
            for i in range(self.__D_accusator["influence"]):
                print("card ",i+1,' ',self.__D_accusator["cards"][i])

            print('Chose the number of the card to flip')
        
            fliped_card= int(input())-1

            DM=Brain(self.__deck,self.__D_accusator).Lost_card(fliped_card)
            self.__D_accusator=DM


            return [self.__D_accusated,self.__D_accusator,self.__deck,0]
            


            
        else:
            print(self.__D_accusated["name"],''' has lost the challenge''')

            DM=Brain(self.__deck,self.__D_accusated).Lost_card(fliped_card)
            self.__D_accusated=DM

            return[self.__D_accusated,self.__D_accusator,self.__deck,1]


    def Special_challenge(self):
        print(self.__D_accusated["name"],'''has been challenge ''',self.__D_accusator["name"],
        '''Press any key to see your cards''')
        input()
        
        
        for i in range(self.__D_accusated["influence"]):
            print("card ",i+1,' ',self.__D_accusated["cards"][i])

        print('Chose the number of the card to flip')
        
        fliped_card= int(input())-1
        print('\n''\n''\n''\n''\n','player ',self.__D_accusated["name"]
            ,' has fliped the card ',self.__D_accusated["cards"][fliped_card])

        if self.__D_accusated["cards"][fliped_card] == 'Captain':
            
            DM=Brain(self.__deck,self.__D_accusated).Deposit_cards(self.__D_accusated["cards"][fliped_card]) 
            self.__D_accusated=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_accusated).Take_cards()
            self.__D_accusated=DM[0]
            self.__deck=DM[1]


            print(self.__D_accusator["name"],'''has lost challenge. 
            Press any key to see your cards''')
            input()
        
            for i in range(self.__D_accusator["influence"]):
                print("card ",i+1,' ',self.__D_accusator["cards"][i])

            print('Chose the number of the card to flip')
        
            fliped_card= int(input())-1

            DM=Brain(self.__deck,self.__D_accusator).Lost_card(fliped_card)
            self.__D_accusator=DM


            return [self.__D_accusated,self.__D_accusator,self.__deck,0]
            


            
        else:
            print(self.__D_accusated["name"],'''has lost the challenge''')

            DM=Brain(self.__deck,self.__D_accusated).Lost_card(fliped_card)
            self.__D_accusated=DM

            return[self.__D_accusated,self.__D_accusator,self.__deck,1]