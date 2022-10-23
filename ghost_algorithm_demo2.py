# Demo only

import pygame
import random

# Window size
WINDOW_WIDTH      = 420
WINDOW_HEIGHT     = 465

GRID_SIZE = WINDOW_HEIGHT // 21

MAP_WIDTH  = 19
MAP_HEIGHT = 21
MAP = [ "###################", 
        "#        #        #",
        "# ## ### # ### ## #",
        "#                 #",
        "# ## # ##### # ## #",
        "#    #   #   #    #",
        "#### ### # ### ####",
        "#### #       # ####",
        "#### # ## ## # ####",
        "<      #   #      >",
        "#### # ##### # ####",
        "#### #   c   # ####",
        "#### # ##### # ####",
        "#        #        #",
        "# ## ### # ### ## #",
        "#  #           #  #",
        "## # # ##### # # ##",
        "#    #   #   #    #",
        "# ###### # ###### #",
        "#                 #",
        "###################" ]

BLACK    = (  0,   0,   0)
YELLOW   = (255, 255,   0)
BLUE     = (  0,   0, 254)
RED      = (255,   0,   0)
LIGHTBLUE= (161, 255, 254)
PINK     = (255, 192, 203)
ORANGE   = (255, 165,   0)


def pixelPosToGridPos( pixel_x, pixel_y ):
    """ Map a window-pixel position to a map-grid position """
    return ( pixel_x // GRID_SIZE, pixel_y // GRID_SIZE )

def gridPosToPixelPos( grid_x, grid_y ):
    """ Map a grid position to a window-position position """
    return ( grid_x * GRID_SIZE, grid_y * GRID_SIZE )
    
def getMapColour( x, y ):
    """ Convert map symbols into colours """
    symbol = MAP[y][x]
    if ( symbol == '#' ):
        return BLUE
    elif ( symbol == 'c' ):
        return YELLOW
    elif ( symbol == 'b' ):   # "Shadow" / "Blinky"
        return RED
    elif ( symbol == 'p' ):   # "Speedy" / "Pinky"
        return PINK
    elif ( symbol == 'i' ):   # "Bashful" / "Inky"
        return LIGHTBLUE
    elif ( symbol == 'o' ):   # "Pokey" / "Clyde"
        return ORANGE
    return BLACK


class GhostSprite( pygame.sprite.Sprite ):
    """ A pacman-like ghost sprite """

    def __init__( self, grid_x, grid_y, colour ):
        super().__init__()
        self.image = pygame.Surface( ( GRID_SIZE, GRID_SIZE), pygame.SRCALPHA )
        self.image.fill( colour )
        self.rect = self.image.get_rect()
        self.rect.topleft = gridPosToPixelPos( grid_x, grid_y )
        self.direction = random.choice( [ 'N', 'S', 'E', 'W' ] ) 


    def moveToGrid( self, grid_x, grid_y ):
        """ Allow position to be reset """
        self.rect.topleft = gridPosToPixelPos( grid_x, grid_y )

    def availableMoves( self ):
        """ Consult the map to see where is good to go from here.
            We only consider walls, not other NPCs """
        map_x, map_y = pixelPosToGridPos( self.rect.x, self.rect.y )
        exits = []
        # handle wrap-around, where it's possible to go "off grid"
        if ( map_x <= 0 or map_x >= MAP_WIDTH-1 ):
            exits = [ 'E', 'W' ]
        else:
            # otherwise consult the map
            if ( MAP[ map_y-1 ][ map_x ] != '#' ):
                exits.append( 'N' )
            if ( MAP[ map_y ][ map_x+1 ] != '#' ):
                exits.append( 'E' )
            if ( MAP[ map_y+1 ][ map_x ] != '#' ):
                exits.append( 'S' )
            if ( MAP[ map_y ][ map_x-1 ] != '#' ):
                exits.append( 'W' )
        return exits

    def getOppositeDirection( self ):
        """ Return the compass-opposite of our current movement direction """
        opposites = { 'N':'S', 'S':'N', 'E':'W', 'W':'E' };
        return opposites[ self.direction ]

    def moveForward( self ):
        """ Move in the current direction.  Generally we use the map
            to keep us in-bounds, but on the wrap-around we can get
            close to the edge of the map, so use special handling for
            warping """
        # handle wrap-around avenue
        map_x, map_y = pixelPosToGridPos( self.rect.x, self.rect.y )
        if ( MAP[ map_y ][ map_x ] == '<' ):
            self.direction = 'W'
            self.rect.x = (MAP_WIDTH-1) * GRID_SIZE
        elif ( MAP[ map_y ][ map_x ] == '>' ):
            self.direction = 'E'
            self.rect.x = 0
            
        
        # Whichever direction we're moving in, go forward
        if ( self.direction == 'N' ):
            self.rect.y -= GRID_SIZE
        elif ( self.direction == 'E' ):
            self.rect.x += GRID_SIZE
        elif ( self.direction == 'S' ):
            self.rect.y += GRID_SIZE
        else:  # W
            self.rect.x -= GRID_SIZE


    def update( self ):
        """ Move the ghost, mostly forward, never backwards (unless dead-end)
            At an intersection, possibly turn """
        exits = self.availableMoves()
        # Generally: Keep moving in current direction, never u-turn 
        opposite = self.getOppositeDirection()
        # 60% change of continuing forward at an intersection
        if ( self.direction in exits and ( len( exits ) == 1 or random.randrange( 0,100 ) <= 60 ) ):
            pass
        elif ( self.direction not in exits and len( exits ) == 1 ):
            self.direction = exits[0]   # maybe u-turn
        else:  # more than 1 exit
            if ( opposite in exits ):
                exits.remove( opposite )
            self.direction = random.choice( exits )
        # Move-it- Move-it
        self.moveForward()



###
### MAIN
###
pygame.init()
window  = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), pygame.HWSURFACE )
pygame.display.set_caption("Pac Algorithm")

# Make background image of map
background = pygame.Surface( ( WINDOW_WIDTH, WINDOW_HEIGHT ), pygame.SRCALPHA )
for y in range( MAP_HEIGHT ):
    for x in range( MAP_WIDTH ):
        rect = pygame.Rect( x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE )
        pygame.draw.rect( background, getMapColour( x, y ), rect )

# Make the Ghosts
blinky = GhostSprite( 9, 7, RED )
inky   = GhostSprite( 8, 9, LIGHTBLUE )
pinky  = GhostSprite( 9, 9, PINK )
pokey  = GhostSprite(10, 9, ORANGE )
ghosts = pygame.sprite.Group() 
ghosts.add( [ blinky, inky, pinky, pokey ] )

# Ghosts move periodically
next_ghost_movement = pygame.time.get_ticks() + 1000

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    time_now = pygame.time.get_ticks()
    # Handle user-input
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            running = False

    # Movement keys
    keys = pygame.key.get_pressed()
    if ( keys[pygame.K_UP] ):
        print("up")
    elif ( keys[pygame.K_DOWN] ):
        print("down")
    elif ( keys[pygame.K_LEFT] ):
        print("left")
    elif ( keys[pygame.K_RIGHT] ):
        print("right")
    elif ( keys[pygame.K_ESCAPE] ):
        # Reset the ghosts home
        blinky.moveToGrid( 9, 7 )
        inky.moveToGrid( 8, 9 )
        pinky.moveToGrid( 9, 9 )
        pokey.moveToGrid( 10, 9 )
        next_ghost_movement = time_now + 1000 

    # move the ghosts
    if ( time_now > next_ghost_movement ):
        ghosts.update()
        next_ghost_movement = time_now + 100 

    # Update the window, but not more than 60fps
    window.blit( background, ( 0, 0 ) )
    ghosts.draw( window )
    pygame.display.flip()
        
    # Clamp FPS
    clock.tick(30)

pygame.quit()
