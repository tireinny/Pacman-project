import pygame as pg
from pygame.sprite import Sprite

class Character(Sprite):
    pacman_down =  [pg.transform.rotozoom(pg.image.load(f'images/sprites/pacman/pacman_down{n}.png'), 0, 1.0) for n in range(2)]
    pacman_up =  [pg.transform.rotozoom(pg.image.load(f'images/sprites/pacman/pacman_up{n}.png'), 0, 1.0) for n in range(2)]
    pacman_left =  [pg.transform.rotozoom(pg.image.load(f'images/sprites/pacman/pacman_left{n}.png'), 0, 1.0) for n in range(2)]
    pacman_right =  [pg.transform.rotozoom(pg.image.load(f'images/sprites/pacman/pacman_right{n}.png'), 0, 1.0) for n in range(2)]
    pacman_dead =  [pg.transform.rotozoom(pg.image.load(f'images/sprites/dead/dead{n}.png'), 0, 1.0) for n in range(16)]

    def __init__(self, game):
        super.__init__()
        self.game = game

    def die(self):pass
    def update(self):pass
    def draw(self, pos_x, pos_y):
        self.rect = self.image.get_rect()
        
