# Write a class to hold player information, e.g. what room they are in
# currently.

import random
class Player: 
    def __init__(self, name, current_room): 
        self.name = name
        self.current_room = current_room
        self.direction = 'x'

        self.health = 100
        self.attack = random.randrange(10, 50, 10)

    def take_damage(self, attack_val): 
        self.health -= int(attack_val)
        return f"Player HEALTH: {self.health}, \nPlayer Magic Attack Value {self.attack}"
    def move(self, n): 
        dirs = {'s':'n', 'e':'w'}
        reverse_dirs = {'n':'s', 'w':'e'}
        
        if hasattr(self.current_room, f'{n}_to'): 
            new_room = getattr(self.current_room, f'{n}_to')
            print(new_room)
            self.direction = n
            self.current_room = new_room
        else:
            return 'Cannot go that way'
    def print_room(self): 
        print(f"{self.current_room.name}")