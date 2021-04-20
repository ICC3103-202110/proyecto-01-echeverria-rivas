from Acciones import *





class Intervenciones(Actions):
    def __init__(self,D_acusado,D_acusador,deck):
    

    def Desafio (self):
        input(print(self.__D_acusado["name"],'''ha sido desafiado. 
            Presione cualquier tecla para ver tus cartas'''))
        
        
        for i in range(self.__D_acusado["influence"]):
            print("carta ",i+1,' ',self.__D_acusado["cards"][i])
        return input()
            