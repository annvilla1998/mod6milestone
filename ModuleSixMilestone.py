#Anabel Villalobos



#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

currentRoom = 'Great Hall'

while True:
    #print what room the player is currently in
    print("You are in the {}".format(currentRoom))
    print("Make your move.")
    #take in player's move
    player_move = input()
    moveList = player_move.split(" ")

