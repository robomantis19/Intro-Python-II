from room import Room
from player import Player
from monster import Monster
import pyglet
import random
from item import Item
import sys

# Declare all the rooms
room_items = ['','','','','','potion', 'mana', 'shield', 'sword', 'bow', 'arrows', 'ring', 'backpack']
num = random.randrange(0,len(room_items))
num2 = random.randrange(0,len(room_items))
num3 = random.randrange(0,len(room_items))

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [room_items[num]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [room_items[num],room_items[num2],room_items[num3]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[room_items[num],room_items[num2]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[room_items[num],room_items[num2]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[room_items[num],room_items[num3]]),
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
item_holder = Item()
count = 0 
start = pyglet.resource.media('item.wav', streaming = False)
while True:

    if count == 0 or inputs == 'h' or inputs =='help': 	
                start.play()
                print(f'\n--------------------\n\nHi player: {player.name} \nType q to quit \n Type i for inventory\n Type room to see items in room \n Type "get item" to pick up item for example ---> get potion | or "drop item" to drop item from inventory| \n\n-----------------\n\n  ')
            
    count += 1
    inputs = input('\n\n-------------\n\nmove: n, s, e, w: \n get\drop [item name] \n\n--->')
    if inputs == 'room': 
        player.print_room()
        print('hi')
    if inputs == 'i': 
        print(item_holder)
    if inputs[0:3] == 'get': 
        print(item_holder.on_take(inputs[3:]))
        if inputs == 'i': 
            print(item_holder)
    if inputs == "q": 
        sys.exit(1)
    print(player.move(inputs))
    print(player.take_damage('2'))
    if count == 2: 
        print("\n\noh no you've encountered a goblin, time to fight\n\n")
        gobblin = Monster()
        print(gobblin)
        start = pyglet.resource.media('item.wav', streaming = False)
        sword = pyglet.resource.media('swordHit.wav', streaming = False)
        magic = pyglet.resource.media('magic.wav', streaming = False)
        count2 = 0
        loop = True
        while loop == True: 
            if count2 == 0 or inputs == 'h' or inputs =='help': 	
                start.play()
                print('\n--------------------\n\nAttack directions, for magic: press r key | for sword: press f key | \n\n  ')
            count2 += 1
            inputs = input("\n\n--->  ")
            if inputs == 'r': 
                sword.play()
                gobblin.take_damage('10')
                print(gobblin)
            elif inputs == 'f':
                magic.play() 
                print('\n\nmagic attack value of: ',player.attack,'\n\n')
                gobblin.take_damage(player.attack)
                print(gobblin)
            if gobblin.health == 0 : 
                print('\n\n Gobblin fainted \n\n')
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
