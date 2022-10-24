# Please fix the display's coordinations for me. Thank you 
# Khoi

import pygame as pg 

class UI:
        def __init__(self, screen):
      
                # health and score 
                self.screen_width = 800
                self.screen_height = 1000
                self.lives = 3
                self.live_surf = pg.image.load(f'images/sprites/pacman/pacman_left0.png').convert_alpha()
                self.live_x_start_pos = self.screen_width - (self.live_surf.get_size()[0] * 2 + 10)          # get width and height of lives and offset the lives on the screen
                self.score = 0      
                self.font = pg.font.Font('font/Emulogic-zrEw.ttf', 20)        # add font                      #<---------- add your font here
                self.screen = screen 
# Display lives
        def display_lives(self):
                for live in range(self.lives - 1):
                        x = self.live_x_start_pos + (live* (self.live_surf.get_size()[0] + 5))             # start lives on left side; place them next to each other, offset 10
                        self.screen.blit(self.live_surf,(x,self.screen_height-200))
                score_surf  = self.font.render(f'Lives:', False, 'white')
                # score_rect = score_surf.get_rect(topleft =(10,-10))
                self.screen.blit(score_surf, ((self.screen_width - self.live_surf.get_width())/1.3, self.screen_height -200)) 

        # Add and display score:
        def display_score(self):
                score_surf  = self.font.render(f'score: {self.score}', False, 'white')
                # score_rect = score_surf.get_rect(topleft =(10,-10))
                self.screen.blit(score_surf, ((self.screen_width - self.live_surf.get_width())/10, self.screen_height -200)) 
        def display_hi_score(self):
                score_surf  = self.font.render(f'Highscore: {self.score}', False, 'white')
                # score_rect = score_surf.get_rect(topleft =(10,-10))
                self.screen.blit(score_surf, ((self.screen_width - self.live_surf.get_width())/3, self.screen_height -200)) 
        
        def run(self):
                self.display_lives()
                self.display_score()
                self.display_hi_score()
