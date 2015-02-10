#!/usr/bin/env python3



def q1():
    print('''
    What is my middle name?
    A. Joseph
    B. Tyler
    C. Paul
    D. Renee
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("Correct")
        return 100
    elif answer == 'b':
        print("No")
    elif answer == 'c':
        print("No")
    elif answer == 'd':
        print("No")
    else:
        print("Not a legitimate answer")
        return 0 

def q2():
    print('''
    What is my favorite number? 
    A. 28
    B. 666
    C. 19
    D. 2345678
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("Correct")
        return 100
    elif answer == 'b':
        print("No")
    elif answer == 'c':
        print("No")
    elif answer == 'd':
        print("No")
    else:
        print("Not a legitimate answer")
        return 0

def q3():
    print('''
    What is my favorite TV show? 
    A. Doctor Who
    B. Castle
    C. COPS
    D. Daily Show
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("No")
    elif answer == 'b':
        print("No")
    elif answer == 'c':
        print("Correct")
        return 100
    elif answer == 'd':
        print("No")
    else:
        print("Not a legitimate answer")
        return 0
def q4():
    print('''
    What is my favorite band? 
    A. Panic! At The Disco
    B. Breaking Benjamin
    C. Beartooth
    D. Sixx:A.M.
''')
    answer = input('> ').strip().lower()
    if answer == 'a':
        print("No")
    if answer == 'b':
        print("Correct")
        return 100
    if answer == 'c':
        print("No")
    if answer == 'd':
        print("No")
    else:
        print("Not a legitimate answer")
        return 0

