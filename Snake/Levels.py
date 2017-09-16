import pygame
from pygame.locals import *
import colors
from LevelObjects import *
from EventHandler import *

class Levels(object):
    """All levels in the game"""
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.DISPLAYWIDTH = this.screen.get_width()
        this.DISPLAYHEIGHT = this.screen.get_height()
        this.eventHandler = _eventHandler
        this.levelObjects = LevelObjects(this.screen, this.eventHandler)
        pygame.font.init()
        this.TITLEFONT = pygame.font.Font(None,80)
        this.BUTTONFONT = pygame.font.Font(None,65)

    def MainMenu(this):
        #Header
        rect = pygame.draw.rect(this.screen, color.WHITE, (0,0,this.DISPLAYWIDTH,this.DISPLAYHEIGHT*0.1),0)
        title = this.TITLEFONT.render("Snake", 1, color.BLACK,None)
        titleInfo = title.get_rect()
        this.screen.blit(title, (this.DISPLAYWIDTH/2 - titleInfo.center[0],this.DISPLAYHEIGHT*0.01))
        #Buttons
        playButton = this.levelObjects.Button(color.RED, ((this.DISPLAYWIDTH/2)-100,(this.DISPLAYHEIGHT/2),200,(60)),0, "Play", color.BLACK, this.BUTTONFONT, None)
        playButtonDetector = this.levelObjects.Boundaries((this.DISPLAYWIDTH/2)-100,(this.DISPLAYHEIGHT/2),200,(60))


