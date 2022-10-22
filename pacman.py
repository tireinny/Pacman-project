import pygame as pg
from character import Character
from vector import Vector
import timer


class Pacman(Character):
    def __init__(self):
        super.__init__()

    def center_pac(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        return Vector(self.rect.left, self.rect.top)

    def fire_portal():
        pass

    def reset(self):
        pass

    def update(self):
        pass
