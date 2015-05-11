"""
A simple dice rolling module
"""
import random as r

def rolldie(sides=6):
    return r.randint(1,sides)
def roll(times,sides):
    total = 0
    for count in range(times):
        total += rolldie(sides)
    return total
        
if __name__ == "__main__":
    number = rolldie(6)
    print(number)

    strength = roll(3,6)
    print(strength)

    
