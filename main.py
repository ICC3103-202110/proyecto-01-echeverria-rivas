from players import *
from numpy import *

maze = ["Duke", "Duke", "Duke", "Assassin", "Assassin", "Assassin", 
        "Captain", "Captain", "Captain", "Ambassador", "Ambassador", "Ambassador", 
        "Contessa", "Contessa", "Contessa"]
random.shuffle(maze)
x = [] #Lista vacia para nombres de jugadores
LUsers = [] #Lista vacia para diccionario de jugadores
n = 0 #Dumero jugadores
while n != 3 and n != 4:
    n = int(input("How many player will play (3 or 4): "))

def create_player(L,J): #Funcion para agregar nombres a la lista (Keys Dictionary)
    for i in range(J):
        print("Write player #",i+1,"name: ")
        name = input()
        L.append(name)
    return L

LPlayers = create_player(x,n) #Keys Dictionary

for n in LPlayers: #Uso de la funcion Dic en la clase Player
    p = Player(n).Dic()
    LUsers.append(p)