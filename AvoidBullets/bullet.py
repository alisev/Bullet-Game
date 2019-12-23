'''
    Game assets, that aren't characters
'''

import pygame as pg
import entity
import util
import constants

class Bullet(entity.Entity):
    '''
        Bullet object data. Used to shoot the player's character.
        All properties are listed in the Entity class.
    '''
    def __init__(self, img = None, width = 0, height = 0):
        super().__init__(img, width, height)

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        self.hitbox = (0,0,0,0)

# Functions for simple bullet creation
def makeSmallBall(pos_x, pos_y, angle, variant):
    '''
        angle       Angle
        variant     Version of sprite
    '''
    sprites = ["ball3.png", "ball3_bug.png"]
    bullet = Bullet(sprites[variant])
    bullet.name = "Small generic bullet"
    bullet.speed = 5
    bullet.width = 10
    bullet.height = 10
    bullet.hb_offset_x = 3
    bullet.hb_offset_y = 3
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    bullet.angle = angle
    bullet.radius = 0
    return bullet

def makeMeteor(pos_x, pos_y):
    img = "meteor.png"
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

def makeHomingMissile(pos_x, pos_y):
    sprites = ["aim_still.png", "aim_move.png"]
    bullet = Bullet(sprites[0])
    bullet.name = "Homing missile"
    bullet.speed = 4
    bullet.width = 10
    bullet.height = 22
    bullet.hb_offset_x = 2
    bullet.hb_offset_y = 0
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    bullet.sprite_still = util.loadSprite(sprites[0])
    bullet.sprites_move = util.loadSprite(sprites[1])
    return bullet

def makeLaser(pos_x, pos_y):
    img = "laser.png"
    bullet = Bullet(img)
    bullet.name = "Laser"
    bullet.width = 16
    bullet.height = 16
    bullet.hb_offset_x = 0
    bullet.hb_offset_y = 0
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    return bullet

def makeLaserHint(start_pos, end_pos):
    surface_size = util.calcVector(start_pos, end_pos)
    bullet = Bullet(None, surface_size[0], surface_size[1])
    bullet.image.set_colorkey(constants.COLOR["black"])
    bullet.rect = bullet.image.get_rect()
    # todo blit line on screen
    return bullet
