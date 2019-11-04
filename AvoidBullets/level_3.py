import pygame
import math
import constants
import bullet
import chara
import levelUtil

rings = 10
count = 12
total = rings * count

speed_r = 2
speed_a = 1

threshold = 10 # radius of a ring, that triggers movement of the next ring

bug = chara.makeBug((constants.SCREEN_X / 2) - 25, -50)
bulletLists = []
for i in range(rings):
    bulletLists.append(pygame.sprite.Group())
allSprites = pygame.sprite.Group()

isPrepared = False

def prepare():
    global isPrepared

    for i in range(rings):
        angle = 0
        offset = 360/12
        for j in range(count):
            angle = angle + offset
            ball = bullet.makeSmallBall(bug.rect.x + 36, bug.rect.y + 36, angle, 1)
            bulletLists[i].add(ball)
            allSprites.add(ball)

    allSprites.add(bug)
    isPrepared = True

def update(lvl):
    if not isPrepared:
        prepare()

    if bug.rect.y < 150:
        speed = 3
        levelUtil.moveDown(bug, speed)
    else:
        th_reached = False

        for ring in bulletLists:
            for ball in ring:
                if ring == bulletLists[0] or ball.radius > 0 or (ball.radius == 0 and th_reached == True):
                    levelUtil.explode(ball, bug.rect.x + 36, bug.rect.y + 36, speed_r)
                    levelUtil.orbit(ball, bug.rect.x + 36, bug.rect.y + 36, speed_a)
                    if ball.radius == threshold:
                        th_reached = True
                    else:
                        th_reached = False
                ball.collide(chara.player)

                levelUtil.checkBounds(ball, 14)

    if len(allSprites) == 1:
        # At the end of the level the Bug Alien exits the screen
        levelUtil.moveDown(bug, -5)
        levelUtil.checkBounds(bug, 72)
    # needs a check, when all bulletlIsts are empty
    return levelUtil.isGroupEmpty(allSprites, lvl)

def draw():
    allSprites.draw(constants.DISPLAYSURF)