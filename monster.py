from dice import roll
import colors as c

monsters = [
"Elf",
"Goblin",
"Demon"
]

class HasStats():
    health = 100
    def __init__(self):
        self.strength = roll(5,6)
        self.intelligence = roll(1,6)
        self.dexterity = roll(1,6)
        self.wisdom = roll(2,6)

    def show_stats(self):
        text = """
        Strength:       {s.strength:>2}
        Intelligence:   {s.intelligence:>2}
        Dexterity:      {s.dexterity:>2}
        Wisdom:         {s.wisdom:>2}
        """
        print(text.format(s=self))
        
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
    hasstats = HasStats()
    print(c.clear)
    hasstats.show_stats()
     
