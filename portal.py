# Portal 
# Demo file 
# Need to test and make changes before implement into main --- Khoi 
# 

# -------------------------------------------------------------------------------------
class Portal:
    SPEED = 30

    def __init__(self, rect, velocity=Vector()):
        self.portalAnimation = ['animation file goes here'] <<<--------------------- change this 
        self.currentFrame, self.active = 0, 0
        self.startF, self.endF = 0, 1  # len(self.enemyAnimation) - 1
        self.rect = rect
        self.velocity = velocity
        self.image = pg.transform.rotozoom(pg.image.load(self.portalAnimation[self.currentFrame]), 0, 0.06)

    def __repr__(self):
        return "Portal(rect={},velocity={})".format(self.rect, self.velocity)

    def create_portal(self, game):
        self.active = 0
        pX, pY = game.player.rect.centerx, game.player.rect.centery
        if game.player.currentAngle == 0:
            cX, cY = 10, -10
            self.velocity = Portal.SPEED * Vector(1, 0)
        elif game.player.currentAngle == 180:
            cX, cY = -35, -10
            self.velocity = Portal.SPEED * Vector(-1, 0)
        elif game.player.currentAngle == -90:
            cX, cY = -10, 10
            self.velocity = Portal.SPEED * Vector(0, 1)
        else:
            cX, cY = -10, -35
            self.velocity = Portal.SPEED * Vector(0, -1)
        self.rect.left, self.rect.top = pX + cX, pY + cY

    def remove_portal(self, x=350, y=660):
        self.active = 0
        self.rect.left, self.rect.top = x, y

    def change_frame(self):
        if self.startF <= self.currentFrame < self.endF:
            self.currentFrame += 1
        else:
            self.currentFrame = self.startF

    def limit_to_screen(self, game):
        self.rect.top = max(73, min(game.WINDOW_HEIGHT - self.rect.height - 55, self.rect.top))
        if game.m == 0:
            self.rect.left = max(-28, min(game.WINDOW_WIDTH - self.rect.width + 48, self.rect.left))
        else:
            self.rect.left = max(-300, min(game.WINDOW_WIDTH - self.rect.width + 48, self.rect.left))

    def move(self, game):
        self.change_frame()
        if self.check_collisions(game):
            self.velocity = Vector()
            self.active = 1
        if self.rect.top == 73 or self.rect.top == 663 and self.rect.left != 350 and self.rect.left != 400:
            self.active = 1
        if self.active == 0:
            self.rect.left += self.velocity.x
            self.rect.top += self.velocity.y
        self.limit_to_screen(game)

    def check_collisions(self, game):
        for j in range(len(game.walls)):
            if self.rect.colliderect(game.walls[j]):
                return True
        return False

    def draw(self, game):
        self.image = pg.transform.rotozoom(pg.image.load(self.portalAnimation[self.currentFrame]), 0, 0.06)
        game.surface.blit(self.image, self.rect)

    def update(self, game):
        self.check_collisions(game=game)
        self.move(game=game)
        self.draw(game=game)
