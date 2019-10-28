import pygame
import constants
import bullet
from chara import player

rows = 8
countPerRow = 8
count = countPerRow * rows

speed_x = 2
speed_y = 3

bulletLists = []
for i in range(rows):
    bulletLists.append(pygame.sprite.Group())
allBullets = pygame.sprite.Group()

isPrepared = False

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
    if not isPrepared:
        for i in range(rows):
            prepare(bulletLists[i], i)
    
    for i in range(rows):
        moveRight = True if (i % 2 == 0) else False # Every other row moves left
        movement(bulletLists[i], moveRight)

    if len(allBullets)==0:
        return lvl + 1
    return lvl

def movement(group, moveRight):
    # Actual movement
    for obj in group:
        obj.rect.x = obj.rect.x + speed_x if moveRight else obj.rect.x - speed_x

        # Reappears on the other side of the screen, if the bullet disappears in x direction
        if obj.rect.x < 0:
            obj.rect.x = constants.SCREEN_X
        elif obj.rect.x > constants.SCREEN_X:
            obj.rect.x = 0

        obj.rect.y = obj.rect.y + speed_y

        obj.updateHitbox()

        obj.collide(player)

        if obj.rect.y > constants.SCREEN_Y:
            obj.remove()