

class Item: 
    def __init__(self, name=None, description=None): 
        self.name = name
        self.description = description
        self.inventory = []

    def on_take(self, item):
        self.inventory.append(item)
        return f"\n*****\nYou have picked up {item}!\n******* \n" 

    def on_drop(self, item): 
        i = self.inventory.index(item)
        self.inventory.pop(i)
        return f"\n*****\nYou have dropped up {item}!\n******* \n" 

    def __str__(self): 
        return f"Inventory of Items: {self.inventory}"