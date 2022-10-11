import pygame as pg
import sys
import spriteSheets as ss
from ghost import Ghost

WHITE =(255, 255, 255)
GRAY = (150, 150, 150)
LIGHTERGRAY = (200, 200, 200)
BLACK =(0,0,0)
RED = (255, 0, 0)
PINK =  (255, 184, 255)
AQUA = (0, 255, 255)
PASTELORANGE = (255, 184, 82)



class Start_screen:
    def __init__(self):
        pg.init()
        
        self.title_font = pg.font.Font(f'font/Emulogic-zrEw.ttf', 100) #import font file in folder "font for title"
        self.blink_ghost_names = False
        self.smaller_font = pg.font.Font(f"font/Emulogic-zrEw.ttf", 30)
        self.small_font = pg.font.Font(f"font/Emulogic-zrEw.ttf", 50) #for play and highscore button


        self.screen_width = 1000
        self.screen_height =700 
        self.backgroundColor = (0, 0, 0) #Black

        self.screen = pg.display.set_mode((self.screen_width, self.screen_height)) 
        pg.display.set_caption(f'Pacman Menu')

    def create_button(self,message, x, y, width, height, hover_color, normal_color): # function to create button, x, and y stands for the pixel coordinate, width and height is the dimenstion of the button, hover color is what color
                                                                                     # you want your button to be when it is hovered upon, normal_color is what the button color normally is. 
        mouse = pg.mouse.get_pos()# get the mouse's current position on the screen
        press = pg.mouse.get_pressed(3) # detect if mouse is clicked

        if x +width > mouse[0] > x and y + height > mouse[1] >y:  # detect if mouse is hovering over the location of the box
            pg.draw.rect(self.screen, hover_color, (x,y, width, height)) #turn the box into  the hover color
            if press[0] ==1:
                self.finish_start = True
                #self.title_music.stop()
        else:
            pg.draw.rect(self.screen, normal_color, (x, y, width, height))

        play_button_text = self.small_font.render(message, True, GRAY)
        self.screen.blit(play_button_text, (int(x), int(y)))

    def play(self):
        run = True
        while (run):

            start_text = self.title_font.render("Pac man", True, (255,255,255)) #get fonts ready
            play_text = self.small_font.render("Play Game", True, GRAY)
            highscore_text = self.small_font.render("High Scores", True, GRAY)

            self.screen.fill(self.backgroundColor)

            ghost = Ghost(self.screen)#create ghhost object to create other ghosts
            list_of_ghost =[ghost.red_ghost, ghost.pink_ghost, ghost.blue_ghost, ghost.yellow_ghost]#store ghosts in a list to print 
            

            self.screen.blit(start_text, [(self.screen_width - start_text.get_width())/2, 0])
            self.create_button("PLAY", (self.screen_width -play_text.get_width())/2, self.screen_height-200, 200, 60, LIGHTERGRAY, BLACK)
            self.create_button("HighScores", (self.screen_width -highscore_text.get_width())/2, self.screen_height-100, 510, 60, LIGHTERGRAY, BLACK)


            names_of_ghosts = '-SHADOW\n "BLINKY"\n -SPEEDY\n "PINKY"\n -BASHFUL \n"INKYl"\n -POKEY \n"CLYDE"'.splitlines()
            txt_cnt = 0 #used for seuquentially blinking the names of the ghost on the screen
                        #every increment is a name 
        
            

            list_of_colors = (RED, RED,  PINK, PINK, AQUA, AQUA,  PASTELORANGE, PASTELORANGE)
            color_index =0 #used to color the names of the ghost according to their colors


            list_of_posX = (self.screen_width -(self.screen_width - 200), self.screen_width -(self.screen_width - 500)) #used for positioning each name of the ghosts on the x axis
            pos_indexX = 0

            list_of_posY = (200, 200, 280, 280, 360, 360, 440, 440) #used for positioning each name of the ghosts on the y axis
            pos_indexY =0

            while(self.blink_ghost_names == False): #responsible for blinking the ghosts and names sequentially 
               
                for n in list_of_ghost: # loop used for drawing ghosts on screen before their name is introduced
                    for g in range(2):
                        if g == 0:
                            n.draw(list_of_posX[pos_indexX], list_of_posY[pos_indexY])
                            n.update() 
                            # pg.display.update()
                # if color_index%2 ==0:
                #     ghost.red_ghost.draw(list_of_posX[pos_indexX], list_of_posY[pos_indexY])
                #     ghost.red_ghost.update() 
                        # pg.display.update()
                        pg.time.wait(700) #timer for duration between each blink
                        if len(names_of_ghosts) <= txt_cnt: #break out of loop if the there are no more ghost names
                            self.blink_ghost_names = True
                            break
                        
                        text = self.smaller_font.render(names_of_ghosts[txt_cnt],True, list_of_colors[color_index]) #changes text and color based on the ghost
                        color_index +=1
                        
                        self.screen.blit(text, (list_of_posX[pos_indexX], list_of_posY[pos_indexY]))
                        # [self.screen.blit(redghost.sprites[n]) for n in len(redghost.sprites)]
                        
                        
                        pg.display.update()
                        
                        pos_indexY +=1
                        pos_indexX +=1
                        if pos_indexX > 1: pos_indexX=0 #reset pos x after the nickname is shown
                        if pos_indexY > 7: pos_indexY =0#reset pos y after the nickname is shown
                        txt_cnt +=1
            
            # for n in list_of_ghost:
            #     for i in range(2):
            #         if i == 1:
            #             n.draw(list_of_posX[pos_indexX], list_of_posY[pos_indexY])
            #             n.update() 
            
           
            while(self.blink_ghost_names == True): #used for keeping the names and ghosts on screen TODO: ghosts sprites are still need to be kept on screen 
               
                
                if len(names_of_ghosts) <= txt_cnt: break
                
                text = self.smaller_font.render(names_of_ghosts[txt_cnt],True, list_of_colors[color_index])
                color_index +=1
                
                self.screen.blit(text, (list_of_posX[pos_indexX], list_of_posY[pos_indexY]))
                # self.screen.blit(redghost.sprites[0], (200, 100))
                
                
                # redGhost.draw(200, 100)
               
                pos_indexY +=1
                pos_indexX +=1
                if pos_indexX > 1: pos_indexX=0
                if pos_indexY > 7: pos_indexY =0
                txt_cnt +=1



            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()   

def main():
    s = Start_screen()
    s.play()

if __name__ == '__main__':
    main()

    