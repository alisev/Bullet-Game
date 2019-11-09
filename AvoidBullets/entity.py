import constants
import pygame as pg

'''
    Entity class. Used as basis for both Bullet and Character class.
'''

class Entity(pg.sprite.Sprite):
    '''
        Entity data. Used to create both Bullet and Character class.
        Has the following properties:
            name            Entity's name.
            width, height   Entity's hitbox width and height
            color           Entity's color if it's srawn as a basic shape.
            image           Entity's sprite.
            rect            Necessary for drawing sprite
            hitbox          Entity's hitbox

    '''
    def __init__(self, img):
        super().__init__()
        self.name = ""
        self.width = 0
        self.height = 0
        self.image = img
        self.rect = self.image.get_rect()
        self.hb_offset_x = 0
        self.hb_offset_y = 0
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def drawHitbox(self):
        '''
            Draws character's hitbox border. For testing purposes only.
        '''
        pg.draw.rect(constants.DISPLAYSURF, (255,0,0), self.hitbox, 2)

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