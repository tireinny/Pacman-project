# Please fix the display's coordinations for me. Thank you 
# Khoi

import pygame

class UI:
  
    def __init__(self):
      
        # health and score 
        self.lives = 3
        self.live_surf = pg.image.load('pacman.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)          # get width and height of lives and offset the lives on the screen
        self.score = 0      
        self.font = pg.font.Font('font/Pixeled.ttf', 20)        # add font                      #<---------- add your font here
        
# Display lives
def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live* (self.live_surf.get_size()[0] + 10))             # start lives on left side; place them next to each other, offset 10
            screen.blit(self.live_surf,(x,8))

# Add and display score:
def display_score(self):
        score_surf  = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft =(10,-10))
        screen.blit(score_surf, score_rect) 
     
def run(self):
       self.display_lives()
       self.display_score()
