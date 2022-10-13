import pygame

class Dot():
    def _init__(self, x ,y, image):
        super(Dot, self). __init__(x,y)
        
        #sprite of dot
        self.image = image 
        
        # rect of sprite of dot 
        self.image_rect = pygame.Rect(x - 8, y - 8, 16, 16)
        
        # collision rect of dot 
        self.collision_rect = pygame.Rect(x - 1, y - 1, 2, 2)
    