# Please check for me. Thank you - Khoi 
'''Modified ghost point value to be 200 (which doubles if you eat ghosts quickly, which means we need a timer.py). 
Also added node point value, as each dot is worth 10 in the original, 
and modified screen width and height variables to be same as game.py -Charlie'''

import random
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 800
        self.screen_height = 1000
        # changes I made 
        # shoot portal every 4 minutes 
        # set points for ghosts 
        
        self.pacman_shoot_every = 240    # about every 240 seconds (4 minutes) at 60 fps 
        self.ghost_points = 200 
        self.node_points = 10 
        self.fruit_points = 100
        self.fruits = random.randint(self.screen_width, self.screen_height)           # spawn random locations
        
    def initialize_speed_settings(self):
        self.ghosts_speed = 1
        self.pacman_speed_factor = 1
        self.portal_speed_factor = 1

    def increase_speed(self):
        scale = self.speedup_scale
        self.pacman_speed_factor *= scale
        self.portal_speed_factor *= scale
