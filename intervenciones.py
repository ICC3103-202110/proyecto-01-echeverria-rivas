from Acciones import *
from crerebro import *





class Intervenciones(Actions):
    def __init__(self,D_acusado,D_acusador,deck):
        self.__D_acusado = D_acusado
        self.__D_acusador = D_acusador
        self.__deck = deck
    

    def Desafio (self,card):
        input(print(self.__D_acusado["name"],'''ha sido desafiado. 
            Presione cualquier tecla para ver tus cartas'''))
        
        
        for i in range(self.__D_acusado["influence"]):
            print("carta ",i+1,' ',self.__D_acusado["cards"][i])

        print('seleccione la carta que quiera voltear')
        
        carta_volteada= int(input())-1
        print('\n''\n''\n''\n''\n','jugador ',self.__D_acusado["name"]
            ,' ha volteado la carta ',self.__D_acusado["cards"][carta_volteada])

        if self.__D_acusado["cards"][carta_volteada] == card:
            DM=Brain(self.__deck,self.__D_acusado).Deposit_cards(carta_volteada)
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_acusado).Take_cards()
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            ###############gana acusado###############
            
            





            input(print(self.__D_acusador["name"],'''ha perdido el desafio. 
            Presione cualquier tecla para ver tus cartas'''))
        
        
            for i in range(self.__D_acusador["influence"]):
                print("carta ",i+1,' ',self.__D_acusador["cards"][i])

            print('seleccione la carta que quieres perder')
        
            carta_volteada= int(input())-1

            DM=Brain(self.__deck,self.__D_acusador).Lost_card(carta_volteada)
            self.__D_acusador=DM

            ################# lo que pierde acusador##########

            return [self.__D_acusado,self.__D_acusador,self.__deck,0]
            


            
        else:
            print(self.__D_acusado["name"],'''ha perdido el desafio''')

            DM=Brain(self.__deck,self.__D_acusado).Lost_card(carta_volteada)
            self.__D_acusado=DM

            return[self.__D_acusado,self.__D_acusador,self.__deck,1]#si termina en 0 el desafiado gana y si termina en 1 el desafiante gana


    def Desafio_esp(self):
        input(print(self.__D_acusado["name"],'''ha sido desafiado. 
            Presione cualquier tecla para ver tus cartas'''))
        
        
        for i in range(self.__D_acusado["influence"]):
            print("carta ",i+1,' ',self.__D_acusado["cards"][i])

        print('seleccione la carta que quiera voltear')
        
        carta_volteada= int(input())-1
        print('\n''\n''\n''\n''\n','jugador ',self.__D_acusado["name"]
            ,' ha volteado la carta ',self.__D_acusado["cards"][carta_volteada])

        if self.__D_acusado["cards"][carta_volteada] == 'Ambassador' or self.__D_acusado["cards"][carta_volteada] == 'Captain':
            DM=Brain(self.__deck,self.__D_acusado).Deposit_cards(carta_volteada)
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            DM=Brain(self.__deck,self.__D_acusado).Take_cards()
            self.__D_acusado=DM[0]
            self.__deck=DM[1]
            ###############gana acusado###############
            
            





            input(print(self.__D_acusador["name"],'''ha perdido el desafio. 
            Presione cualquier tecla para ver tus cartas'''))
        
        
            for i in range(self.__D_acusador["influence"]):
                print("carta ",i+1,' ',self.__D_acusador["cards"][i])

            print('seleccione la carta que quieres perder')
        
            carta_volteada= int(input())-1

            DM=Brain(self.__deck,self.__D_acusador).Lost_card(carta_volteada)
            self.__D_acusador=DM

            ################# lo que pierde acusador##########

            return [self.__D_acusado,self.__D_acusador,self.__deck,0]
            


            
        else:
            print(self.__D_acusado["name"],'''ha perdido el desafio''')

            DM=Brain(self.__deck,self.__D_acusado).Lost_card(carta_volteada)
            self.__D_acusado=DM

            return[self.__D_acusado,self.__D_acusador,self.__deck,1]#si termina en 0 el desafiado gana y si termina en 1 el desafiante gana