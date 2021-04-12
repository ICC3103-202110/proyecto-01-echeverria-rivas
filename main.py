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

for i in LUsers: #Dicionario con cartas para cada jugador
    c = maze[0]
    maze.pop(0)
    i["cards"].append(c)
    c = maze[0]
    maze.pop(0)
    i["cards"].append(c)

def print_menu(): #Menu Turno
    print("")
    for i in LUsers:
        print(i["name"],"Cartas:", len(i["cards"]), "Cartas Perdidas:",i["lostcards"], "Monedas:",i["coins"])
    print("")
    print("Selecione que quiere hacer: ")
    print("1. Ejecutar una accion")
    print("2. Ver mis cartas")
    print("3. Ver log")
    return int(input())

def game(mazo, LJ, LU, turno):
    JA = LU[turno]["name"] #acceder al nombre del jugador actual
    print(JA)
    selection = print_menu()
    if selection == 1:
        pass
        if turno != len(LJ):
            turno += 1
        else:
            turno = 0
    if selection == 2:
        print(LU[turno]["cards"]) #acceder a cartas del jugador actual

turno=0
game(maze, LPlayers, LUsers, turno)    