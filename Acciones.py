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


    def Duque (self):
        self.__D_acusador['coins'] = Brain(self.__deck,self.__D_acusador).Change_coins('+',3)
        return self.__D_acusador['coins']

   # def Embajador(self):

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

    



   # def Embajador (self):

  #  def Capitan(self):




    































