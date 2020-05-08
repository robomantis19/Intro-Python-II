import random

class Monster: 
    def __init__(self): 
        self.health = random.randrange(50,100, 10)
        self.attack = random.randrange(5,30, 5)
    def take_damage(self, attack_val): 
        self.health -= int(attack_val)
    def __str__(self): 
        return f"MONSTER HEALTH: {self.health}"
    def fire_attack(self): 
        print(f'gobblin fire attack {self.attack + 10}')
        return self.attack + 10
    def tackle(self): 
        num = random.randrange(1,4)
        num2 = random.randrange(5, 25, 1)
        if num == 2:
            print(f'**gobblin tackle > critical hit** -{self.attack + num2}') 
            return self.attack + num2 
        else: 
            print(f'gobblin tackle -{self.attack}')
            return self.attack

# gobblin = Monster()
# print(gobblin)
# while True: 
#     inputs = input('input attack value: ')
#     gobblin.take_damage(inputs)
#     print(gobblin)
    