import random

class sword:
    damage = 100
    durability = 200
    resilience = 100


class player:
    def __init__(self, name:str, weapon:object):
        self.name = name
        self.health = random.randint(100, 500)
        self.damage = weapon.damage
if __name__ == '__main__':