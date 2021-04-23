from crerebro import *


class Actions:
    def __init__(self,D_acusado,D_acusador,deck):#diccionarios de ambos usuarios involucrados
        self.__D_acusado = D_acusado
        self.__D_acusador = D_acusador
        self.__deck = deck
    
    def Ingreso(self):
        self.__D_acusador['coins'] = Brain(self.__deck,self.__D_acusador).Change_coins('+',1)
        return self.__D_acusador['coins']

    def Ayuda_Extrangera(self):
        self.__D_acusador['coins'] = Brain(self.__deck,self.__D_acusador).Change_coins('+',2)
        return self.__D_acusador['coins']

    def Golpe(self):
        nd = Brain(self.__deck,self.__D_acusador).Change_coins('-',7)
        self.__D_acusador['coins'] = nd
        print(self.__D_acusado['name'], "Press to see your cards and chose the one to lose")
        input()
        for i in   range(len(self.__D_acusado['cards'])):
            print(i+1,". ",self.__D_acusado['cards'][i])
        card = int(input('Chose the one to lose: '))-1
        nda = Brain(self.__deck,self.__D_acusado).Lost_card(card)
        self.__D_acusado = nda
        return [self.__D_acusador['coins'],self.__D_acusado]


    def Tax (self):
        self.__D_acusador['coins'] = Brain(self.__deck,self.__D_acusador).Change_coins('+',3)
        return self.__D_acusador['coins']

   
    def Cambio(self):
        EM= Brain(self.__deck, self.__D_acusador).Take_cards()
        self.__D_acusador=EM[0]
        self.__deck=EM[1]

        EM= Brain(self.__deck, self.__D_acusador).Take_cards()
        self.__D_acusador=EM[0]
        self.__deck=EM[1]
        print("Press any key to see your cards in the hand and chose the one to lose")
        input()
        a=1
        for i in self.__D_acusador['cards']:
            print(a,". ",i)
            a+=1
        carta_a_eliminar=int(input("Write the number of the card to eliminate: "))-1

        EM= Brain(self.__deck, self.__D_acusador).Deposit_cards(self.__D_acusador['cards'][carta_a_eliminar])
        self.__D_acusador=EM[0]
        self.__deck=EM[1]

        print("Select another card to eliminate")
        
        a=1
        for i in self.__D_acusador['cards']:
            print(a,". ",i)
            a+=1
        carta_a_eliminar=int(input("Write the number of the card to eliminate: "))-1

        EM= Brain(self.__deck, self.__D_acusador).Deposit_cards(self.__D_acusador['cards'][carta_a_eliminar])
        self.__D_acusador=EM[0]
        self.__deck=EM[1]

        return [self.__D_acusador,self.__deck]













    def Asesino(self):
        #nd = Brain(self.__deck,self.__D_acusador).Change_coins('-',3)
        #self.__D_acusador['coins'] = nd
        #esto hacia que se restara 2 veces 3 en monedas
        print(self.__D_acusado['name'], "Pulsa para ver tus cartas y selecciona la que quieres perder")
        input()
        for i in range(len(self.__D_acusado['cards'])):
            print(i+1,". ",self.__D_acusado['cards'][i])
        card = int(input('Selecciona cual quieres perder: '))-1
        nda = Brain(self.__deck,self.__D_acusado).Lost_card(card)
        self.__D_acusado = nda
        return [self.__D_acusador['coins'],self.__D_acusado]


    def Extorison (self):
        x = 0
        if self.__D_acusado['coins'] < 2:
            x = int(self.__D_acusado['coins'])
            self.__D_acusador['coins']=Brain(self.__deck,self.__D_acusador).Change_coins("+",x)
            self.__D_acusado['coins']=Brain(self.__deck,self.__D_acusado).Change_coins('-',x)
        else:
            self.__D_acusador['coins']=Brain(self.__deck,self.__D_acusador).Change_coins("+",2)
            self.__D_acusado['coins']=Brain(self.__deck,self.__D_acusado).Change_coins('-',2)
        return [self.__D_acusado,self.__D_acusador]
        

    




    































