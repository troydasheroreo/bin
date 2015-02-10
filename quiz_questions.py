#!/usr/bin/env python3



def q1():
    print('''
    What is the capital of Finland?
    A. St. Croix
    B. Andorra La Vella
    C. Helinksi
    D. Bernuli
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("St. Croix is in the Virgin Islands")
    elif answer == 'b':
        print("Andorra La Vella is the capital of Andorra")
    elif answer == 'c':
        print("Correct")
        return 100
    elif answer == 'd':
        print("This was a guy, not even a city")
    else:
        print("Not a legitimate answer")
        return 0 

def q2():
    print('''
    What country is bigger than Pluto? 
    A. Russia
    B. Yugoslavia
    C. Canada
    D. Sri Lanka
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("Correct")
        return 100
    elif answer == 'b':
        print("This does not exist anymore")
    elif answer == 'c':
        print("Close, but no cigar")
    elif answer == 'd':
        print("Just...No")
    else:
        print("Not a legitimate answer")
        return 0

def q3():
    print('''
    What country has the only non-rectangular flag? 
    A. India
    B. Berlin
    C. Jordan
    D. Nepal
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("No")
    elif answer == 'b':
        print("Berlin is a town, which has no flag")
    elif answer == 'c':
        print("No")
    elif answer == 'd':
        print("Correct")
        return 100
    else:
        print("Not a legitimate answer")
        return 0
def q4():
    print('''
    What state is both the farthest east and west in the United States? 
    A. Hawaii
    B. Delaware
    C. Idaho
    D. Alaska
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("You picked the only trick answer, you aren't fully stupid")
    if answer == 'b':
        print("I have no faith in your wisdom")
    if answer == 'c':
        print("You probably chose B the first time")
    if answer == 'd':
        print("Correct")
        return 100
    else:
        print("Not a legitimate answer")
        return 0

