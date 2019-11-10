'''
    Game assets, that aren't characters
'''

import pygame as pg
import constants
import entity

class Bullet(entity.Entity):
    '''
        Bullet object data. Used to shoot the player's character.
        All properties are listed in the Entity class.
    '''
    def __init__(self, img):
        super().__init__(img)

    def collide(self, character):
        '''
            Checks if the bullet has collided with a character object.
            This method checks if bullet's and character's hitboxes are overlapping.
        '''
        x_min1 = self.hitbox[0]
        x_max1 = self.hitbox[0] + self.hitbox[2]
        x_min2 = character.hitbox[0]
        x_max2 = character.hitbox[0] + character.hitbox[2]

        x_box1 = (x_min1, x_max1) # x position interval for the bullet
        x_box2 = (x_min2, x_max2) # x position interval for the character
        
        y_min1 = self.hitbox[1]
        y_max1 = self.hitbox[1] + self.hitbox[3]
        y_min2 = character.hitbox[1]
        y_max2 = character.hitbox[1] + character.hitbox[3]

        # Checks if bullet has collided with the character
        isColliding = False
        if x_max1 >= x_min2 and x_max2 >= x_min1:
            if y_max1 >= y_min2 and y_max2 >= y_min1:
                isColliding = True
        
        # If collission has happened, character loses a life and bullet gets removed
        if isColliding:
            character.gotHit()
            self.remove()

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        self.hitbox = (0,0,0,0)

# Functions that are used to create each type of bullet
class Meteor(Bullet):
    def __init__(self, pos_x, pos_y):
        img = pg.image.load("sprites\\meteor.png").convert_alpha()
        super().__init__(img)
        self.name = "Meteor"
        self.speed = 10
        self.width = 16
        self.height = 16
        self.hb_offset_x = 4
        self.hb_offset_y = 4
        self.rect.x = pos_x
        self.rect.y = pos_y
