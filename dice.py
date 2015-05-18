"""
A simple dice rolling module
"""
import random as r
import colors as c

def rolldie(sides=6):
    return r.randint(1,sides)
def roll(amount=1,sides=6):
    total = 0
    for count in range(amount):
        total += rolldie(sides)
    return total
def parse_roll(text):
    """Parses traditional dice notation (ex:3d6)"""
    amount, sides = text.split('d')
    return roll(int(amount), int(sides))
if __name__ == "__main__":
   for count in range(20):
        #number = rolldie()
        #print(intnumber,end=" ")
    print(c.random_color(), end=' ')   
    print(parse_roll('2d20'), end=' ')
    


    
