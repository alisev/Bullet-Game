import pygame as pg
from constants import *
import highscore
from levels import Level, levelList
import player
import util

class Game(object):
    '''
        Manages active game state and handles main loop events.
        https://gist.github.com/iminurnamez/8d51f5b40032f106a847
        Properties:
            done        Indicates if player is quitting the game
            screen      Pygame display surface
            clock       Pygame clock
            fps         FPS limit
            states      Dictionary mapping state names to Gamestate objects
            state_name  Current state's name
            state       Current state object
    '''
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = FPS
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        '''
            Event handling. 
        '''
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        '''
            Switches to next game state.
        '''
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        '''
            Check for state flip and update active state.
            dt  milliseconds since last frame
        '''
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()    
        self.state.update(dt)

    def draw(self):
        '''
            Pass display surface to the active state for drawing.
        '''
        self.state.draw(self.screen)

    def run(self):
        '''
            Handles main loop events.
        '''
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()

class GameState(object):
    '''
        Game state superclass.
        done        Indicates if game needs to switch to next state.
        quit        Indicates if player is quitting the game.
        next_state  Name of the next state
        screen_rect Gets reference to current display surface
        persist     
        font        Font used by the state
    '''
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        
    def startup(self, persistent):
        '''
            Called when a state resumes being active. Allows information to be passed between states.
            persistent  A dict passed from state to state
        '''
        self.persist = persistent        
        
    def get_event(self, event):
        '''
            Handles a single event passed by the Game object.
        '''
        pass
        
    
    def update(self, dt):
        '''
            Update the state. Called by the Game object once per frame. 
            dt  time since last frame
        '''
        pass
        
    def draw(self, surface):
        '''
            Draw everything to the screen.
        '''
        pass

class SplashScreen(GameState):
    '''
        Game's splash screen state.
        persist
        next_state  Name of the next game state
        title_logo  Title logo's graphic
    '''
    def __init__(self): # TODO add necessary variables
        super(SplashScreen, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "GAMEPLAY"
        self.title_logo = util.loadSprite("title.png")
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True
    
    def draw(self, surface):
        surface.fill(BGCOLOR)
        surface.blit(self.title_logo,(121,100))
        util.renderText(surface, 'Press Enter key to start the game', [150, 350], 22)

class Gameplay(GameState):
    '''
        Game's state designed for gameplay.
        player      Player object
        allSprites  Group object, contains all sprites

        score       Player's current score
        levels      Level logic
    '''
    def __init__(self):
        super(Gameplay, self).__init__()
        self.levels = Level(levelList)
        self.next_state = "GAMEOVER"
        
    def startup(self, persistent):
        self.player = player.player
        self.allSprites = pg.sprite.Group()
        self.allSprites.add(self.player)

        self.score = 0
        self.levels.resetGame()
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.player.moveX(-1)
            elif event.key == pg.K_RIGHT:
                self.player.moveX(1)
            elif event.key == pg.K_UP:
                self.player.moveY(-1)
            elif event.key == pg.K_DOWN:
                self.player.moveY(1)
            elif event.key == pg.K_z:
                blt = self.player.shoot()
                self.allSprites.add(blt)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                self.player.moveX(0)
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                self.player.moveY(0)
        
    def update(self, dt):
        '''
            Updates entity position on screen and checks for collissions between them. 
        '''
        self.player.update()
        data = self.levels.call()
        isGameFinished = data["done"]
        self.levels.entityCollission(self.player)
        self.score += self.levels.groupCollission(self.player.children) + data["points"]
        if self.player.lives == 0 or isGameFinished:
            self.persist["score"] = self.score
            self.persist["lives"] = self.player.lives
            self.done = True

    def draw(self, surface):
        surface.fill(BGCOLOR)
        self.levels.draw()
        self.allSprites.draw(surface)
        self.lifeCounter(surface)
        highscore.displayScore(surface, self.score)

    def lifeCounter(self, surface):
        '''
            Displays how many lives player has left.
        '''
        lives_max = PLAYER_MAX_LIVES
        lives = self.player.lives
        sprites = ["life.png", "life_empty.png"]
        x_pos = 25
        y_pos = 25
        for i in range(lives_max):
            img = sprites[0] if i < lives else sprites[1]
            loadedImage = util.loadSprite(img)
            surface.blit(loadedImage, (x_pos, y_pos))
            x_pos += 37

class GameOver(GameState):
    '''
        Game state when player wins or loses the game.
    '''
    def __init__(self):
        super(GameOver, self).__init__()
        self.next_state = "SPLASH"
        
    def startup(self, persistent):
        self.persist = persistent 
        self.player_score = self.persist["score"]
        self.message = ""
        if self.persist["lives"] > 0:
            self.message = "Congratulations! You've won!"
        else:
            self.message = "Game Over"
        self.highscores = highscore.Highscore(self.player_score, highscore.file)
        self.highscores.compare()
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True
        
    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(BGCOLOR)
        util.renderText(surface, self.message, [100, 100], 36)
        util.renderText(surface, "You earned " + str(self.player_score) + " points.", [100, 144], 36)
        self.highscores.displayBest(surface)