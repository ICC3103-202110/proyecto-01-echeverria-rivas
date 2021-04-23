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
        print(self.__D_acusado['name'], "Pulsa para ver tus cartas y selecciona la que quieres perder")
        input()
        for i in len(self.__D_acusado['cards']):
            print(i,". ",self.__D_acusado['cards'][i])
        card = int(input('Selecciona cual quieres perder: '))-1
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
        print("pulse cualquier tecla para ver todas las cartas en su mano e indique una que quiera eliminar")
        input()
        a=1
        for i in self.__D_acusador['cards']:
            print(a,". ",i)
            a+=1
        carta_a_eliminar=int(input("N° de carta eliminar: "))-1

        EM= Brain(self.__deck, self.__D_acusador).Deposit_cards(self.__D_acusador['cards'][carta_a_eliminar])
        self.__D_acusador=EM[0]
        self.__deck=EM[1]

        print(" indique la siguente carta que quiera eliminar")
        
        a=1
        for i in self.__D_acusador['cards']:
            print(a,". ",i)
            a+=1
        carta_a_eliminar=int(input("N° de carta eliminar: "))-1

        EM= Brain(self.__deck, self.__D_acusador).Deposit_cards(self.__D_acusador['cards'][carta_a_eliminar])
        self.__D_acusador=EM[0]
        self.__deck=EM[1]

        return [self.__D_acusador,self.__deck]













    def Asesino(self):
        nd = Brain(self.__deck,self.__D_acusador).Change_coins('-',3)
        self.__D_acusador['coins'] = nd
        print(self.__D_acusado['name'], "Pulsa para ver tus cartas y selecciona la que quieres perder")
        input()
        for i in len(self.__D_acusado['cards']):
            print(i,". ",self.__D_acusado['cards'][i])
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
        

    




    































