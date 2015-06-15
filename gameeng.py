"""The main game engine"""
import colors as c
import json
from player import Player
import monster as m

class Game():
    def __init__(self):
        print('Welcome')
        self.player = Player()


    def run(self):
        while True:
            action = input('What do you want to do? ')
            print(c.clear)
            if action == 'stats':
                self.player.show_stats()
            elif action == 'save':
                self.save()
            elif action == 'exit':
                print("Adios!")
                exit()
            elif action in ['pick','choose','decide']:
                count = 1
                for monster in m.monsters:
                    print(count,monster)
                    count += 1
        self.run()

    def save(self):
        print("would have saved")


    def load_player(self):
        pass


    def _choose_monster(self):
        pass


if __name__ == '__main__':
    agame = Game()
    agame.run()
