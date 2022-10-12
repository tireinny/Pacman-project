from os import path

HS_FILE = "high_score.txt"

class high_score:
    
    def __init__(self):

        self.load_data()
        
    # load high score
    def load_data(self):
        
        self.dir = path.dirname(__dirname__)
        with open(path.join(self.dir, HS_FILE), 'w') as f:
            self.highscore = int(f.read())
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
                
    def show_high_score(self):       
        
        if self.score > self.highscore:
            self.highscore > self.highscore
            self.draw_text("New High Score!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
             self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        
        

