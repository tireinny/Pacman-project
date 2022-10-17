# Please check for me. Thank you - Khoi 

import random
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 224
        self.screen_height = 288

        # changes I made 
        # shoot portal every 4 minutes 
        # set points for ghosts 
        
        self.pacman_shoot_every = 240    # about every 240 seconds (4 minutes) at 60 fps 
        self.ghosts = 50
        self.fruits = random.randint(screen_width, screen_height)           # spawn random locations
        
    def initialize_speed_settings(self):
        self.ghosts_speed = 1
        self.pacman_speed_factor = 1
        self.portal_speed_factor = 1

    def increase_speed(self):
        scale = self.speedup_scale
        self.pacman_speed_factor *= scale
        self.portal_speed_factor *= scale
