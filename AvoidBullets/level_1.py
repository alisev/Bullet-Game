import pygame
import constants
import bullet
from chara import player

rows = 5
countPerRow = 8
count = countPerRow * rows

speed_x = 1
speed_y = 3

# TODO move all bulletlists into an array and fix the code
bulletList_1 = pygame.sprite.Group()
bulletList_2 = pygame.sprite.Group()
bulletList_3 = pygame.sprite.Group()
bulletList_4 = pygame.sprite.Group()
bulletList_5 = pygame.sprite.Group()
allBullets = pygame.sprite.Group()

isPrepared = False
wallHits = [False, True] * 3

# prepares level
def prepare(group, a):
    global isPrepared
    x = 0
    y = -120 * a
    for i in range(countPerRow):
        x = constants.SCREEN_X/countPerRow * i
        meteor = bullet.makeMeteor(x, y)
        group.add(meteor)
        allBullets.add(meteor)
    isPrepared = True

# Updates all enemy and/or bullet position on screen
def update(lvl):
    # for cycle here after making an array holding bulletLists
    if not isPrepared:
        prepare(bulletList_1, 0)
        prepare(bulletList_2, 1)
        prepare(bulletList_3, 2)
        prepare(bulletList_4, 3)
        prepare(bulletList_5, 4)
    movement(bulletList_1, True)
    movement(bulletList_2, False)
    movement(bulletList_3, True)
    movement(bulletList_4, False)
    movement(bulletList_5, True)
    if len(allBullets)==0:
        return lvl + 1
    return lvl

def movement(group, moveRight):
    # Actual movement
    for obj in group:
        obj.rect.x = obj.rect.x + speed_x if moveRight else obj.rect.x - speed_x
        # reappears on the other side of the screen, if the bullet disappears in x direction
        if obj.rect.x < 0:
            obj.rect.x = constants.SCREEN_X
        elif obj.rect.x > constants.SCREEN_X:
            obj.rect.x = 0
        obj.rect.y = obj.rect.y + speed_y

        obj.updateHitbox()

        obj.collide(player)

        if obj.rect.y > constants.SCREEN_Y:
            obj.remove()