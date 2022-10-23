import pygame as pg
import sys
import os
from os import listdir
from settings import Settings
from timer import Timer

class Ghost_manager:
    def __init__(self, screen, settings):
        self.screen = screen
        self.setting = settings
        self.red_ghost = red_ghost (self.screen, 0, 0, settings)
        self.blue_ghost = blue_ghost(self.screen, 0, 0, settings)
        self.yellow_ghost = yellow_ghost(self.screen, 0, 0, settings)
        self.pink_ghost = pink_ghost(self.screen, 0, 0, settings)
        
        # self.ghost_timers = {0 : Timer(image_list=self.red_ghost.sprites), 
        #         1 : Timer(image_list=self.blue_ghost.sprites), 
        #         2 : Timer(image_list=self.pink_ghost.sprites),
        #         2 : Timer(image_list=self.pink_ghost.sprites)}         
    
    def set_coordinate(self, row, col, color):

        if color == 1:    
            self.red_ghost.y = row
            self.red_ghost.x = col

        if color == 2:
            self.blue_ghost.y = row
            self.blue_ghost.x = col 
        
        if color == 3: 
            self.pink_ghost.y= row
            self.pink_ghost.x = col
        
        if color == 4: 
            self.yellow_ghost.y= row
            self.yellow_ghost.x = col
        
    def set_direction(self, dir, ghost_code):
        #1-red 2-blue, 3-pink 4-pink
        if ghost_code ==1:
            self.red_ghost.direction = dir
        if ghost_code ==2:
            self.blue_ghost.direction = dir
        if ghost_code ==3:
            self.pink_ghost.direction = dir
        if ghost_code ==4:
            self.yellow_ghost.direction =dir 
    def update(self):
        
        # self.red_ghost.move()
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
    def __init__(self, screen, row,col, settings):
        super().__init__()
        self.screen = screen
        self.row = row
        self.col = col
        self.direction = 3
        self.image= pg.image.load(f'images/sprites/red/red_ghost1.png')
        self.rect= self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.settings = settings 
       


    def draw(self, pos_x, pos_y): 
        
        # image = ghost_timer.image()
        # rect = image.get_rect()
        # rect.left, rect.top = self.rect.left, self.rect.top
        # self.screen.blit(image, rect)
        

        self.rect.topleft = [pos_x, pos_y]
        self.screen.blit(self.sprites[self.current_sprite], self.rect)

    def update(self):
        # self.current_sprite += 1
        if self.direction == 4:
            self.x += (self.settings.ghosts_speed)
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction ==2:
            self.x -= (self.settings.ghosts_speed)
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == 1:
            self.y -= (self.settings.ghosts_speed )
            self.rect.y = self.y
            self.rect.x = self.x
        elif self.direction == 3:
            self.y += (self.settings.ghosts_speed )
            self.rect.y = self.y
            self.rect.x = self.x
            
        
        # if self.current_sprite >= len(self.sprites):
        #     self.current_sprite =0
        # self.image = self.sprites[self.current_sprite]
        self.draw(self.rect.x, self.rect.y)

    


class red_ghost(Ghost): #for loading red ghosts
    def __init__(self,screen, row, col, settings):
        super().__init__(screen, row,col,  settings)

        # screen =screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/red/red_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

    def change_facing_dir(self, dir):
        if dir == 1:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/red/red_down{n}.png')) for n in range(2)]

        if dir == 2:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/red/red_left{n}.png')) for n in range(2)]

        if dir == 3:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/red/red_up{n}.png')) for n in range(2)]

        if dir == 4:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/red/red_right{n}.png')) for n in range(2)]




    
        
    
class blue_ghost(Ghost):
    def __init__(self,screen, row, col, settings):
        super().__init__(screen, row, col, settings)
        
 # self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/blue/blue_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
    def change_facing_dir(self, dir):
        if dir == 1:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/blue/blue_down{n}.png')) for n in range(2)]
        
        if dir == 2:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/blue/blue_left{n}.png')) for n in range(2)]

        if dir == 3:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/blue/blue_up{n}.png')) for n in range(2)]

        if dir == 4:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/blue/blue_right{n}.png')) for n in range(2)]


class pink_ghost(Ghost):
    def __init__(self,screen,  row, col, settings):
        super().__init__(screen, row, col, settings)
        # screen = screen 
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/pink/pink_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
    def change_facing_dir(self, dir):
        if dir == 1:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/pink/pink_down{n}.png')) for n in range(2)]
        
        if dir == 2:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/pink/pink_left{n}.png')) for n in range(2)]

        if dir == 3:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/pink/pink_up{n}.png')) for n in range(2)]

        if dir == 4:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/pink/pink_right{n}.png')) for n in range(2)]

class yellow_ghost(Ghost):
    def __init__(self,screen, row, col, settings):
        super().__init__(screen, row, col, settings)
        # self.screen = screen
        self.sprites = []
        [self.sprites.append(pg.image.load(f'images/sprites/yellow/yellow_ghost{n+1}.png')) for n in range(8)]
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
    def change_facing_dir(self, dir):
        if dir == 1:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/yellow/yellow_down{n}.png')) for n in range(2)]
        
        if dir == 2:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/yellow/yellow_left{n}.png')) for n in range(2)]

        if dir == 3:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/yellow/yellow_up{n}.png')) for n in range(2)]

        if dir == 4:
            self.sprites.clear()
            [self.sprites.append(pg.image.load(f'iamges/sprites/yellow/yellow_right{n}.png')) for n in range(2)]

