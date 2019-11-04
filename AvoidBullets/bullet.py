'''
    Game assets, that aren't characters
'''

import pygame
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

# Functions that are used to create each type of bullet
def makeMeteor(pos_x, pos_y):
    image = pygame.image.load("sprites\\meteor.png").convert_alpha()
    bullet = Bullet(image)
    bullet.name = "Meteor"
    bullet.width = 16
    bullet.height = 16
    bullet.hb_offset_x = 4
    bullet.hb_offset_y = 4
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y
    return bullet

def makeBigBall(pos_x, pos_y, a):
    image = pygame.image.load("sprites\\ball1.png").convert_alpha()
    bullet = Bullet(image)
    bullet.name = "Small generic bullet"
    bullet.width = 22
    bullet.height = 22
    bullet.hb_offset_x = 4
    bullet.hb_offset_y = 4
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y

    bullet.angle = a
    bullet.radius = 30
    return bullet

def makeMediumBall(pos_x, pos_y, a):
    image = pygame.image.load("sprites\\ball2.png").convert_alpha()
    bullet = Bullet(image)
    bullet.name = "Medium generic bullet"
    bullet.width = 16
    bullet.height = 16
    bullet.hb_offset_x = 2
    bullet.hb_offset_y = 2
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y

    bullet.angle = a
    bullet.radius = 50
    return bullet

def makeSmallBall(pos_x, pos_y, a, variant):
    sprites = ["sprites\\ball3.png", "sprites\\ball3_bug.png"]
    image = pygame.image.load(sprites[variant]).convert_alpha()
    bullet = Bullet(image)
    bullet.name = "Small generic bullet"
    bullet.width = 10
    bullet.height = 10
    bullet.hb_offset_x = 2
    bullet.hb_offset_y = 2
    bullet.rect.x = pos_x
    bullet.rect.y = pos_y

    bullet.angle = a
    bullet.radius = 0
    return bullet
