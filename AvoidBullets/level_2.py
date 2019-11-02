import pygame
import math
import constants
import bullet
import chara
from levelUtil import isGroupEmpty

# UFO count
col = 2
countPerCol = 5

speed_y = 5
speed_1 = 1
speed_2 = 2
speed_3 = 3

UFOLists = []
for i in range(col):
    UFOLists.append(pygame.sprite.Group())
allSprites = pygame.sprite.Group()


isPrepared = False

def prepare(it, a):
    '''
        Prepares meteor groups, sprites and their start positions.
        it - array item's number, to which group belongs to
        a - x position offset
        (it == a)
    '''
    global isPrepared

    x = constants.SCREEN_X/(col + 1) * (a + 1)
    y = 0
    for i in range(countPerCol):
        y = y - 120 * i # TODO Change to minus
        ufo = chara.makeBallUFO(x, y)
        UFOLists[it].add(ufo)
        # TODO use loop here
        allSprites.add(ufo)
        for j in range(3):
            pos_x = x
            pos_y = y + 5 + 2 * j
            ball = None
            if j == 0:
                ball = bullet.makeBigBall(pos_x, pos_y)
            elif j == 1:
                ball = bullet.makeMediumBall(pos_x, pos_y)
            else:
                ball = bullet.makeSmallBall(pos_x, pos_y)
            ufo.children.add(ball)
            allSprites.add(ball)
    isPrepared = True

def update(lvl):
    '''
        Prepares level (if needed) and goes through bulletLists to update each sprite group's position.
        As soon as all meteors are gone, level is increased.
        lvl - current level
    '''
    if not isPrepared:
        for i in range(col):
            prepare(i, i)
    
    for i in range(col):
        moveUFO(UFOLists[i])

    return isGroupEmpty(allSprites, lvl)

def moveUFO (group):
    for ufo in group:
        moveDown(ufo)
        counter = 0
        for ball in ufo.children:
            moveDown(ball)
            if ufo.rect.y < 150:
                orbit(ball, ufo.rect.x + 12, ufo.rect.y + 12, counter)
            else:
                explode(ball, ufo.rect.x + 12, ufo.rect.y + 12)
            ball.collide(chara.player)
            counter = counter + 1

def moveDown(item):
    item.rect.y = item.rect.y + speed_y
    item.updateHitbox()

def orbit(obj, origin_x, origin_y, a):
    '''
        Moves sprite in a circular path. Used for ball animation.
        obj - sprite to move
        origin_x, origin_y - path's center coordinates
    '''
    obj.angle = obj.angle + 0.2 * (a + 1)
    obj.rect.x = origin_x + math.cos(obj.angle) * obj.radius
    obj.rect.y = origin_y + math.sin(obj.angle) * obj.radius

def explode(obj, origin_x, origin_y):
    obj.radius = obj.radius + 5
    obj.rect.x = origin_x + math.cos(obj.angle) * obj.radius
    obj.rect.y = origin_y + math.cos(obj.angle) * obj.radius
    pass

def draw():
    '''
        Draws all bullets.
    '''
    allSprites.draw(constants.DISPLAYSURF)



