import math
import pygame as pg
from UI import UI
import ghost
from pacman import Pacman
from scoreboard import Scoreboard
from sound import Sound
import spriteSheets
from node import Node
import sys
from queue import PriorityQueue
from vector import Vector
import copy
from start_screen import BLACK, Start_screen
from settings import Settings
from audio import Audio

from os import system


class Game:
    movement = {pg.K_LEFT: Vector(-1, 0),   # dictionary to map keys to Vector velocities
                pg.K_RIGHT: Vector(1, 0),
                pg.K_UP: Vector(0, -1),
                pg.K_DOWN: Vector(0, 1)
                }

    def __init__(self):
        pg.init()  # intialize and set screen size
        self.screen_width = 800
        self.screen_height = 1000
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.settings = Settings()
        # self.small_font = pg.font.Font(f"font/Emulogic-zrEw.ttf", 50)
        # self.UI = self.small_font.render("Play Game", True, GRAY)
        self.UI = UI(self.screen)
        # this block of code may need to be removed if pg is intialized elsewhere
        self.settings = Settings()
        pg.display.set_caption("Pacman")
        self.background_img = pg.image.load(f'images/game_board.png')
        self.scoreboard = Scoreboard(game=self)
        self.screen.fill((0, 0, 0))
        self.bg_sounds = Sound('sounds/siren_1.wav')
        self.pacman = Pacman(game=self, screen=self.screen, row=0, col=0)

        t = 1  # dot
        x = 0  # wall
        p = 2  # powerup
        i = 3  # emptyspace
        w = 4  # door
        g = 6  # ghost
        m = 7  # pacman
        self.game_board = [

            [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],  # 0
            [x, t, t, t, t, t, t, t, t, t, t, t, t, x, x, t, t, t, t, t, t, t, t, t, t, t, t, x],  # 1
            [x, p, x, x, x, x, t, x, x, x, x, x, t, x, x, t, x, x, x, x, x, t, x, x, x, x, p, x],  # 2
            [x, t, x, x, x, x, t, x, x, x, x, x, t, x, x, t, x, x, x, x, x, t, x, x, x, x, t, x],  # 3
            [x, t, x, x, x, x, t, x, x, x, x, x, t, x, x, t, x, x, x, x, x, t, x, x, x, x, t, x],  # 4
            [x, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, x],  # 5
            [x, t, x, x, x, x, t, x, x, t, x, x, x, x, x, x, x, x, t, x, x, t, x, x, x, x, t, x],  # 6
            [x, t, x, x, x, x, t, x, x, t, x, x, x, x, x, x, x, x, t, x, x, t, x, x, x, x, t, x],  # 7
            [x, t, t, t, t, t, t, x, x, t, t, t, t, x, x, t, t, t, t, x, x, t, t, t, t, t, t, x],  # 8
            [x, x, x, x, x, x, t, x, x, x, x, x, i, x, x, i, x, x, x, x, x, t, x, x, x, x, x, x],  # 9
            [x, x, x, x, x, x, t, x, x, x, x, x, i, x, x, i, x, x, x, x, x, t, x, x, x, x, x, x],  # 10
            [x, x, x, x, x, x, t, x, i, i, i, i, g, g, g, g, i, i, i, i, x, t, x, x, x, x, x, x],  # 11
            [x, x, x, x, x, x, t, x, i, x, x, x, w, w, w, w, x, x, x, i, x, t, x, x, x, x, x, x],  # 12
            [i, i, i, i, i, i, t, i, i, x, i, i, i, i, i, i, i, i, x, i, i, t, i, i, i, i, i, i],  # 13
            [x, x, x, x, x, x, t, x, i, x, x, x, x, x, x, x, x, x, x, i, x, t, x, x, x, x, x, x],  # 14
            [x, x, x, x, x, x, t, x, i, i, i, i, i, i, i, i, i, i, i, i, x, t, x, x, x, x, x, x],  # 15
            [x, x, x, x, x, x, t, x, i, x, x, x, x, x, x, x, x, x, x, i, x, t, x, x, x, x, x, x],  # 16
            [x, x, x, x, x, x, t, x, i, x, x, x, x, x, x, x, x, x, x, i, x, t, x, x, x, x, x, x],  # 17
            [x, x, x, x, x, x, t, x, i, x, x, x, x, x, x, x, x, x, x, i, x, t, x, x, x, x, x, x],  # 18
            [x, x, x, x, x, x, t, x, i, x, x, x, x, x, x, x, x, x, x, i, x, t, x, x, x, x, x, x],  # 19
            [x, t, t, t, t, t, t, t, t, t, t, t, t, x, x, t, t, t, t, t, t, t, t, t, t, t, t, x],  # 20
            [x, t, x, x, x, x, t, x, x, x, x, x, t, x, x, t, x, x, x, x, x, t, x, x, x, x, t, x],  # 21
            [x, t, x, x, x, x, t, x, x, x, x, x, t, x, x, t, x, x, x, x, x, t, x, x, x, x, t, x],  # 22
            [x, p, t, t, x, x, t, t, t, t, t, t, t, t, p, t, t, t, t, t, t, t, x, x, t, t, p, x],  # 23
            [x, x, x, t, x, x, t, x, x, t, x, x, x, x, x, x, x, x, t, x, x, t, x, x, t, x, x, x],  # 24
            [x, x, x, t, x, x, t, x, x, t, x, x, x, x, x, x, x, x, t, x, x, t, x, x, t, x, x, x],  # 25
            [x, t, t, t, t, t, t, x, x, t, t, t, t, x, x, t, t, t, t, x, x, t, t, t, t, t, t, x],  # 26
            [x, t, x, x, x, x, x, x, x, x, x, x, t, x, x, t, x, x, x, x, x, x, x, x, x, x, t, x],  # 27
            [x, t, x, x, x, x, x, x, x, x, x, x, t, x, x, m, x, x, x, x, x, x, x, x, x, x, t, x],  # 28
            [x, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, x],  # 39
            [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x]]  # 30
        #width of matrix is 28
        # pacman is at self.gameboard[28][15]
        #self.game_board[11][12] - [28][15]
        h_score = abs(11-28) + abs(12-15)

        # print(adjacency_list)

        self.intro_msc = 'sounds/game_start.wav'
        self.victory = 'sounds/extend.wav'
        #self.munch, self.bckgrnd_msc, self.death, = 0, 1, 2
        '''sounds = [{self.munch: 'sounds/munch_1.wav', 
                    self.bckgrnd_msc: 'sounds/siren_1.wav',
                    self.death:'sounds/death_1.wav'}]'''
        self.munch, self.death, = 0, 1
        sounds = [{self.munch: 'sounds/munch_1.wav', 
        self.death:'sounds/death_1.wav'}]
        self.audio = Audio(sounds=sounds, playing=True)
        #TODO enter a background song to play

        #self.character = Character()
        #TODO declare character when possible

        #self.ghosts = Ghosts()
        #TODO create ghost class and create it

    def play(self):
        #pg.mixer.music.load(self.intro_msc)
        #pg.mixer.music.play(1, 0.0)
        #self.screen.blit(self.background_img, (((self.screen_width - self.background_img.get_width())/2),10))
        
        

        pg.display.update()

        tiles = copy.deepcopy(self.game_board)
        pelletColor = (222, 161, 133)
        square = 25
        # print(len(tiles))
        ghosts = ghost.Ghost_manager(self.screen, self.settings)
        index = 1

        g_score = {}  # TODO: A*
        f_score = {}  # TODO: A*
        adjacency_list = {}
        p_row = 23
        p_col = 15

        runs = True
        pacman_position = (28,15)
        self.pacman.set_coords(440, 730)
        self.pacman.update()
        dict_of_ghost_coord = {}
        temp_ghost_coordinate = {}     
         
        while True:
            
            offset = 0
            current_row = 0
            current_pos = 0

            priority_queue = []  # TODO: A*

            t = 1   # dot
            x = 0   # wall
            p = 2   # powerup
            i = 3   # emptyspace
            w = 4   # door
            # power pellet
            g = 6   # ghost
            p = 7   # pacman
            ghost_color_code = 1
            self.check_events()  # checks what keys have been pressed
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background_img, ((
                (self.screen_width - self.background_img.get_width())/2), 10))
            self.UI.run()  
                     # a_star(tiles, (15, 12))

            for row in tiles:
                # adjacency_list[(current_row, current_pos)] = {}
                # print(adjacency_list)
                for index in row:
                    if index != x and index!=w and current_pos < 28:  # if space is a dot

                        #print("found a space for index " + str(offset))
                        if index == 1:  # Draw Tic-Tak
                            pg.draw.circle(self.screen, pelletColor, (current_pos * square +
                                           square//.375, current_row * square + square//1), square//4.5)
                           

                        elif index == 2:  # Special Tic-Tak PELLETE COLOR
                            pg.draw.circle(self.screen, pelletColor, (current_pos * square +
                                           square//.375, current_row * square + square//1), square//2.5)
                           

                        elif index == 5:  # special tick tak black color
                            pg.draw.circle(self.screen, BLACK, (current_pos * square +
                                           square//.375, current_row * square + square//1), square//2.5)
                            

                        elif index == 6:
                            dict_of_ghost_coord[ghost_color_code] = ((current_row, current_pos))
                            temp_ghost_coordinate[ghost_color_code] = ((current_row, current_pos))
                            ghosts.set_coordinate(current_row* square + square //.44, current_pos * square + square//2, ghost_color_code)
                            # print(dict_of_ghost_coord)
                            # print(dict_of_ghost_coord.get(1))
                            # TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                            

                            ghost_color_code += 1
                            h_score = abs(current_row-p_row) + \
                                abs(current_pos-p_col)
                        elif index == 7:
                            pacman_position = (current_row, current_pos)
                            self.pacman.y = current_row* square + square //.44
                            self.pacman.x = current_pos * square + square//2
                            
                            #print("found Pacman")
                        
                        # check if space to the right is a moveable space
                        if (current_pos + 1 < 28) and (current_pos + 1 != 4 and (tiles[current_row][current_pos+1]) != 0):
                            # adjacency_list[(current_row, current_pos )] = 
                            adjacency_list.setdefault((current_row, current_pos), {})['E'] =1
                            # print(adjacency_list)
                            # print(adjacency_list)
                            # adjacency_list[(current_row, current_pos)]['E'] = 1
                            #adjacency_list.setdefault(str([current_row, current_pos]), []).append(
                                #{'E': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['E'] =0
                                #{'E': 0})
                        
                        # check if space to the left is a moveable space
                        if (current_pos - 1 >= 0) and (current_pos - 1 != 4 and (tiles[current_row][current_pos-1]) != 0):
                            adjacency_list.setdefault((current_row, current_pos), {})['W'] =1
                                #{'W': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['W'] =0
                                #{'W': 0})
                              #  [current_row, current_pos-1])
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                        # check if above below is a moveable space
                        if (current_row+1 < len(tiles)) and (tiles[current_row+1][current_pos] != 4 and (tiles[current_row+1][current_pos]) != 0):
                            # print(tiles[12][12])
                            adjacency_list.setdefault((current_row, current_pos), {})['S'] =1    
                                #{'S': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['S'] =0
                                #{'S': 0})
                              #  [(current_row+1, current_pos)])
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                        # check if space above is a moveable space
                        if (current_row-1 >= 0) and (tiles[current_row-1][current_pos] != 4 and (tiles[current_row-1][current_pos]) != 0):
                            adjacency_list.setdefault((current_row, current_pos), {})['N'] =1
                                #{'N': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['N'] =0
                                #{'N': 0})
                              #  [(current_row-1, current_pos)])
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        current_pos += 1
                        offset += 1

                    elif index == x and current_pos < 28:
                        #print("found wall")
                          #  str([current_row, current_pos]), []).append([None, None])
                        # TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        # g_score.setdefault(
                        #     str([current_row, current_pos]), []).append(float('inf'))
                        current_pos += 1
                        offset += 1

                    elif index == w and current_pos < 28:
                        #print("found door")
                          #  str([current_row, current_pos]), []).append([None, None])
                        # TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        # g_score.setdefault(
                        #     str([current_row, current_pos]), []).append(float('inf'))

                        # check if space below is a moveable space
                        if (current_row+1 < len(tiles)) and (tiles[current_row+1][current_pos] != 4 and (tiles[current_row+1][current_pos]) != 0):
                            adjacency_list.setdefault((current_row, current_pos), {})['S'] =1
                                #{'S': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['S'] =0
                                #{'S]': 0})
                              #  [(current_row+1, current_pos)])
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end

                        # check if space above is a moveable space
                        if (current_row-1 >= 0) and (tiles[current_row-1][current_pos] != 4 and (tiles[current_row-1][current_pos]) != 0):
                            adjacency_list.setdefault((current_row, current_pos), {})['N'] =1
                                #{'N': 1})  # save coordinate of eligible space
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))#TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        else:
                            adjacency_list.setdefault((current_row, current_pos), {})['N'] =0
                            
                                #{'N': 0})
                              #  [(current_row-1, current_pos)])
                            #g_score.setdefault(str([current_row, current_pos]), []).append(float('inf'))   #TODO: A* these are used in A* algorithm refer to the youtube video in resource "A-Star A* Search in Python [Python Maze World- pyamaze]" Iam at 9:52 min into the video, watch from begining and follow to the end
                        current_pos += 1
                        # offset += 1

                current_pos = 0
                current_row += 1
                pg.display.update
               
                # for n in adjacency_list:
                # print(adjacency_list)
                
                # self.check_events()
            n = 1
            
            for coord in dict_of_ghost_coord.values():

                
                # temp_ghost_coordinate[ghost_color_code] = ((current_row, current_pos))
                path = a_star(adjacency_list,(coord[0], coord[1]), pacman_position)
                print((path.get(coord)[0]* square + square //.44, path.get(coord)[1] * square + square//2))
                print(path.get(coord)[0])
                print(temp_ghost_coordinate[n][0])
                print(temp_ghost_coordinate[n][1])
                if temp_ghost_coordinate[n][0] > path.get(coord)[0]:#used for changing the facing direction of the ghost 
                    ghosts.set_direction(1,n) #set direction to down
                elif temp_ghost_coordinate[n][0] < path.get(coord)[0]:
                    ghost.set_direction(3, n) #set direction to up
                
                if temp_ghost_coordinate[n][1] > path.get(coord)[1]:
                    ghosts.set_direction(2,n)
                elif temp_ghost_coordinate[n][1] < path.get(coord)[1]:
                    ghosts.set_direction(4,n)
                    
                ghosts.set_coordinate(path.get(coord)[0]* square + square //.44, path.get(coord)[1] * square + square//2, n)
                
            ghosts.update()
            self.pacman.update()
                
            # runs = False
                #self.character.update()
                #self.ghosts.update()
               
                #TODO uncomment when classes are implemented
            #TODO: A* implement GHOST AI MOVE HERE
            # print(adjacency_list)
            pg.display.flip()  # draws everything to the screen
            if(runs):
                self.bg_sounds.game_start()
                runs = False

    def check_events(self):
        #print("\n\n\nCheck event entered\n\n\n")
        for event in pg.event.get():  # standart check to see what has been pressed
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
            #print(f'Game has received #{self.movement[key]} button')
            self.pacman.vel += 3 * self.movement[key]

        # Right now only prints out what key has been pressed but should be modified once
        # we have pacman actually moving around

    def check_keyup_events(self, event):
        key = event.key
        if key in self.movement.keys():
            self.pacman.vel = Vector()   # Note: Escape key stops the ship
        # elif key in movement.keys(): ship.vel = Vector()

 #----------------------------------------------------------------------
def heuristics(cell1, cell2):
        x1,y1 =cell1
        x2,y2 = cell2 
        
        return abs(x1 -x2) + abs(y1 -y2)

def a_star(grid, ghost_pos, pacman_pos):
    start = (ghost_pos[0],ghost_pos[1])
    # adjacency_list.setdefault((current_row, current_pos), {})['S'] =1
    gridkeys = grid.keys()
   
    # print([key for key in gridkeys])

    g_score = {cell: float('inf') for cell in gridkeys}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in gridkeys}
    f_score[start] = heuristics(start, pacman_pos)
    
    open = PriorityQueue()
    open.put((heuristics(start, pacman_pos), heuristics(start, pacman_pos), start))
    path = {}
    while not open.empty(): 
        current_cell = open.get()[2]
        if current_cell == pacman_pos:
            break
        for d in 'ESNW': #means east south north west 
            # print(grid[current_cell][d])
            if grid[current_cell][d] == True:
                if d == 'E':
                    child_cell = (current_cell[0], current_cell[1]+1)

                if d == 'W':
                    child_cell = (current_cell[0], current_cell[1]-1)

                if d == 'N':
                    child_cell = (current_cell[0]-1, current_cell[1])
                    
                if d == 'S':
                    child_cell = (current_cell[0]+1, current_cell[1])

                temp_g_score = g_score[current_cell] +1
                temp_f_score = temp_g_score + heuristics(child_cell, pacman_pos)
                
                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open.put((temp_f_score, heuristics(child_cell, pacman_pos), child_cell))
                    path[child_cell] = current_cell
                    
    forward_path ={}
    cell =(pacman_pos)
    while cell!= start:
        forward_path[path[cell]] = cell
        cell = path[cell]
    
    
    # print(forward_path)
    return forward_path


#The below functions are currently located in start_screen.py and
# I am unsure if it should stay there or migrate here or even go
# into another place. Regardless these are here just in case
def main():
   game = Game()
   start_screen = Start_screen(game)
   start_screen.play()


if __name__ == '__main__':
   main()
