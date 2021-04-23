from players import *
from numpy import *
from start_game import *
from mazo import *



shuffled_deck=Deck(["Duke", "Duke", "Duke", "Assassin", "Assassin", "Assassin", 
        "Captain", "Captain", "Captain", "Ambassador", "Ambassador", "Ambassador", 
        "Contessa", "Contessa", "Contessa"]).shuffle()



x = [] #Lista vacia para nombres de jugadores

n = 0 #numero jugadores
while n != 3 and n != 4:
    n = int(input("How many player will play (3 or 4): "))



LPlayers = Player.create_player("",x,n)

for i in LPlayers:
    c = shuffled_deck[0]
    shuffled_deck.pop(0)
    i["cards"].append(c)
    c = shuffled_deck[0]
    shuffled_deck.pop(0)
    i["cards"].append(c)


for i in range(len(LPlayers)):
    print('\n','Player' , LPlayers[i]['name'],'press any key to see your cards')
    input()
    print('\n',LPlayers[i]['cards'])


Start_Game(shuffled_deck, LPlayers, 0).game() 