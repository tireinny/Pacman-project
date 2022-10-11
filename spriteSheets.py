import pygame as pg 


def get_image(sheet, width, height):
    image = pg.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0,0), (0, 0, width, height))
    return image