import pygame as pg
import character
import ghost
import spriteSheets
import start_screen
from vector import Vector
import copy
from start_screen import BLACK, Start_screen


from os import system

class Game:
    movement = {pg.K_LEFT: Vector(-1, 0),   # dictionary to map keys to Vector velocities
                pg.K_RIGHT: Vector(1, 0),
                pg.K_UP: Vector(0, -1),
                pg.K_DOWN: Vector(0, 1)
                }
    def __init__(self):
        pg.init() #intialize and set screen size
        self.screen_width = 800
        self.screen_height = 1000
        self.screen = pg.display.set_mode((self.screen_width,self.screen_height)) 
        # this block of code may need to be removed if pg is intialized elsewhere

        pg.display.set_caption("Pacman")
        self.background_img = pg.image.load(f'images/game_board.png')

        self.screen.fill((0,0,0))
        start_coordinate_x = 10 
        start_coordinate_y = 10

        t = 1 #dot
        x =0    #wall
        p = 2   #powerup
        i =3    #emptyspace
        w= 4 # door
        self.game_board =[
                [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x], 
                [x,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,x],
                [x,p,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,p,x],
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],
                [x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x],
                [x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x],
                [x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x],
                [x,t,t,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,t,t,x],
                [x,x,x,x,x,x,t,x,x,x,x,x,i,x,x,i,x,x,x,x,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,x,x,x,x,i,x,x,i,x,x,x,x,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,i,i,i,i,i,i,i,i,i,i,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,x,x,x,w,w,w,w,x,x,x,i,x,t,x,x,x,x,x,x],
                [i,i,i,i,i,i,t,i,i,x,i,i,i,i,i,i,i,i,x,i,i,t,i,i,i,i,i,i],
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,i,i,i,i,i,i,i,i,i,i,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],
                [x,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,x],
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],
                [x,p,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,p,x],
                [x,x,x,t,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,t,x,x,x],
                [x,x,x,t,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,t,x,x,x],
                [x,t,t,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,t,t,x],
                [x,t,x,x,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,x,x,t,x],
                [x,t,x,x,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,x,x,t,x],
                [x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x],
                [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x]]
        
      

        #self.sound = Sound() 
        #TODO enter a background song to play

        #self.character = Character() 
        #TODO declare character when possible

        #self.ghosts = Ghosts()
        #TODO create ghost class and create it

    def play(self):
        #self.sound.play()
        #TODO uncomment when sound has been made
        self.screen.blit(self.background_img, (((self.screen_width - self.background_img.get_width())/2),10))
        pg.display.update()


        tiles = copy.deepcopy(self.game_board)
        currentTile = 0
        pelletColor = (222, 161, 133)
        square =25
        print(len(tiles))
        for i in range(0, len(tiles) ):
            for j in range(len(tiles[0])):
                if tiles[i][j] == 0: pass# Draw wall
                  
                elif tiles[i][j] ==1: # Draw Tic-Tak
                    pg.draw.circle(self.screen, pelletColor,(j * square + square//.375, i * square + square//1), square//4.5)
                elif tiles[i][j] == 2: # Special Tic-Tak PELLETE COLOR
                    pg.draw.circle(self.screen, pelletColor,(j * square + square//.375, i * square + square//1), square//2.5)
                    tiles[i][j] =5
                    pg.time.wait(100)  
                    pg.display.update()
                elif tiles[i][j] ==5: #special tick tak black color
                    pg.draw.circle(self.screen, BLACK,(j * square + square//.375, i * square + square//1), square//2.5)           
                    tiles[i][j] =2
                    pg.time.wait(100)       
                    pg.display.update() 


                # elif tiles[i][j] == 6: #White Special Tic-Tak
                #     pg.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//2)
                pg.display.update()
                currentTile += 1

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
        
 #----------------------------------------------------------------------




#The below functions are currently located in start_screen.py and 
# I am unsure if it should stay there or migrate here or even go
# into another place. Regardless these are here just in case
def main(): 
   game = Game()
   start_screen = Start_screen(game)
   start_screen.play()

if __name__ == '__main__':
   main()




