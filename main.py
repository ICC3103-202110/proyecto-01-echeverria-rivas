from players import *
from numpy import *
from start_game import *

maze = ["Duke", "Duke", "Duke", "Assassin", "Assassin", "Assassin", 
        "Captain", "Captain", "Captain", "Ambassador", "Ambassador", "Ambassador", 
        "Contessa", "Contessa", "Contessa"]
random.shuffle(maze)
x = [] #Lista vacia para nombres de jugadores
LUsers = [] #Lista vacia para diccionario de jugadores
n = 0 #numero jugadores
while n != 3 and n != 4:
    n = int(input("How many player will play (3 or 4): "))



LPlayers = Player.create_player("",x,n)


for n in LPlayers: #Uso de la funcion Dic en la clase Player
    p = Player(n).Dic()
    LUsers.append(p)

for i in LPlayers: #Dicionario con cartas para cada jugador
    c = maze[0]
    maze.pop(0)
    i["cards"].append(c)
    c = maze[0]
    maze.pop(0)
    i["cards"].append(c)



Start_Game(maze, LPlayers, 0).game() 