from room import Room
from player import Player
from monster import Monster
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
monster = Monster()
player = Player('tj', room['outside'])
count = 0 
while True:
    count += 1
    inputs = input('input direction: n, s, e, w: ')
    
    print(player.move(inputs))
    print(player.take_damage('2'))
    if count == 2: 
        print("oh no you've encountered a goblin, time to fight")
        gobblin = Monster()
        print(gobblin)
        loop = True
        while loop == True: 
            inputs = input('swipe sword enter r, magic enter f:')
            if inputs == 'r': 
                gobblin.take_damage('10')
                print(gobblin)
            elif inputs == 'f': 
                print('magic attack value of: ',player.attack)
                gobblin.take_damage(player.attack)
                print(gobblin)
            if gobblin.health == 0 : 
                loop = False





# Make a new player object that is currently in the 'outside' room.

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
