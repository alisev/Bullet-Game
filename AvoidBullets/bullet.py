'''
    Game assets, that aren't characters
'''

import pygame as pg
import entity
import os

class Bullet(entity.Entity):
    '''
        Bullet object data. Used to shoot the player's character.
        All properties are listed in the Entity class.
    '''
    def __init__(self, img):
        super().__init__(img)

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        self.hitbox = (0,0,0,0)

# Functions for simple bullet creation
def makeSmallBall(pos_x, pos_y, angle, variant):
    '''
        a           Angle
        variant     Version of sprite
    '''
    sprites = [os.path.join("sprites", "ball3.png"), os.path.join("sprites", "ball3_bug.png")]
    image = pg.image.load(sprites[variant]).convert_alpha()
    bullet = Bullet(image)
    bullet.name = "Small generic bullet"
    bullet.speed = 5
    bullet.width = 10
    bullet.height = 10
    bullet.hb_offset_x = 2
    bullet.hb_offset_y = 2
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    bullet.angle = angle
    bullet.radius = 0
    return bullet

def makeMeteor(pos_x, pos_y):
    img = pg.image.load(os.path.join("sprites", "meteor.png")).convert_alpha()
    bullet = Bullet(img)
    bullet.name = "Meteor"
    bullet.speed = 10
    bullet.width = 16
    bullet.height = 16
    bullet.hb_offset_x = 4
    bullet.hb_offset_y = 4
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    return bullet
