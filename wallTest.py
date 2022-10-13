import sys 
import pygame as pg 

BLUE = (0,0, 255)

def test_wall():
    while(True):
        width = 28
        height =10
        area = width * height 
        t = 1 #dot
        x =0    #wall
        p = 2   #powerup
        i =3    #emptyspace
        tiles =[x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x, 
                x,t,t,t,t,t,t,t,t,t,t,t,t,x,x,t,t,t,t,t,t,t,t,t,t,t,t,x,
                x,p,x,x,x,x,t,x,x,x,x,x,t,x,x,t,x,x,x,x,x,t,x,x,x,x,p,x,
                x,t,x,x,x,x,t,x,x,x,x,x,t,t,t,t,x,x,x,x,x,t,x,x,x,x,t,x,
                x,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,x,
                x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x,
                x,t,x,x,x,x,t,x,x,t,x,x,x,x,x,x,x,x,t,x,x,t,x,x,x,x,t,x,
                x,t,t,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,x,x,t,t,t,t,t,t,x,
                x,x,x,x,x,x,t,x,x,x,x,x,i,x,x,i,x,x,x,x,x,t,x,x,x,x,x,x,
                x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,]

        screen_width = 1000
        screen_height = 700
        screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("pac man")
        screen.fill((0,0,0))
        start_coordinate_x = 10 
        start_coordinate_y = 10
        lemon = pg.image.load(f'images/sprites/fruits/lemon.png')
        for r in tiles:
            if r == 0 and (r+1 % 28 != 0):
                
                
                wall = pg.Rect(start_coordinate_x, start_coordinate_y, 20, 20 )
                pg.draw.rect(screen, BLUE, wall, 0, 20)
                start_coordinate_x +=10
            elif r ==1:
                screen.blit(lemon, (start_coordinate_x, start_coordinate_y))
            else:
                start_coordinate_y +=10
                start_coordinate_x =10
                wall = pg.Rect(start_coordinate_x, start_coordinate_y, 20, 20 )
                pg.draw.rect(screen, BLUE, wall, 0, 20)

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
        pg.display.update()   

def main():
    test_wall()


if __name__ == '__main__':
    main()