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

isPrepared = False

def prepare(it, a):
    '''
        Prepares meteor groups, sprites and their start positions.
        it - array item's number, to which group belongs to
        a - x position offset
        (it == a)
    '''
    global isPrepared

    levelUtil.clearSpriteLists()
    levelUtil.bulletLists = levelUtil.createSpriteList(1)
    levelUtil.enemyLists = levelUtil.createSpriteList(col)

    x = [100, constants.SCREEN_X - 100 - 50]
    y = 101

    for i in range(col):
        for j in range(countPerCol):
            y = y - 120 if j > 0 else 0
            ufo = chara.makeBallUFO(x[i], y)
            for k in range(5):
                angle = 0
                if i == 0:
                    angle = -60 + 30 * k
                else:
                    angle = -120 - 30 * k
                ball = bullet.makeSmallBall(x[i] + 25, y + 25, angle, 0)
                ufo.children.add(ball)
                # levelUtil.bulletLists[0].add(ball) # TODO Evaluate if this is really necessary
                levelUtil.allSprites.add(ball)
            levelUtil.enemyLists[i].add(ufo)
            levelUtil.allSprites.add(ufo)
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
        moveUFO(levelUtil.enemyLists[i])

    return levelUtil.isGroupEmpty(levelUtil.allSprites, lvl)

def moveUFO (group):
    for ufo in group:
        ufo.move(0, speed_y)
        for ball in ufo.children:
            if ball.rect.y > 100:
                levelUtil.explode(ball, ufo.rect.x + 25, ufo.rect.y + 25, 5)
            else:
                ball.move(0, speed_y)

            ball.collide(chara.player)

            if ball.rect.x < -50 or ball.rect.x > constants.SCREEN_X + 50 or ball.rect.y > constants.SCREEN_Y + 50:
                ball.remove()

        if ufo.rect.y > constants.SCREEN_Y + 50:
            for ball in ufo.children:
                ball.remove()
            ufo.remove()




