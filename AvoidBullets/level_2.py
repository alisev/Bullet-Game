import pygame
import math
import constants
import bullet
import chara
import levelUtil

# UFO count
col = 2
countPerCol = 5

speed_y = 5

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
            makeBall = [bullet.makeBigBall, bullet.makeMediumBall, bullet.makeSmallBall]
            ball = makeBall[j](pos_x, pos_y)
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

    return levelUtil.isGroupEmpty(allSprites, lvl)

def moveUFO (group):
    for ufo in group:
        moveDown(ufo)
        counter = 0
        for ball in ufo.children:
            moveDown(ball)
            if ufo.rect.y < 100:
                levelUtil.orbit(ball, ufo.rect.x + 25, ufo.rect.y + 25, 0.05, counter)
            else:
                levelUtil.explode(ball, ufo.rect.x + 25, ufo.rect.y + 25, 3)

            ball.collide(chara.player)

            if ball.rect.x < -50 or ball.rect.x > constants.SCREEN_X + 50 or ball.rect.y > constants.SCREEN_Y + 50:
                ball.remove()

            counter = counter + 1
        if ufo.rect.y > constants.SCREEN_Y + 50:
            for ball in ufo.children:
                ball.remove()
            ufo.remove()

def moveDown(item):
    item.rect.y = item.rect.y + speed_y
    item.updateHitbox()

def draw():
    '''
        Draws all bullets.
    '''
    allSprites.draw(constants.DISPLAYSURF)



