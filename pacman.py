import pygame as pg
import pygame.sprite as Sprite
from vector import Vector
import timer

from vector import Vector


class Pacman(Sprite.Sprite):
    def __init__(self, game, screen, row, col):
        #super.__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game = game
        self.y = row
        self.x = col

        self.image = pg.image.load("images/sprites/pacman/pacman_left2.png")
        self.rect = self.image.get_rect()
        self.posn = (self.center_pac())
        print(self.posn)
        # self.posn = ((self.y, self.x))

        self.vel = Vector()

    def center_pac(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.y
        return Vector(self.rect.left, self.rect.top)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.posn += self.vel
        self.posn, self.rect = self.clamp(self.posn, self.rect)
        self.draw()

    def check_collisions(self):
        pass
    def die(self):
        pass

    def clamp(self, posn, rect):
        left, top = posn.x, posn.y
        width, height = rect.width, rect.height
        left = max(0, min(left, 800 - width))
        top = max(0, min(top, 1000- height))
        return Vector(x=left, y=top), pg.Rect(left, top, width, height)



