import pygame as pg
import chara
import constants
import bullet

class Player(chara.Character):
    '''
        Player class. Defines all entity and initial character properties.
    '''
    def __init__(self, img):
        super().__init__(img)
        self.name = "Player"
        self.width = 32
        self.height = 24
        self.speed = 5
        self.rect.x = constants.SCREEN_X / 2 - 12
        self.rect.y = constants.SCREEN_Y / 6 * 5
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)
        self.lives = 3

    def update(self):
        '''
            Updates player's position on screen
        '''
        self.move(self.move_x, self.move_y)
        self.checkBounds()
        self.updateHitbox()
        for blt in self.children:
            blt.update()

    def moveX(self, x=0):
        '''
            Enables player's movement by changing move_x value.
            x - direction in which character is moving. Usual values are -1, 1 and the default value 0 (not moving).
        '''
        self.move_x = x * self.speed

    def moveY(self, y=0):
        '''
            Enables player's movement by changing move_y value.
            y - direction in which character is moving. Usual values are -1, 1 and the default value 0 (not moving).
        '''
        self.move_y = y * self.speed

    def checkBounds(self):
        '''
            Checks if player isn't leaving the bounds.
            x_min, x_max, y_min, y_max - bound's corner positions.
        '''
        max_x = constants.SCREEN_X - self.width
        max_y = constants.SCREEN_Y - self.height
        if self.rect.x > max_x:
            self.rect.x = max_x
        elif self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > max_y:
            self.rect.y = max_y
        elif self.rect.y < 0:
            self.rect.y = 0

    def gotHit(self): # TODO test
        '''
            When player is hit by a bullet, they lose life points.
            Function returns either True or False value 
        '''
        self.removeLifePoint()
        if self.lives == 0:
            # TODO test gameover call
            return True
        return False

    def shoot(self):
        '''
            Creates a new bullet when player presses button.
            Returns the bullet object, so it can be added to sprite lists.
        '''
        image = pg.image.load("sprites\\ship_bullet.png").convert_alpha()
        blt = PlayerBullet(image, self.rect.x + 16, self.rect.y)
        self.children.add(blt)
        return blt

class PlayerBullet(bullet.Bullet):
    def __init__(self, img, pos_x, pos_y):
        super().__init__(img)
        self.name = "Player's bullet"
        self.width = 3
        self.height = 10
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def update(self):
        self.move(0, -5)
        # TODO check if it has collided with an enemy
        # TODO kill when bullet has left bounds
