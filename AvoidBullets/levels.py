import pygame as pg
import bullet
import chara
import paths
import position
import player
import frame
import util

'''
    Contains functions that handles all level logic and rendering.
'''

class Level():
    '''
        Contains functions that handles all level logic and rendering.
        level_num   Current level number
        levels      A dict containing all levels
        level       Current level
    '''
    def __init__(self, levelList):
        self.level_num = 0
        self.levels = levelList
        self.level = self.levels[self.level_num]

    def resetGame(self):
        player.player.reset()
        self.level_num = 0
        for level in self.levels:
            level.reset()
        self.level = self.levels[self.level_num]
    
    def call(self):
        '''
            Calls current level's game logic, updates level_num when level is completed and returns True or False value to indicate if the game has been beaten.
        '''
        levelCount = len(self.levels)
        data = {"done": False,
                "points": 0}
        if self.level_num < levelCount:
            gameUpdateData = self.level.update(self.level_num)
            self.level_num = gameUpdateData["level_num"]
            data["points"] = gameUpdateData["points"]
            if self.level_num == levelCount:
                data["done"] = True
            else:
                self.level = self.levels[self.level_num]
        return data

    def draw(self):
        '''
            Draws current level.
        '''
        screen = pg.display.get_surface()
        if self.level_num < len(self.levels):
            self.level.allSprites.draw(screen)

    def entityCollission(self, entity):
        '''
            Checks for collissions between passed entity (player) and each group in BulletLists.
            entity  Passed entity object
        '''
        for group in self.level.bulletLists:
            list = pg.sprite.spritecollide(entity, group, True)
            if len(list) > 0:
                entity.gotHit()

    def groupCollission(self, group):
        '''
            Checks for collissions between the passed group and each group in EnemyLists.
            group   Passed group object
        '''
        earned_pts = 0
        for enemyGroup in self.level.enemyLists:
            hitEnemies = pg.sprite.groupcollide(enemyGroup, group, False, True)
            for enemy in hitEnemies:
                enemy.gotHit()
                earned_pts += enemy.value
        return earned_pts

class LevelBlueprint():
    '''
        A blueprint class for level creation.
        bullet_rows     Amount of rows with bullets
        bullets_perRow  Amount of bullets per row
        bullet_count    Total amount of bullets
        enemyGroupCount Number of enemy groups
        enemy_perGroup  Number of enemies per group
        value           Amount of points player is rewarded with, when they finish the level.
        allSprites      All sprites in current level
        bulletLists     Array of bullet sprite groups
        enemyLists      Array of enemy sprite groups
        isPrepared      Indicates if the level has been prepared for gameplay
    '''
    def __init__(self, bulletRows, bulletCount, enemyGroups = 1, enemyCount = 0, value = 0):
        self.bullet_rows = bulletRows
        self.bullets_perRow = bulletCount
        self.bullet_count = self.bullet_rows * self.bullets_perRow

        self.enemyGroupCount = enemyGroups
        self.enemy_perGroup = enemyCount
        self.value = value

    def reset(self):
        self.allSprites = pg.sprite.Group()
        self.bulletLists = []
        self.enemyLists = []

        self.isPrepared = False

    def createSpriteList(self, n):
        '''
            Creates sprite group arrays. Used for bulletLists and enemyLists.
            Function is called by populateBulletLists and populateEnemyLists
        '''
        array = []
        for i in range(n):
            array.append(pg.sprite.Group())
        return array

    def populateBulletLists(self):
        self.bulletLists = self.createSpriteList(self.bullet_rows)

    def populateEnemyLists(self):
        self.enemyLists = self.createSpriteList(self.enemyGroupCount)

    def clearSpriteLists(self):
        '''
            Clears all sprite lists.
        '''
        self.allSprites.empty()
        self.bulletLists.clear()
        self.enemyLists.clear()

    def update(self, lvl):
        '''
            Updates game logic in current level.
            lvl     Current level
        '''
        self.prepare()
        self.updateLevel()
        return self.isAllSpritesEmpty(lvl)

    def updateLevel(self):
        '''
            Empty function for updating level to avoid errors in prepare() function.
            This function is properly defined and used in each level's class.
        '''
        pass

    def prepare(self):
        '''
            Prepares level for the gameplay.
        '''
        if not self.isPrepared:
            self.populateBulletLists()
            self.populateEnemyLists()
            self.prepareLevel()
            self.isPrepared = True

    def prepareLevel(self, row):
        '''
            Empty function for level preparation to avoid errors in prepare() function.
            This function is properly defined and used in each level's class.
        '''
        pass

    def isGroupEmpty(self, group):
        '''
            Checks if given sprite group is empty.
            group   Sprite group to be checked
        '''
        if len(group) == 0:
            return True
        return False

    def isAllSpritesEmpty(self, lvl):
        data = {"level_num": lvl,
                "points": 0}
        if self.isGroupEmpty(self.allSprites):
            data["level_num"] += 1
            data["points"] = self.value
        return data


class Level_1(LevelBlueprint):
    def __init__(self):
        super().__init__(3, 5, value = 10)
    
    def prepareLevel(self):
        '''
            Defines each bullet group's parameters (width, height, position) and calculates each bullet's coordinate.
            Then creates bullets and places them in the appropriate groups.
        '''
        sprite_width = 24
        widths = [320, 320, 640]
        heights = [-320, 320, 0]
        offsets = [(-320, 0),
                    (1280, -720),
                    (80 - sprite_width/2, -800)]
        for row in range(self.bullet_rows):
            positions = position.distributeEven(self.bullets_perRow,
                                                widths[row],
                                                heights[row],
                                                offsets[row][0],
                                                offsets[row][1])
            for i in range(self.bullets_perRow):
                x = positions[i][0]
                y = positions[i][1]
                meteor = bullet.makeMeteor(x, y)
                self.allSprites.add(meteor)
                self.bulletLists[row].add(meteor)

    def updateLevel(self):
        '''
            Prepares enemies and bullets at the start of the level and handles game logic.
            Level 1 shoots meteors.
        '''
        for i in range(self.bullet_rows):
            for obj in self.bulletLists[i]:
                if i == 0:
                    obj.move(obj.speed, obj.speed)
                elif i == 1:
                    obj.move(-obj.speed, obj.speed)
                else:
                    obj.move(0, obj.speed)
                obj.checkBounds(False, False, True, False)

class Level_2(LevelBlueprint):
    def __init__(self):
        super().__init__(10, 12, 1, 1, value = 50)

    def prepareLevel(self):
        '''
            Creates a bug enemy and it's bullets.
        '''
        self.bug = chara.makeBug(364, -50)
        for row in range(self.bullet_rows):
            prepareCircle(self.bullets_perRow, (self.bug.rect.x + 36, self.bug.rect.y + 36), 1, [self.bug.children, self.bulletLists[row], self.allSprites])
        addToGroups(self.bug, [self.allSprites, self.enemyLists[0]])
        self.bullets_gone = False
        self.bug_leave_done = False
        self.bug_enter_done = False

    def updateLevel(self):
        if self.bug_enter_done == False:
            self.bug_enter_done = self.bugMovement(150)
        else:
            self.bullets_gone = self.ringMovement()
        if self.bullets_gone:
            self.bug_leave_done = self.bugMovement(-55, False)
        if self.bug_leave_done:
            self.bug.remove()

    def bugMovement(self, target, moveDown = True):
        '''
            Bug enters the screen.
            Returns bool if the action is completed.
            target      Target y coordinate
            moveDown    Bug is descending
        '''
        speed = self.bug.speed if moveDown else -self.bug.speed
        if (self.bug.rect.y < target and moveDown) or (self.bug.rect.y > target and moveDown == False):
            self.bug.move(0, speed)
            return False
        return True

    def ringMovement(self):
        '''
            Bullets orbit around the bug and move away
        '''
        th_reached = False
        speed_r = 2
        speed_a = 1
        emptyBulletGroups = []
        for ring in self.bulletLists:
            for ball in ring:
                if ring == self.bulletLists[0] or ball.radius > 0 or (ball.radius == 0 and th_reached == True):
                    th_reached = bulletMovement(self.bug, ball, speed_r, speed_a)
            if len(ring) == 0:
                emptyBulletGroups.append(True)
        if len(emptyBulletGroups) == self.bullet_rows:
            return True
        return False

class Level_3(LevelBlueprint):
    def __init__(self):
        bullet_count = [10, 18, 24, 30]
        super().__init__(len(bullet_count), bullet_count, 1, 1, value = 500)

    def prepareMissiles(self, group):
        y = self.boss.rect.y
        for i in range(self.bullets_perRow[group]):
            blt = bullet.makeHomingMissile(393, y + 5)
            blt.flyOff = False
            addToGroups(blt, [self.boss.children, self.bulletLists[group], self.allSprites])

    def prepareLasers(self, group):
        for i in range(self.bullets_perRow[group]):
            laser = bullet.makeLaser(-18, -18)
            laser.org_image = laser.image
            laser.scaleSprite((0.5, 0.5))
            addToGroups(laser, [self.bulletLists[group], self.allSprites])

    def prepareLevel(self):
        x = 352
        y = -55
        self.boss = chara.makeBoss(x, y)
        self.boss_has_entered = False
        prepOrder = [self.prepareMissiles, prepareCircle, prepareCircle, prepareCircle]
        for i in range(self.bullet_rows):
            if prepOrder[i] is not prepareCircle:
                prepOrder[i](i)
            else:
                prepareCircle(self.bullets_perRow[i], (self.boss.rect.x + 48, self.boss.rect.y + 27), 0, [self.bulletLists[i], self.boss.children, self.allSprites])
        addToGroups(self.boss, [self.enemyLists[0], self.allSprites])
        self.frame = frame.Frame(40)
        self.act = 0

    def updateLevel(self):
        '''
            Prepares enemies and bullets at the start of the level and handles game logic.
        '''
        acts = [self.bossEntrance, self.launchMissiles, self.bulletWaves]
        if self.act < len(acts):
            acts[self.act]()

    def bossEntrance(self):
        '''
            Boss sprite enters the screen.
        '''
        boss_target_y = 100
        if self.boss.rect.y < boss_target_y:
            self.boss.move(0, 5)
            for child in self.boss.children:
                child.move(0, 5)
            return
        self.act += 1

    def launchMissiles(self):
        '''
            Boss launches missiles that follow player's movements.
        '''
        group = self.bulletLists[0]
        for blt in group:
            if paths.calcDistance(player.player, blt) < 100 or blt.flyOff == True:
                paths.explode(blt, blt.rect.x, blt.rect.y, int(blt.speed/3))
                blt.flyOff = True
            elif blt.radius > 0 or self.frame.maxReached():
                paths.followEntity(player.player, blt, False)
            blt.checkBounds(True, True, True, True)
        self.frame.add()
        if self.isGroupEmpty(group):
            self.act += 1
            self.frame.count = 0

    def rotatingLaser(self):
        '''
            Rotating lasers.
        '''
        group = self.bulletLists[1]
        pos = [(352, 150), (430, 150)]
        i = 0
        self.frame.max_count = 30
        for laser in group:
            if not self.frame.maxReached():
                laser.image = laser.org_image
                laser.scaleSprite((1, self.frame.count))
                # TODO adjust position
                laser.rect.x = pos[i][0]
                laser.rect.y = pos[i][1]
                i += 1
            else:
                self.frame.count = self.frame.max_count
                # TODO rotate
        self.frame.add()
        # TODO condition when to end

    def bulletWaves(self):
        '''
           Circles of bullets. In this case self.frame is used to determine when to send out next row.
           blt.radius must be dividable by bullet radius speed in path.explode function
        '''
        groups = self.bulletLists[1:]
        emptyGroups = 0
        self.frame.max_count = len(groups)
        for group in groups:
            if groups.index(group) <= self.frame.count:
                radiusChecked = False
                for blt in group:
                    paths.explode(blt, self.boss.rect.x + 48, self.boss.rect.y + 27, 4)
                    paths.orbit(blt, self.boss.rect.x + 48, self.boss.rect.y + 27, 1)
                    if blt.radius == 200 and radiusChecked == False:
                        self.frame.add()
                        radiusChecked = True
                    blt.checkBounds(True, True, True, True)
            if self.isGroupEmpty(group):
                emptyGroups += 1
        if emptyGroups == len(groups):
            self.act += 1

levelList = [Level_1(), Level_2(), Level_3()]

# == Some functions for level preparation and updating ==
def prepareCircle(count, center_pos, variant, groups):
    '''
        Prepares a set of bullets, distributed in a circle.
        count       Number of bullets in a circle
        center_pos  Center of circle
        variant     Small ball sprite variant
        groups      A list of groups, to which bullet should be added
    '''
    angles = position.distributeAngle(count)
    for i in range(count):
        ball = bullet.makeSmallBall(center_pos[0], center_pos[1], angles[i], variant)
        addToGroups(ball, groups)

def addToGroups(obj, groups):
    '''
        Adds object to specified groups.
    '''
    for group in groups:
        group.add(obj)

def bulletMovement(enemy, bullet, speed_r, speed_a):
    paths.explode(bullet, enemy.rect.x + 36, enemy.rect.y + 36, speed_r)
    paths.orbit(bullet, enemy.rect.x + 36, enemy.rect.y + 36, speed_a)
    bullet.checkBounds(True, True, True, True)
    if bullet.radius == 10:
        return True
    return False