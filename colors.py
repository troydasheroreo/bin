
'''
The colors
'''

import random as r

red = '\033[0;31m'
orange = '\033[1;31m'
pink = '\033[0;35m'
yellow = '\033[0;33m'
green = '\033[0;32m'
blue = '\033[0;34m'
black = '\033[0;30m'
grey = '\033[1;34m'
gray = '\033[1;32m'
purple = '\033[1;35m'
white = '\033[0;37m'
turquoise = '\033[0;36m'
reset = '\033[0m'
clear = '\033[H\033[2J'

colors = [red,
orange,
pink,
yellow,
green,
blue,
black,
grey,
gray,
purple,
white,
turquoise,
reset,
clear]
 
def random_color():
    return r.choice(colors)

if __name__ == '__main__':
    print(clear)
    print(red + 'red' + reset)
    print(blue + 'blue' + reset)
    print(yellow + 'yellow' + reset)
    print(orange + 'orange' + reset)
    print(pink + 'pink' + reset)
    print(green + 'green' + reset)
    print(black + 'black' + reset)
    print(grey + 'grey' + reset)
    print(gray + 'gray' + reset)
    print(purple + 'purple' + reset)
    print(white + 'white' + reset)
    print(turquoise + 'turquoise' + reset)
