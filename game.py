import pygame as pg
import character
import ghost
import spriteSheets
import start_screen
import vector

from os import system

class Game:
    movement = {pg.K_LEFT: vector(-1, 0),   # dictionary to map keys to Vector velocities
                pg.K_RIGHT: vector(1, 0),
                pg.K_UP: vector(0, -1),
                pg.K_DOWN: vector(0, 1)
                }
    def __init__(self):
        pg.init() #intialize and set screen size
        self.screen_width = 1000
        self.screen_height = 700
        self.screen = pg.display.set_mode((1000,700)) 
        # this block of code may need to be removed if pygame is intialized elsewhere

        pg.display.set_caption("Pacman")

        #self.sound = Sound() 
        #TODO enter a background song to play

        #self.character = Character() 
        #TODO declare character when possible

        #self.ghosts = Ghosts()
        #TODO create ghost class and create it

    def play(self):
        #self.sound.play()
        #TODO uncomment when sound has been made

        while True:
            self.check_events() #checks what keys have been pressed
            
            #self.character.update()
            #self.ghosts.update()
            #TODO uncomment when classes are implemented
            
            pg.display.flip() # draws everything to the screen

    def check_events(self):
        for event in pg.event.get(): # standart check to see what has been pressed
            if event.type == pg.QUIT: 
                pg.quit()
                system.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        key = event.key

        if key in self.movement.keys(): print(f'Game has received {self.movement[key]} button')
        # Right now only prints out what key has been pressed but should be modified once
        # we have pacman actually moving around


#The below functions are currently located in start_screen.py and 
# I am unsure if it should stay there or migrate here or even go
# into another place. Regardless these are here just in case
#def main(): 
#    g = Game()
#    g.play()

#if __name__ == '__main__':
#    main()




