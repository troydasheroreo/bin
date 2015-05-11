#!/usr/bin/env python3
""" Dice module
"""
import random
def roll(n, sides):
    n = int(n)
    sides = int(sides)
    total = 0
    for count in range(n):
        total += random.randint(1,sides)
    return total
if __name__ == '__main__':
    for count in range(20):
        print(roll(3,6))
    
