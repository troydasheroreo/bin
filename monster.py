from dice import roll
import colors as c

class Monster():
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
if __name__ == '__main__':
    monster = Monster()
    print(c.clear)
    monster.show_stats()
     
