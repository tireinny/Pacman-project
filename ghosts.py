import pygame
# Demo Only 

# -------------------------------------------------------------------------------------
class Enemy:
    SPEED = 6

    def __init__(self, rect, velocity=Vector()):
        self.enemyAnimation = [# png files go here for animations.]
        self.currentFrame, self.animationDirection, self.portalPower = 0, 0, 0
        self.startF, self.endF = 0, 1  # len(self.enemyAnimation) - 1
        self.rect = rect
        self.velocity = velocity
        self.enemy = pg.Rect(300, 100, 50, 50)
        self.image = pg.transform.rotozoom(pg.image.load(self.enemyAnimation[self.currentFrame]), 0, 0.06)

    def __repr__(self):
        return "Enemy(rect={},velocity={})".format(self.rect, self.velocity)

    def change_frame(self):
        if self.velocity == Vector():
            return
        if self.startF <= self.currentFrame < self.endF:
            self.currentFrame += 1
        else:
            self.currentFrame = self.startF

    def change_menu_frame(self):
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
        if self.velocity == Vector():
            return
        if game.level >= 3:
            self.portalPower = 1
        if game.m == 1:
            self.rect.left += self.velocity.x
            self.rect.top += self.velocity.y
            tempX = self.velocity.x
            tempY = self.velocity.y
            if tempX != 0 or tempY != 0:
                self.change_frame()
        else:
            self.change_frame()
            if not self.check_collisions(game):
                self.rect.left += self.velocity.x
                self.rect.top += self.velocity.y
            if self.check_collisions(game):
                self.rect.left -= self.velocity.x
                self.rect.top -= self.velocity.y
            if game.bluemode == 0:
                if self.velocity.x > 0:
                    self.startF, self.endF = 2, 3
                elif self.velocity.x < 0:
                    self.startF, self.endF = 0, 1
                elif self.velocity.y > 0:
                    self.startF, self.endF = 4, 5
                else:
                    self.startF, self.endF = 6, 7
            else:
                self.startF, self.endF = 8, 9
        self.limit_to_screen(game)

    def check_collisions(self, game):
        if game.bluePortal.active == 1 and game.oranPortal.active == 1 and self.portalPower == 1:
            if self.rect.colliderect(game.bluePortal.rect):
                game.audio.play_sound(4)
                self.rect.left, self.rect.top = game.oranPortal.rect.left, game.oranPortal.rect.top
                game.bluePortal.remove_portal()
                game.oranPortal.remove_portal(400)
            if self.rect.colliderect(game.oranPortal.rect):
                game.audio.play_sound(4)
                self.rect.left, self.rect.top = game.bluePortal.rect.left, game.bluePortal.rect.top
                game.bluePortal.remove_portal()
                game.oranPortal.remove_portal(400)

        for j in range(len(game.gWalls)):
            if self.rect.colliderect(game.gWalls[j]):
                return True
        return False

    def draw(self, game):
        self.image = pg.transform.rotozoom(pg.image.load(self.enemyAnimation[self.currentFrame]), 0, 0.06)
        game.surface.blit(self.image, self.rect)

    def update(self, game):
        self.check_collisions(game=game)
        self.move(game=game)
        self.draw(game=game)

# -------------------------------------------------------------------------------------
