from players import *
from numpy import *
from start_game import *
from mazo import *



shuffled_deck=Deck([]).shuffle()



x = [] #Lista vacia para nombres de jugadores

n = 0 #numero jugadores
while n != 3 and n != 4:
    n = int(input("How many player will play (3 or 4): "))



LPlayers = Player.create_player("",x,n)

for i in LPlayers: #Dicionario con cartas para cada jugador
    c = shuffled_deck[0]
    shuffled_deck.pop(0)
    i["cards"].append(c)
    c = shuffled_deck[0]
    shuffled_deck.pop(0)
    i["cards"].append(c)

print(LPlayers)

Start_Game(shuffled_deck, LPlayers, 0).game() 