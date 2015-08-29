from interfaces import HasStats
import colors as c        
class Player(HasStats):
    def __init__(self):
        self.set_stats()
    

    def pick_move(self):
        self.move = ask("What move do you want to make?")

    def move(self):
        if self.move == 'harden':
            self.buff('defense','battle', percent =25)
            

if __name__ == '__main__':
    player = Player()
    print(c.clear)
    player.load()
    player.show_stats()
    player.save()
    
    
