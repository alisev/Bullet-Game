import pygame as pg
import entity

'''
    Defines character class and objects.
'''

class Character(entity.Entity):
    '''
        Character data. Used for both the player and enemies.
        Has the following properties. The rest are defined in Entity class.
            move_x, move_y  Character's movement "vectors". Value usually switches between -1, 0 and 1. When value is -1 or 1 the character is moving across the screen, when 0 - it is still
            lives           Number of lives a character has. Each character has 1 life by default.
            isPlayer        Defines if character is the player
            children        Bullet sprite group
            value           Amount of points that the player is awarded with, when they shoot the enemy.
    '''
    def __init__(self, img = None, width = 0, height = 0):
        super().__init__(img, width, height)
        self.move_x = 0
        self.move_y = 0
        self.lives = 1
        self.children = pg.sprite.Group()
        self.value = 0

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        for child in self.children:
            child.kill()
            # TODO make an animation for the bullets, to make it look less jarring
        self.hitbox = (0,0,0,0)

    def gotHit(self):
        '''
            When character gets hit by a bullet, they lose a lifepoint.
        '''
        self.lives -= 1
        if self.lives == 0:
            self.remove()

def makeBallUFO(pos_x, pos_y):
    image = "ballUFO.png"
    enemy = Character(image)
    enemy.name = "Ball UFO"
    enemy.speed = 5
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 34
    enemy.height = 34
    enemy.hb_offset_x = 8
    enemy.hb_offset_y = 8
    enemy.value = 5
    return enemy

def makeBug(pos_x, pos_y):
    image = "bug.png"
    enemy = Character(image)
    enemy.name = "Bug alien"
    enemy.speed = 3
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 52
    enemy.height = 52
    enemy.hb_offset_x = 10
    enemy.hb_offset_y = 10
    enemy.lives = 10
    enemy.value = 20
    return enemy

def makeBoss(pos_x, pos_y):
    image = "boss1.png"
    enemy = Character(image)
    enemy.name = "Boss UFO"
    enemy.speed = 3
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 96
    enemy.height = 55
    enemy.hb_offset_x = 0
    enemy.hb_offset_y = 0
    enemy.lives = 25
    enemy.value = 100
    return enemy