""" A collection of interfaces used in the gameeng classes"""
from dice import roll
import colors as c
import json


class HasStats():
    hp = 100
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
    def load(self):
        with open('player.json', 'r') as pfile:
            j = json.load(pfile)
            self.strength = j['strength']
            self.constitution = j['constitution']
            self.intelligence = j['intelligence']
            self.dexterity = j['dexterity']
            self.wisdom = j['wisdom']
            self.charisma = j['charisma']
        



