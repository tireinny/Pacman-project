import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        gameover_sound = pg.mixer.Sound('sounds/death_1.wav')

    def play_bg(self, music = 'sounds/siren_1.wav', loops = -1):
        pg.mixer.music.load(music)
        pg.mixer.music.play(loops, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/death_1.wav')
        self.play_bg()
        time.sleep(2.8)

    def game_start(self):
        pg.mixer.music.load('sounds/game_start.wav')
        pg.mixer.music.play(0, 0.0)
        time.sleep(4.5)
        self.play_bg()
