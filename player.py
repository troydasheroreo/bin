from interfaces import HasStats
import colors as c        
class Player(HasStats):
    def __init__(self):
        self.set_stats()

    def pick_move(self):
        move = ask("What move do you want to make?") 

if __name__ == '__main__':
    player = Player()
    print(c.clear)
    player.load()
    player.show_stats()
    player.save()
    
    
