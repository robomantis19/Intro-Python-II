from room import Room
from player import Player
from monster import Monster
import pyglet
import random
from item import Item
import sys

# Declare all the rooms
room_items = ['','','','','potion','potion', 'mana', 'shield', 'sword', 'bow', 'arrows', 'ring', 'potion']
num = random.randrange(0,len(room_items))
num2 = random.randrange(0,len(room_items))
num3 = random.randrange(0,len(room_items))

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [room_items[num]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [room_items[random.randrange(0,len(room_items))],room_items[random.randrange(0,len(room_items))],room_items[random.randrange(0,len(room_items))]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[room_items[random.randrange(0,len(room_items))],room_items[random.randrange(0,len(room_items))]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[room_items[random.randrange(0,len(room_items))],room_items[random.randrange(0,len(room_items))]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[room_items[num],room_items[random.randrange(0,len(room_items))]]),
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
                print(f'\n--------------------\n\nHi player: {player.name} \nType q to quit \n Type i for inventory and stats\n Type room to see items in room \n Type "get item" to pick up item for example ---> get potion | or "drop item" to drop item from inventory| \n\n-----------------\n\n  ')
            
    count += 1
    inputs = input('\n\n-------------\n\nmove: n, s, e, w: \n get\drop [item name] \n\n--->')
    if inputs == 'room': 
        player.print_room()
    if inputs == 'i': 
                print(f'\n---------items: {item_holder}, \nplayer health: {player.health}\nplayer attack value: {player.attack}')
    if inputs[0:3] == 'get': 
        start.play()
        # print('player.print_items()>>:', player.print_room_items())
        word = inputs[4:].strip(" ")
        popped_item = player.print_room_items(word)
        print('popped_item', popped_item)
        if popped_item: 

            print(item_holder.on_take(popped_item))
        if inputs == 'i': 
            print(item_holder)

    
    if inputs in item_holder.inventory:
        index = item_holder.inventory.index(inputs)
        item_to_be_used = item_holder.inventory.pop(index)
        player.use_item(item_to_be_used)
    elif inputs[0:4] == 'drop': 
        word = inputs[5:].strip(" ")
        if word in item_holder.inventory:
            item_holder.on_drop(word)

    if inputs == "q": 
        sys.exit(1)
    print(player.move(inputs))
    # print(player.take_damage('2'))
    if count % 6 == 0: 
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
            if inputs in item_holder.inventory:
                index = item_holder.inventory.index(inputs)
                item_to_be_used = item_holder.inventory.pop(index)
                player.use_item(item_to_be_used)
            if inputs == 'r':
                 
                sword.play()
                gobblin.take_damage(player.attack)
                print(gobblin)
                print(player.take_damage(gobblin.tackle()))
                
            elif inputs == 'f':
                
                magic.play() 
                print('\n\nmagic attack value of: ',player.attack,'\n\n')
                gobblin.take_damage(player.magic)
                print(gobblin)
                print(player.take_damage(gobblin.fire_attack()))
                
               
                
            if inputs == 'i': 
                print(f'\n---------items: {item_holder}, \nplayer health: {player.health}\nplayer attack value: {player.attack}')
            if gobblin.health <= 0 : 
                print('\n\n Gobblin fainted \n\n')
                loop = False
            if player.health <= 0: 
                print('\n\n Player fainted, game over \n\n')
                loop = False
                sys.quit(1)





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
