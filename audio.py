import pygame as pg

class Audio:
    def __init__(self, sounds, playing):
        self.sounds = {}
        
        for sound in sounds: 
            for k, v in sound.items():
                self.sounds[k] = pg.mixer.Sound(v)
                
        self.playing = playing 
        
        
    def play_sound(self, sound):                                                           #<--------- Check before testing
        if self.playing and sound in self.sounds.keys():                                    #-Khoi
            self.sounds[sound].play()
            
    def toggle(self):
        self.playing = not self.playing
        pg.mixer.music.play(-1, 0.0) if self.playing else pg.mixer.music.stop()
               
    def game_over(self, game):
        pg.playing = False 
        pg.mixer.music.stop()
        self.play_sound(game.GAME_OVER)
    
