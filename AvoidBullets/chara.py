import pygame
import constants
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
    '''
    def __init__(self, img):
        super().__init__(img)
        self.move_x = 0
        self.move_y = 0
        self.lives = 1
        self.isPlayer = False
        self.children = None

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
        self.move(self.move_x, self.move_y)
        if self.isPlayer:
            self.checkBounds()
        self.updateHitbox()

    def checkBounds(self):
        '''
            Checks if character isn't leaving the bounds. Used mainly for player character.
            x_min, x_max, y_min, y_max - bound's corner positions.
        '''
        max_x = constants.SCREEN_X - self.width
        max_y = constants.SCREEN_Y - self.height
        if self.rect.x > max_x:
            self.rect.x = max_x
        elif self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > max_y:
            self.rect.y = max_y
        elif self.rect.y < 0:
            self.rect.y = 0

    def gotHit(self):
        '''
            When character is hit by a bullet, it loses life points.
        '''
        print(self.name, 'got hit')
        self.lives = self.lives - 1
        if self.lives == 0:
            if self.isPlayer:
                # TODO Calls GAME OVER
                pass
            else:
                # Removes character from screen
                self.remove()
            print(self.name, 'has died')

# Player character data
ship = pygame.image.load("sprites\\ship.png").convert_alpha()
player = Character(ship)
player.name = "Player"
player.rect.x = constants.SCREEN_X / 2 - 12
player.rect.y = constants.SCREEN_Y / 6 * 5
player.width = 32
player.height = 24
player.speed = 6
player.lives = 3
player.isPlayer = True

# Player specific function
def displayLives():
    '''
        Displays how many lives player has left.
    '''
    font = pygame.font.Font(None, 36)
    lives = font.render('Lives: ' + str(player.lives), False, constants.YELLOW)
    constants.DISPLAYSURF.blit(lives, [20, 20])

# List of each character
spriteList = pygame.sprite.Group()
spriteList.add(player)

def makeBallUFO(pos_x, pos_y):
    image = pygame.image.load("sprites\\ballUFO.png").convert_alpha()
    enemy = Character(image)
    enemy.name = "Ball UFO"
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 17
    enemy.height = 17
    enemy.hb_offset_x = 4
    enemy.hb_offset_y = 4
    enemy.children = pygame.sprite.Group()
    return enemy