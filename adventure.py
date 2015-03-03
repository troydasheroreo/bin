"""
Library of stuff to make a text adventure
"""

import diceroll as roll 

class Entity():
    
    def __init__(self):
        self.health = 100
        self.speed = 1
        self.hunger = 0
        self.attack = roll.roll(3,6)
        self.defense = roll.roll(3,6)

    def __str__(self):
       f = "Health: {}\nSpeed: {}\nHunger: {}\nAttack: {}\nDefense: {}"
       return f.format(self.hunger,self.speed,self.attack,self.health,self.defense)
         


class NPC(Entity):
    pass

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.health = 120

class Monster(NPC):
    pass

class Villager(NPC):
    pass

if __name__ == '__main__':
    player = Player()
    print ("-~-" * 10)
    print("Player ",player)

    npc = NPC()
    print ("-~-" * 10)
    print("NPC",npc)
