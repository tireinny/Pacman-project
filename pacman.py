import pygame as pg
import pygame.sprite as Sprite


class Pacman(Sprite):
    def __init__(self, game, screen, row, col):
        super.__init__()
        self.screen = screen
        self.game = game
        self.row = row
        self.col = col
        self.rect = self.image.get_rect()

    def center_pac(self):
        self.rect.centerx = self.screen_rect.centerx


    def draw(self):
        pass

    def update(self):
        pass




