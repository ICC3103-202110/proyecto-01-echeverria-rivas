class Player:
    def __init__(self, name):
        self.__name = name
    
    def Dic(self):
        D = {"name": self.__name , "cards":[], "coins":2, "log":[], "influence":2, "lostcards":[]}
        return D
