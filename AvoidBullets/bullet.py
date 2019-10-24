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

    def recalcPos(self, x=0, y=0):
        '''
            Moves bullet in x direction as long as the bullet is 'active'.
        '''
        if self.isActive:
            move_x = x * self.speed
            move_y = y * self.speed
            self.move(move_x, move_y)
            self.hitbox = (self.rect.x, self.rect.y, self.width, self.height)

    def collide(self, character):
        '''
            Checks if the bullet has collided with a character object.
            This method checks if bullet's and character's hitboxes are overlapping.
        '''
        if self.isActive == False:
            return

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

ship = pygame.image.load("sprites\\ship.png").convert_alpha()
test = Bullet(ship)
test.name = "Test enemy"
test.width = 24
test.height = 24
test.speed = 3
test.color = constants.YELLOW

spriteList = pygame.sprite.Group()
spriteList.add(test)