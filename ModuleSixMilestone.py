#Anabel Villalobos



#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

current_room = 'Great Hall'

while True:
    #if the user input was exit the game will end
    if current_room == 'exit':
        break

    #print what room the player is currently in
    print("You are in the {}".format(currentRoom))
    print("Make your move.")
    #take in player's move
    player_move = input()
    move_arr = player_move.split(" ")
    if move_arr[0] == "go":
        direction = move_arr[1]
        #if the direction is in the current room dictionary
        if direction in rooms.current_room:
            #set the current room equal to that room
            current_room = rooms.direction
    # if the player input is exit
    elif move_arr[0].lower() == "exit":
        #then the current room is set to exit
        current_room = "exit"
    else:
        # handle input validation error
        print("You can't go that way")


