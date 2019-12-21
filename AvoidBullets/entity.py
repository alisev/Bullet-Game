import pygame as pg
from constants import *
import os
import util

'''
    Entity class. Used as basis for both Bullet and Character class.
'''

class Entity(pg.sprite.Sprite):
    '''
        Entity data. Used to create both Bullet and Character class.
        Has the following properties:
            name            Entity's name.
            speed           Entity's base speed
            width, height   Entity's hitbox width and height
            color           Entity's color if it's srawn as a basic shape.
            image           Entity's sprite.
            rect            Necessary for drawing sprite
            hitbox          Entity's hitbox
    '''
    def __init__(self, img):
        super().__init__()
        self.name = ""
        self.speed = 0
        self.width = 0
        self.height = 0
        self.image = util.loadSprite(img)
        self.rect = self.image.get_rect()
        self.hb_offset_x = 0
        self.hb_offset_y = 0
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def move(self, move_x, move_y):
        '''
            Recalculates entity's position on screen.
            move_x, move_y - Variables, which define how much the entity has moved.
        '''
        self.rect.x += move_x
        self.rect.y += move_y
        self.updateHitbox()

    def updateHitbox(self):
        '''
            Updates entity's hitbox.
        '''
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def checkBounds(self, checkTop = True, checkRight = True, checkBot = True, checkLeft = True):
        '''
            Checks if bullet hasn't left the screen's bounds.
            Edge_x and edge_y represent sprite's dimensions.
            checkTop, checkRight, checkBot, checkLeft   Indicates which screen sides, need to be checked.
        '''
        edge_x = self.width + 2 * self.hb_offset_x
        edge_y = self.height + 2 * self.hb_offset_y
        if (checkTop == True and self.rect.y < -edge_x or
            checkRight == True and self.rect.x > SCREEN_X or
            checkBot == True and self.rect.y > SCREEN_Y or
            checkLeft == True and self.rect.x < -edge_y):
            self.remove()

    def getEntityPos(self):
        '''
            Gets entity's coordinates on screen.
        '''
        return [self.rect.x, self.rect.y]