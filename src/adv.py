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
#

# Make a new player object that is currently in the 'outside' room.


player = room["outside"]
print(player.name)

class Loop1: 
    def __init__(self, input): 
        self.input = input

    def the_loop(self):
        name = input('Enter a name  : ')
        for i in self.input: 
            print(self.input[i].name)
            print(self.input[i].description)
            input1 = input("Enter either n w s e:")
            if input1 == 'n': 
                mapper = Room(n_to=True)
            elif input1 == 'w': 
                mapper = Room(w_to=True)
            elif input1 == 's': 
                mapper = Room(s_to=True)
            elif input1 == 'e': 
                mapper = Room(e_to=True)
            output = Player(name, self.input[i])

outer_loop = Loop1(room)
outer_loop.the_loop()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
