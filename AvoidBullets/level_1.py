import pygame
import constants
import bullet
from chara import player
from levelUtil import isGroupEmpty

rows = 4
countPerRow = 9
count = countPerRow * rows

speed_x = 4
speed_y = 8

bulletLists = []
for i in range(rows):
    bulletLists.append(pygame.sprite.Group())
allSprites = pygame.sprite.Group()

isPrepared = False

def prepare(group, a):
    '''
        Prepares meteor groups, sprites and their start positions.
        group - sprite group that is being prepared.
        a - y position offset
    '''
    global isPrepared

    x = 0
    y = -120 * a
    for i in range(countPerRow):
        if countPerRow > 1: # Prevents division with 0
            x = constants.SCREEN_X/(countPerRow - 1) * i
        meteor = bullet.makeMeteor(x, y)
        group.add(meteor)
        allSprites.add(meteor)
    isPrepared = True

def update(lvl):
    '''
        Prepares level (if needed) and goes through bulletLists to update each sprite group's position.
        As soon as all meteors are gone, level is increased.
        lvl - current level
    '''
    if not isPrepared:
        for i in range(rows):
            prepare(bulletLists[i], i)
    
    for i in range(rows):
        moveRight = True if (i % 2 == 0) else False # Every other row moves left
        movement(bulletLists[i], moveRight)

    return isGroupEmpty(allSprites, lvl)

def movement(group, moveRight):
    '''
        Goes through all group's items, updates their position and removes sprites if it has collided or left the screen.
        group - sprite group
        moveRight - if True, all group's sprites are moving to the right side. Otherwise they would move left.
    '''
    for obj in group:
        obj.rect.x = obj.rect.x + speed_x if moveRight else obj.rect.x - speed_x

        # Reappears on the other side of the screen, if the bullet disappears in x direction
        if obj.rect.x < -50:
            obj.rect.x = constants.SCREEN_X + 50
        elif obj.rect.x > constants.SCREEN_X + 50:
            obj.rect.x = -50

        obj.rect.y += speed_y

        obj.updateHitbox()

        obj.collide(player)

        if obj.rect.y > constants.SCREEN_Y:
            obj.remove()

def draw():
    '''
        Draws all bullets.
    '''
    allSprites.draw(constants.DISPLAYSURF)