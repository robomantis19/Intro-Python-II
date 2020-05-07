# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description, lists): 
        self.name = name
        self.description = description
        self.lists = lists
    def __str__(self): 
        return f"{self.name}, {self.description} \n\nItems in room: {self.lists}\n\n"

    