from dice import roll
import colors as c
import json


class HasStats():
    health = 100
    def set_stats(self):
        self.strength = roll(3,6)
        self.constitution = roll(3,6)
        self.dexterity = roll(3,6)
        self.intelligence = roll(3,6)
        self.wisdom = roll(3,6)
        self.charisma = roll(3,6)
    def show_stats(self):
        text = '''
        Strength:       {s.strength:>2}
        Constitution:   {s.constitution:>2}
        Dexterity:      {s.dexterity:>2}
        Intelligence:   {s.intelligence:>2}
        Wisdom:         {s.wisdom:>2}
        Charisma:       {s.charisma:>2}
        '''
        print(text.format(s=self))

    def save(self):
        with open('player.json', 'w') as outfile:
            outfile.write(json.dumps({
            "strength": self.strength,
            "constitution": self.constitution,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
            }))
            
        
class Player(HasStats):
    def __init__(self):
        self.set_stats()
class Elf(HasStats):
    def __init__(self):
        self.set_stats()
        self.wisdom += 10
        self.intelligence += 10
class Goblin(HasStats):
    def __init__(self):
        self.set_stats()
        self.constitution += 10
class Demon(HasStats):
    def __init__(self):
        self.set_stats()
        self.dexterity += 10
        self.intelligence += 10
        self.wisdom += 10
        



if __name__ == '__main__':
    player = Player()
    print(c.clear)
    player.show_stats()
    player.save()
