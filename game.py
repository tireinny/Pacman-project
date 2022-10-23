import math
import pygame as pg
import character
import ghost
from pacman import Pacman
from scoreboard import Scoreboard
import spriteSheets
from node import Node
import sys

from vector import Vector
import copy
from start_screen import BLACK, Start_screen
from settings import Settings



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
        self.settings = Settings()
        # this block of code may need to be removed if pg is intialized elsewhere
        self.settings = Settings()
        pg.display.set_caption("Pacman")
        self.background_img = pg.image.load(f'images/game_board.png')
        self.scoreboard = Scoreboard(game =self)
        self.screen.fill((0,0,0))
        start_coordinate_x = 10 
        start_coordinate_y = 10

        self.pacman = Pacman(game=self, screen=self.screen, row=800, col=400)
        
        t = 1 # dot
        x = 0 # wall
        p = 2 # powerup
        i = 3 # emptyspace
        w = 4 # door
        g = 6 # ghost
        m = 7 # pacman
        self.game_board =[
            
                [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x],#0
                [x,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,x],#1
                [x,p,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,p,x],#2
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],#3
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],#4
                [x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x],#5
                [x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x],#6
                [x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x],#7
                [x,t,t,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,t,t,x],#8
                [x,x,x,x,x,x,t,x,x,x,x,x,i,x,x,i,x,x,x,x,x,t,x,x,x,x,x,x],#9
                [x,x,x,x,x,x,t,x,x,x,x,x,i,x,x,i,x,x,x,x,x,t,x,x,x,x,x,x],#10
                [x,x,x,x,x,x,t,x,i,i,i,i,g,g,g,g,i,i,i,i,x,t,x,x,x,x,x,x],#11
                [x,x,x,x,x,x,t,x,i,x,x,x,w,w,w,w,x,x,x,i,x,t,x,x,x,x,x,x],#12
                [i,i,i,i,i,i,t,i,i,x,i,i,i,i,i,i,i,i,x,i,i,t,i,i,i,i,i,i],#13
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],#14
                [x,x,x,x,x,x,t,x,i,i,i,i,i,i,i,i,i,i,i,i,x,t,x,x,x,x,x,x],#15
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],#16
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],#17
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],#18
                [x,x,x,x,x,x,t,x,i,x,x,x,x,x,x,x,x,x,x,i,x,t,x,x,x,x,x,x],#19
                [x,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,x],#20
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],#21
                [x,t,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,t,x],#22
                [x,p,t,t,x,x,t,t,t,t,t,t,t,t,p,t,t,t,t,t,t,t,x,x,t,t,p,x],#23
                [x,x,x,t,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,t,x,x,x],#24
                [x,x,x,t,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,t,x,x,x],#25
                [x,t,t,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,t,t,x],#26
                [x,t,x,x,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,x,x,t,x],#27
                [x,t,x,x,x,x,x,x,x,x,x,x,t,x,x,m,x,x,x,x,x,x,x,x,x,x,t,x],#28
                [x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x],#39
                [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x]]#30
        #width of matrix is 28
        # pacman is at self.gameboard[28][15]
        #self.game_board[11][12] - [28][15]
        h_score = abs(11-28) + abs(12-15)
        
        # print(adjacency_list)



        #self.sound = Sound() 
        #TODO enter a background song to play

        #self.character = Character() 
        #TODO declare character when possible

        #self.ghosts = Ghosts()
        #TODO create ghost class and create it

    def play(self):
        #self.sound.play()
        #TODO uncomment when sound has been made
        #self.screen.blit(self.background_img, (((self.screen_width - self.background_img.get_width())/2),10))
        pg.display.update()

        tiles = copy.deepcopy(self.game_board)
        pelletColor = (222, 161, 133)
        square =25
        print(len(tiles))
        ghosts = ghost.Ghost_manager(self.screen, self.settings)
        index = 1
        
        g_score = {} #TODO: A*
        f_score = {} #TODO: A*
        adjacency_list = {}
        p_row = 23
        p_col = 15

        runs = True

        while True:
          
            offset = 0
            current_row = 0
            current_pos = 0
            
            priority_queue = []  #TODO: A*


            
            
          
            t = 1   # dot
            x = 0   # wall
            p = 2   # powerup
            i = 3   # emptyspace
            w = 4   # door
                    # power pellet
            g = 6   # ghost
            p = 7   # pacman
            ghost_color_code =1            
            self.check_events() #checks what keys have been pressed
            self.screen.fill((0,0,0))
            self.screen.blit(self.background_img, (((self.screen_width - self.background_img.get_width())/2),10))
            ghosts.update()
            self.pacman.update()
            #TODO: A* find the Heuristic cost and declare it either here or inside the for-loop below (i dont know where yet)

            for row in tiles:
                    for index in row:
                        if index  != (x and w) and current_pos < 28: #if space is a dot 
                            
                            #print("found a space for index " + str(offset))
                            if index ==1: # Draw Tic-Tak
                                pg.draw.circle(self.screen, pelletColor,(current_pos * square + square//.375, current_row * square + square//1), square//4.5)
                            
                            elif index == 2: # Special Tic-Tak PELLETE COLOR
                                pg.draw.circle(self.screen, pelletColor,(current_pos * square + square//.375, current_row * square + square//1), square//2.5)
                            
                            elif index ==5: #special tick tak black color
                                pg.draw.circle(self.screen, BLACK,(current_pos * square + square//.375, current_row * square + square//1), square//2.5)
                            
                            elif index ==6:  
                                ghosts.set_coordinate(current_pos * square + square//.44, current_row * square + square//2, ghost_color_code)
                                ghost_color_code+=1
                            elif index == 7:
                                pass
                                #print("found Pacman")
                            current_pos +=1
                            offset+=1
                            
                        elif index == x and current_pos < 28:
                            #print("found wall")
                            adjacency_list.setdefault(str([current_row, current_pos]),[]).append( [None, None])
                            g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            current_pos +=1
                            offset+=1
                            
                        elif index == w and current_pos < 28: 
                            #print("found door")
                            adjacency_list.setdefault(str([current_row, current_pos]),[]).append( [None, None])
                            g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                            if (current_row+1 < len(tiles)) and (tiles[current_row+1][current_pos ] != x and w): #check if space below is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row+1,current_pos)])
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            
                            if (current_row-1 >= 0) and (tiles[current_row-1][current_pos ] != x and w): #check if space above is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row-1, current_pos)])     
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))   #TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end        
                                current_pos +=1
                                offset+=1
            
                    current_pos =0
                    current_row +=1
                    pg.display.update


            # SETTING THE SCORES ONCE FOR G SCORE AND F SCORE
            if(runs):
                print("HAVE ENTERED RUNS IF")
                for row in tiles:
                    for index in row:
                        if index  != (x and w) and current_pos < 28: #if space is a dot 
                            
                            #print("found a space for index " + str(offset))
                            if index ==1: # Draw Tic-Tak
                                pg.draw.circle(self.screen, pelletColor,(current_pos * square + square//.375, current_row * square + square//1), square//4.5)
                                g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                                f_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                            
                            elif index == 2: # Special Tic-Tak PELLETE COLOR
                                pg.draw.circle(self.screen, pelletColor,(current_pos * square + square//.375, current_row * square + square//1), square//2.5)
                                g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                                f_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                            
                            elif index ==5: #special tick tak black color
                                pg.draw.circle(self.screen, BLACK,(current_pos * square + square//.375, current_row * square + square//1), square//2.5)
                                f_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                            
                            elif index ==6:  
                                ghosts.set_coordinate(current_pos * square + square//.44, current_row * square + square//2, ghost_color_code)
                                g_score.setdefault(str([current_row, current_pos]), []).append(float(0))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                                ghost_color_code+=1
                                h_score = abs(current_row-p_row) + abs(current_pos-p_col)
                            elif index == 7:
                                f_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))
                                #print("found Pacman")
                                                                        
                            if (current_pos + 1 < 28) and (current_pos + 1  != (x and w)):  #check if space to the right is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([current_row, current_pos+1])#save coordinate of eligible space
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                                
                            
                            if (current_pos - 1 >=0) and (current_pos - 1  != (x and w)):  #check if space to the left is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([current_row, current_pos-1])
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                            if (current_row+1 < len(tiles)) and (tiles[current_row+1][current_pos] != (x and w)): #check if above below is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row+1,current_pos)])
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            
                            if (current_row-1 >= 0) and (tiles[current_row-1][current_pos] != (x and w)): #check if space above is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row-1, current_pos)])
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            current_pos +=1
                            offset+=1
                            
                        elif index == x and current_pos < 28:
                            #print("found wall")
                            adjacency_list.setdefault(str([current_row, current_pos]),[]).append( [None, None])
                            g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            current_pos +=1
                            offset+=1
                            
                        elif index == w and current_pos < 28: 
                            #print("found door")
                            adjacency_list.setdefault(str([current_row, current_pos]),[]).append( [None, None])
                            g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                            if (current_row+1 < len(tiles)) and (tiles[current_row+1][current_pos ] != x and w): #check if space below is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row+1,current_pos)])
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            
                            if (current_row-1 >= 0) and (tiles[current_row-1][current_pos ] != x and w): #check if space above is a moveable space
                                adjacency_list.setdefault(str([current_row, current_pos]),[]).append([(current_row-1, current_pos)])     
                                #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))   #TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end        
                                current_pos +=1
                                offset+=1
            
                    

                    current_pos =0
                    current_row +=1
                    pg.display.update    
            
            runs = False
            
                #self.character.update()
                #self.ghosts.update()
                #TODO uncomment when classes are implemented
            #print(adjacency_list)
            #TODO: A* implement GHOST AI MOVE HERE 
            

            pg.display.flip() # draws everything to the screen


    def check_events(self):
        #print("\n\n\nCheck event entered\n\n\n")
        for event in pg.event.get(): # standart check to see what has been pressed
            if event.type == pg.QUIT: 
                pg.quit()
                #system.exit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        #print("\n\n\KEYDOWN event entered\n\n\n")
        key = event.key

        if key in self.movement.keys(): 
            #print(f'Game has received {self.movement[key]} button')
            self.pacman.vel += 3 * self.movement[key]

        # Right now only prints out what key has been pressed but should be modified once
        # we have pacman actually moving around

    def check_keyup_events(self, event):
        key = event.key
        if key in self.movement.keys(): 
            self.pacman.vel = Vector()   # Note: Escape key stops the ship
        # elif key in movement.keys(): ship.vel = Vector()
        
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




