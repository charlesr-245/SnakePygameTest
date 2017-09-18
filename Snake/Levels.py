import pygame
from pygame.locals import *
import colors
from LevelObjects import *
from EventHandler import *
import random

class Levels(object):
    """All levels in the game"""
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.DISPLAYWIDTH = this.screen.get_width()
        this.DISPLAYHEIGHT = this.screen.get_height()
        this.eventHandler = _eventHandler
        pygame.font.init()
        this.TITLEFONT = pygame.font.Font(None,80)
        this.BUTTONFONT = pygame.font.Font(None,65)
        this.ID = random.random()

    def MainMenu(this,manager):
        #print(this.ID)
        #Header
        rect = pygame.draw.rect(this.screen, colors.WHITE, (0,0,this.DISPLAYWIDTH,this.DISPLAYHEIGHT*0.1),0)
        title = this.TITLEFONT.render("Snake", 1, colors.BLACK,None)
        titleInfo = title.get_rect()
        this.screen.blit(title, (this.DISPLAYWIDTH/2 - titleInfo.center[0],this.DISPLAYHEIGHT*0.01))
        #Buttons
        playButton = Button(colors.RED, ((this.DISPLAYWIDTH/2)-100,(this.DISPLAYHEIGHT/2),200,(60)),0, "Play", colors.BLACK, this.BUTTONFONT, this.screen, this.eventHandler,"l 1") #if the button is press the command "l 1" will be called with l standing for level and 1 being the level number
        if (playButton.Boundaries(playButton.size)):
            manager.currentLevel = 1

class Level1(object):
    def __init__(this, screen, eventManager, enabled, manager):
        this.ID = random.random()
        this.screen = screen
        this.eventHandler = eventManager
        this.manager = manager
        this.snake = Snake(colors.GREEN, 15, 5, this.screen, this.manager)
        #print(this.snake.snakeHead.pos)
    def Update(this):
        #print(this.ID)
        dirX = this.eventHandler.getXDirection()
        dirY = this.eventHandler.getYDirection()
        this.snake.Update(dirX, dirY)


