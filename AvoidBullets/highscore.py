import pygame as pg
import util

'''
    Functions related to highscore display, calculation and saving.
'''

file = "high.score"

class Highscore():
    '''
        Handles highscores after the game is finished.
        player_score    Player's current score
        player_name     Player's name
        top_score       Highscore list
    '''
    def __init__(self, player_score, file):
        self.player_score = player_score
        self.player_name = ''
        self.file = file
        self.top_score = self.load()

    def load(self):
        '''
            Opens the specified file and loads its contents in a list.
        '''
        highscore_list = []
        f = open(self.file)
        for line in f:
            if line[0] == '#':
                pass
            else:
                line = line.rstrip()
                score_name = line.split(" ", 1)
                score_name[0] = self.attrib_int(score_name[0])
                highscore_list.append(score_name)
        f.close()
        return highscore_list

    def displayBest(self, screen):
        '''
            Displays 10 best scores on screen.
        '''
        counter = 0
        text_y = 300
        font_size = 24
        lineheight = 26
        xpos = [250, 450]
        for score in self.top_score:
            if counter == 10:
                break
            util.renderText(screen, str(score[0]), [xpos[0], text_y], font_size)
            util.renderText(screen, str(score[1]), [xpos[1], text_y], font_size)
            text_y += lineheight
            counter += 1
        if counter < 10:
            empty_lines = 10 - counter
            for i in range(empty_lines):
                util.renderText(screen, '-', [xpos[0], text_y], font_size)
                util.renderText(screen, '-', [xpos[1], text_y], font_size)
                text_y += lineheight

    def save(self):
        '''
            Saves player's score and name.
        '''
        f = open(self.file, "a")
        record = '\n' + str(self.player_score) + ' ' + self.player_name
        f.write(record)
        f.close()

    def attrib_int(self, record):
        return int(record)

    def compare(self):
        '''
            Does a comparision between 10 best scores and player's. If player has a higher score than any of the listed ones, then it is added to the list.
            If player has no points, there is no point to compare it with the highscore list.
        '''
        if self.player_score > 0:
            for score in self.top_score:
                if score[0] < self.player_score:
                    self.player_name = self.nameInput()
                    self.save()
                    break
        self.top_score.append([self.player_score, self.player_name])
        self.top_score.sort(reverse = True)

    def nameInput(self): #todo finish
        '''
            Allows player to input their name.
        '''
        name = "TODO"
        return name


def displayScore(screen, score):
    '''
        Formats player's score and displays it on screen.
        screen      Gameplay surface
        score       Player's score
    '''
    digit_count = 8
    score_digits = len(str(score))
    zero_count = digit_count - score_digits
    player_score = "0" * zero_count + str(score) if (zero_count > 0) else str(score)
    util.renderText(screen, player_score, [650, 25], 36)

def increaseScore(score, points):
    '''
        Rewards player with points.
    '''
    score += points
    return score
