from Acciones import *
from crerebro import *





class Intervenciones(Actions):
    def __init__(self,D_acusado,D_acusador,deck):
        self.__D_acusado = D_acusado
        self.__D_acusador = D_acusador
        self.__deck = deck
    

    def Desafio (self,card):
        print(self.__D_acusado["name"],'''has been challenge''',self.__D_acusador["name"],
        '''Press any key to see your cards''')
        input()
        
        
        for i in range(self.__D_acusado["influence"]):
            print("card ",i+1,' ',self.__D_acusado["cards"][i])

        print('Chose the number of the card to flip')
        
        carta_volteada= int(input())-1
        print('\n''\n''\n''\n''\n','Player ',self.__D_acusado["name"]
            ,' has fliped the card ',self.__D_acusado["cards"][carta_volteada])

        if self.__D_acusado["cards"][carta_volteada] == card:
            DM=Brain(self.__deck,self.__D_acusado).Deposit_cards(self.__D_acusado["cards"][carta_volteada])
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_acusado).Take_cards()
            self.__D_acusado=DM[0]
            self.__deck=DM[1]


            print(self.__D_acusador["name"],''' lost the challenge. 
            Press any key to see your cards''')
            input()
        
            for i in range(self.__D_acusador["influence"]):
                print("card ",i+1,' ',self.__D_acusador["cards"][i])

            print('Chose the number of the card to flip')
        
            carta_volteada= int(input())-1

            DM=Brain(self.__deck,self.__D_acusador).Lost_card(carta_volteada)
            self.__D_acusador=DM


            return [self.__D_acusado,self.__D_acusador,self.__deck,0]
            


            
        else:
            print(self.__D_acusado["name"],''' has lost the challenge''')

            DM=Brain(self.__deck,self.__D_acusado).Lost_card(carta_volteada)
            self.__D_acusado=DM

            return[self.__D_acusado,self.__D_acusador,self.__deck,1]#si termina en 0 el desafiado gana y si termina en 1 el desafiante gana


    def Desafio_esp(self):
        print(self.__D_acusado["name"],'''has been challenge ''',self.__D_acusador["name"],
        '''Press any key to see your cards''')
        input()
        
        
        for i in range(self.__D_acusado["influence"]):
            print("card ",i+1,' ',self.__D_acusado["cards"][i])

        print('Chose the number of the card to flip')
        
        carta_volteada= int(input())-1
        print('\n''\n''\n''\n''\n','player ',self.__D_acusado["name"]
            ,' has fliped the card ',self.__D_acusado["cards"][carta_volteada])

        if self.__D_acusado["cards"][carta_volteada] == 'Captain':
            # DM=Brain(self.__deck,self.__D_acusado).Deposit_cards(carta_volteada) crashea aqui
            DM=Brain(self.__deck,self.__D_acusado).Deposit_cards(self.__D_acusado["cards"][carta_volteada]) #entrega nombre a depositcard en crerebro
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_acusado).Take_cards()
            self.__D_acusado=DM[0]
            self.__deck=DM[1]


            print(self.__D_acusador["name"],'''has lost challenge. 
            Press any key to see your cards''')
            input()
        
            for i in range(self.__D_acusador["influence"]):
                print("card ",i+1,' ',self.__D_acusador["cards"][i])

            print('Chose the number of the card to flip')
        
            carta_volteada= int(input())-1

            DM=Brain(self.__deck,self.__D_acusador).Lost_card(carta_volteada)
            self.__D_acusador=DM


            return [self.__D_acusado,self.__D_acusador,self.__deck,0]
            


            
        else:
            print(self.__D_acusado["name"],'''has lost the challenge''')

            DM=Brain(self.__deck,self.__D_acusado).Lost_card(carta_volteada)
            self.__D_acusado=DM

            return[self.__D_acusado,self.__D_acusador,self.__deck,1]