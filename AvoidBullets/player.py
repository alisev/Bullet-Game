import pygame as pg
from chara import Character
from constants import *
from bullet import Bullet

class Player(Character):
    '''
        Player class. Defines all entity and initial character properties.
    '''
    def __init__(self):
        img = "ship.png"
        super().__init__(img)
        self.name = "Player"
        self.width = 32
        self.height = 24
        self.speed = 4
        self.rect.x = SCREEN_X / 2 - 12
        self.rect.y = SCREEN_Y / 6 * 5
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)
        self.lives = PLAYER_MAX_LIVES

    def update(self):
        '''
            Updates player's position on screen
        '''
        self.move(self.move_x, self.move_y)
        self.keepWithinBounds()
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

    def keepWithinBounds(self):
        '''
            Checks if player isn't leaving the bounds.
            x_min, x_max, y_min, y_max - bound's corner positions.
        '''
        max_x = SCREEN_X - self.width
        max_y = SCREEN_Y - self.height
        if self.rect.x > max_x:
            self.rect.x = max_x
        elif self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > max_y:
            self.rect.y = max_y
        elif self.rect.y < 0:
            self.rect.y = 0

    def shoot(self):
        '''
            Creates a new bullet when player presses button.
            Returns the bullet object, so it can be added to sprite lists.
        '''
        blt = PlayerBullet(self.rect.x + 16, self.rect.y)
        self.children.add(blt)
        return blt

class PlayerBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        img = "ship_bullet.png"
        super().__init__(img)
        self.name = "Player's bullet"
        self.speed = 5
        self.width = 3
        self.height = 10
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def update(self):
        '''
            Enables movement of the bullet and checks for collissions and 
        '''
        self.move(0, -self.speed)
        self.updateHitbox()
        self.checkBounds(False, False, True, False)
