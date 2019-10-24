'''
    Game assets, that aren't characters
'''

import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    '''
        Bullet object data. Used to shoot the player's character. Has the following properties:
            name            A name for bullet to differentiate.
            x_pos, y_pos    Bullet's position on screen
            width, height   Bullet's width and height
            speed           Bullet's movement speed
            image           Bullet's sprite
            hitbox          Defines bullet's hitbox
    '''
    def __init__(self, img):
        super().__init__()
        self.name = ""
        self.x_pos = 0
        self.y_pos = 0
        self.width = 0
        self.height = 0
        self.speed = 0
        self.color = constants.WHITE
        self.image = img
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)

    def recalcPos(self, x=0, y=0):
        '''
            Moves bullet in x direction.
        '''
        self.x_pos = self.x_pos + x * self.speed
        self.y_pos = self.y_pos + y * self.speed
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)

    def draw(self):
        '''
            Draws character on screen.
            screen - Pygame display object
        '''
        point_1 = [self.x_pos + self.width/2, self.y_pos]
        point_2 = [self.x_pos, self.y_pos + self.height]
        point_3 = [self.x_pos + self.width, self.y_pos + self.height]
        pygame.draw.polygon(constants.DISPLAYSURF, self.color, [point_1, point_2, point_3], 0)

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

        if isColliding:
            pass

    def remove(self):
        '''
            Removes bullet from screen.
        '''
        pass
    def drawHitbox(self):
        '''
            Draws character's hitbox border. For testing only.
        '''
        pygame.draw.rect(constants.DISPLAYSURF, (255,0,0), (self.x_pos, self.y_pos, self.width, self.height), 2)

ship = pygame.image.load("sprites\\ship.png").convert_alpha()
test = Bullet(ship)
test.name = "Test enemy"
test.width = 24
test.height = 24
test.speed = 3
test.color = constants.YELLOW