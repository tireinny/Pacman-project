import pygame as pg
import sys
import os
from os import listdir


class Ghost(pg.sprite.Sprite): #for creating all the ghosts 
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.red_ghost = red_ghost(self.screen)
        self.blue_ghost = blue_ghost(self.screen)
        self.yellow_ghost = yellow_ghost(self.screen)
        self.pink_ghost = pink_ghost(self.screen)

    def draw(self, pos_x, pos_y): 
       
        self.rect= self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.screen.blit(self.sprites[self.current_sprite], (pos_x, pos_y))

    def update(self):
        self.current_sprite += 1 
        if self.current_sprite >= len(self.sprites):
            self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

class red_ghost(Ghost): #for loading red ghosts
    def __init__(self, screen):
        self.screen =screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/red/red_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

    def move():pass
    
        
    
class blue_ghost(Ghost):
    def __init__(self, screen):
        self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/blue/blue_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

class pink_ghost(Ghost):
    def __init__(self, screen):
        self.screen = screen 
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/pink/pink_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

class yellow_ghost(Ghost):
    def __init__(self, screen):
        self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/yellow/yellow_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

