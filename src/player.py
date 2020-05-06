# Write a class to hold player information, e.g. what room they are in
# currently.


class Player: 
    def __init__(self, name, current_room): 
        self.name = name
        self.current_room = current_room
        self.direction = 'x'

    def move(self, n): 
        dirs = {'s':'n', 'e':'w'}
        reverse_dirs = {'n':'s', 'w':'e'}
        
        if hasattr(self.current_room, f'{n}_to'): 
            new_room = getattr(self.current_room, f'{n}_to')
            print(new_room)
            self.direction = n
            self.current_room = new_room
        else:
            print('Cannot go that way')
    