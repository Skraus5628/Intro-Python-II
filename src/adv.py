from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# valid_dirs = ['n', 'e', 'w', 's']

# Make a new player object that is currently in the 'outside' room.
player = Player("Gwar", room["outside"])

       
# Write a loop that:
#
# * Prints the current room name
print(player.room.name)
print(player.room.description)

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

### REPL is repeat eval perform loop
## elif = else if 
# hasattr checks if () input has attribute



userInput = input('Input a movement direction (n,w,s,e) Press "q" to quit.')

#If the user isnt boring or doesnt read instructions and doesnt hit q
while userInput != 'q':

    # IF the user doesnt put any valid entry at all

    if(userInput not in ['n', 'w', 's', 'e', 'q']):

        userInput = input('Please enter a valid input or press "q" to quit.')

    # If players current room doesnt have the specific movement attr input
    # Prompt to move different direction.
    
    elif(not hasattr(player.room, f'{userInput}_to') and userInput != 'q'):

        print(userInput)
        userInput = input('You cannot move in that direction. Choose another or press "q" to quit.')

    # If player puts in valid direction for current room print the name and description of room

    elif(userInput != 'q'):

        player.room = getattr(player.room, f'{userInput}_to')
        # using f formatting to take in user input directional letter to fill 
        #the n_to etc command
        print(player.room.name)
        print(player.room.description)

#Repost user input window 
        userInput = input('Input a movement direction (n,w,s,e_ or press "q" to quit.')

        print('done')
