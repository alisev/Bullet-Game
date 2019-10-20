import pygame
import constants

'''
    Defines character class and objects.
'''

class Character():
    '''
        Character data. Used for both the player and enemies. Has the following properties:
            name            Character's name.
            x_pos, y_pos    Character's position on screen
            width, height   Character's width and height
            speed           Character's movement speed
            move_x, move_y  Character's movement "vectors". Value usually switches between -1, 0 and 1. When value is -1 or 1 the character is moving across the screen, when 0 - it is still
            hp              Character's health points.
            color           Character's color. Only used as long as the character doesn't have sprites
            sprites         Character's sprite list.
            isPlayer        Defines if character is the player
    '''
    def __init__(self):
        self.name = ""
        self.x_pos = 0
        self.y_pos = 0
        self.width = 0
        self.height = 0
        self.speed = 0
        self.move_x = 0
        self.move_y = 0
        self.hp = 0
        self.color = constants.WHITE
        self.sprites = []
        self.isPlayer = False

    def draw(self, screen):
        '''
            Draws character on screen.
            screen - Pygame display object
        '''
        point_1 = [self.x_pos + self.width/2, self.y_pos]
        point_2 = [self.x_pos, self.y_pos + self.height]
        point_3 = [self.x_pos + self.width, self.y_pos + self.height]
        pygame.draw.polygon(screen, self.color, [point_1, point_2, point_3], 0)

    def moveX(self, x=0):
        '''
            Enables character movement by changing move_x value.
            x - direction in which character is moving. Usual values are -1, 1 and the default value 0 (not moving).
        '''
        self.move_x = x * self.speed

    def moveY(self, y=0):
        '''
            Enables character movement by changing move_y value.
            y - direction in which character is moving. Usual values are -1, 1 and the default value 0 (not moving).
        '''
        self.move_y = y * self.speed

    def recalcPos(self):
        '''
            Recalculates character's position on screen. If it is the player's character, then an additional function checks if player isn't leaving the screen's bounds.
        '''
        self.x_pos = self.x_pos + self.move_x
        self.y_pos = self.y_pos + self.move_y
        if self.isPlayer:
            self.checkBounds()

    def checkBounds(self):
        '''
            Checks if character isn't leaving the bounds. Used mainly for player character.
        '''
        max_x = constants.SCREEN_X - self.width
        max_y = constants.SCREEN_Y - self.height
        if self.x_pos > max_x:
            self.x_pos = max_x
        elif self.x_pos < 0:
            self.x_pos = 0
        if self.y_pos > max_y:
            self.y_pos = max_y
        elif self.y_pos < 0:
            self.y_pos = 0

# Player character data
# NOTE: Doesn't contain information on player's health points or sprites.
player = Character()
player.name = "Player"
player.x_pos = constants.SCREEN_X / 2 - 12
player.y_pos = constants.SCREEN_Y / 6 * 5
player.width = 32
player.height = 24
player.speed = 3
player.isPlayer = True

# Test enemy character data
test = Character()
test.name = "Test enemy"
test.width = 24
test.height = 24
test.speed = 3
test.color = constants.YELLOW
