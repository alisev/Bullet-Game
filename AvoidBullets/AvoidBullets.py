# Alise Linda Viļuma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score
# TODO i might need to return to older version if this doesn't work out

import sys
import pygame as pg
import constants
import levels
import player

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
        self.fps = constants.FPS
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
        self.font = pg.font.Font(None, 24)
        
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
        self.title_logo = pg.image.load("sprites\\title.png").convert_alpha()
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True
    
    def draw(self, surface):
        surface.fill(constants.BGCOLOR)
        surface.blit(self.title_logo,(121,100))
        # TODO splash screen graphic rendering goes here

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
        img = pg.image.load("sprites\\ship.png").convert_alpha()
        self.player = player.Player(img)
        self.allSprites = pg.sprite.Group()
        self.allSprites.add(self.player)

        self.score = 0

        self.levels = levels.Level(levels.levelList)
        
    def startup(self, persistent):
        pass
        
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
        self.player.update()
        self.levels.call()
        # TODO calls the necessary level here

    def draw(self, surface):
        surface.fill(constants.BGCOLOR)
        self.allSprites.draw(surface)
        self.levels.draw()
        # TODO calls drawing function of the particular level

class GameOver(GameState):
    '''
        Gameover screen.
    '''
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "SPLASH"
        # TODO variables
        
    def startup(self, persistent):
        # TODO highscore from game gets passed here
        pass
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                # TODO Return to menu
                pass
        
    def update(self, dt):
        # TODO game logic here
        # IMPORTANT events here get looped, so if I'm saving game results to a txt file, I must make sure that it happens only once
        pass

    def draw(self, surface):
        # Renders all highscores so far
        pass

class GameWin(GameState):
    '''
        Gamewin screen.
    '''
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "SPLASH"
        # TODO variables
        
    def startup(self, persistent):
        # TODO highscore from game gets passed here
        pass
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                # TODO Return to menu
                pass
        
    def update(self, dt):
        # TODO game logic here
        # IMPORTANT events here get looped, so if I'm saving game results to a txt file, I must make sure that it happens only once
        pass

    def draw(self, surface):
        # Renders all highscores so far
        pass

# Main event loop
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))
    pg.display.set_caption(constants.TITLE)
    states = {"SPLASH": SplashScreen(),
                    "GAMEPLAY": Gameplay()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()