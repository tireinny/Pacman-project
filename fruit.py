
class Fruit(Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = self.game.surface

        self.image = pg.image.load('images/apple.png')
        self.rect = self.image.get_rect()

        self.rect.left = 259
        self.rect.top = 363
        self.x = float(self.rect.x)                                              #<--------- Check before testing
                                                                                 #-Khoi
    def width(self): return self.rect.width

    def height(self): return self.rect.height

    def check_edges(self):
        r = self.rect
        s_r = self.screen.get_rect()
        return r.right >= s_r.right or r.left <= 0

    def draw(self): self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()
