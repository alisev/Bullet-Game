import pygame as pg

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
    
    def call(self):
        '''
            Calls current level's game logic, updates level_num when level is completed and returns True or False value to indicate if the game has been beaten.
        '''
        if self.level_num < len(self.levels):
            self.level_num = self.level.update(self.level_num)
            return False
        return True

    def draw(self):
        '''
            Draws current level.
        '''
        screen = pg.display.get_surface()
        self.level.allSprites.draw(screen)

class LevelBlueprint():
    '''
        A blueprint class for level creation.
        bullet_rows     Amount of rows with bullets
        bullets_perRow  Amount of bullets per row
        bullet_count    Total amount of bullets
        allSprites      All sprites in current level
        bulletLists     Array of bullet sprite groups
        enemyLists      Array of enemy sprite groups
    '''
    def __init__(self, a, b):
        self.bullet_rows = a
        self.bullets_perRow = b
        self.bullet_count = self.bullet_rows * self.bullets_perRow

        self.allSprites = pg.sprite.Group()
        self.bulletLists = []
        self.enemyLists = []

        self.isPrepared = False

    def createSpriteList(self, n):
        '''
            Creates sprite group arrays. Used for bulletLists and enemyLists
        '''
        array = []
        for i in range(n):
            array.append(pg.sprite.Group())
        return array

    def populateBulletLists(self):
        self.bulletLists = createSpriteList(bullet_rows)

    def populateEnemyList(self, a):
        self.enemyList = createSpriteList(a)

    def clearSpriteLists(self):
        '''
            Clears all sprite lists.
        '''
        self.allSprites.empty()
        self.bulletLists.clear()
        self.enemyLists.clear()

class Level_1(LevelBlueprint):
    def __init__(self):
        super().__init__(3, 5)
        
    def prepare(self):
        pass

    def update(self, lvl):
        return lvl

levelList = [Level_1()]