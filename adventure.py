"""
Library of stuff to make a text adventure
"""
class Entity():
    
    def __init__(self):
        self.health = 100


class NPC(Entity):
    pass

class Player(Entity):
    pass

class Monster(NPC):
    pass

class Villager(NPC):
    pass

if __name__ == '__main__':
    player = Player()
    print(player.health)
