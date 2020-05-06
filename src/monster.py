import random

class Monster: 
    def __init__(self): 
        self.health = random.randrange(50,100, 10)

    def take_damage(self, attack_val): 
        self.health -= int(attack_val)
    def __str__(self): 
        return f"MONSTER HEALTH: {self.health}"

# gobblin = Monster()
# print(gobblin)
# while True: 
#     inputs = input('input attack value: ')
#     gobblin.take_damage(inputs)
#     print(gobblin)
    