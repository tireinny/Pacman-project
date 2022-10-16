import pygame as pg
import sys
import os
from os import listdir

class Ghost_manager:
    def __init__(self, screen):
        self.screen = screen
        self.red_ghost = red_ghost (self.screen, 0, 0)
        self.blue_ghost = blue_ghost(self.screen, 0, 0)
        self.yellow_ghost = yellow_ghost(self.screen, 0, 0)
        self.pink_ghost = pink_ghost(self.screen, 0, 0)
        
    
    def set_coordinate(self, row, col, color):

        if color == 1:    
            self.red_ghost.row = row
            self.red_ghost.col = col

        if color == 2:
            self.blue_ghost.row = row
            self.blue_ghost.col = col 
        
        if color == 3: 
            self.pink_ghost.row = row
            self.pink_ghost.col = col
        
        if color == 4: 
            self.yellow_ghost.row = row
            self.yellow_ghost.col = col
        
    
    
    def update(self):

        self.red_ghost.update()
        self.blue_ghost.update()
        self.yellow_ghost.update()
        self.pink_ghost.update()
    def draw(self):
        self.red_ghost.draw()
        self.blue_ghost.draw()
        self.yellow_ghost.draw()
        self.pink_ghost.draw()

    def move(self,row, col, color):
        self.set_coordinate(row, col, color)
        self.update()


class Ghost(pg.sprite.Sprite): #for creating all the ghosts 
    def __init__(self, screen, row, col):
        super().__init__()
        self.screen = screen
        self.row = row
        self.col = col

    def draw(self, pos_x, pos_y): 
        self.rect= self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.screen.blit(self.sprites[self.current_sprite], (pos_x, pos_y))

    def update(self):
        self.current_sprite += 1
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
        self.draw(self.row, self.col)

    


class red_ghost(Ghost): #for loading red ghosts
    def __init__(self,screen, row, col):
        super().__init__(screen, row, col)

        # screen =screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/red/red_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]



    
        
    
class blue_ghost(Ghost):
    def __init__(self,screen, row, col):
        super().__init__(screen, row, col)
        
 # self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/blue/blue_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

class pink_ghost(Ghost):
    def __init__(self,screen,  row, col):
        super().__init__(screen, row, col)
        # screen = screen 
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/pink/pink_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

class yellow_ghost(Ghost):
    def __init__(self,screen, row, col):
        super().__init__(screen, row, col)
        # self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/yellow/yellow_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

