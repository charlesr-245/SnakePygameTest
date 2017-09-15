import pygame
from pygame.locals import *
import color
from LevelObjects import *

class Levels(object):
    """All levels in the game"""
    def __init__(this, _screen):
        this.screen = _screen
        this.DISPLAYWIDTH = this.screen.get_width()
        this.DISPLAYHEIGHT = this.screen.get_height()

        pygame.font.init()
        this.TITLEFONT = pygame.font.Font(None,80)
        this.BUTTONFONT = pygame.font.Font(None,20)

    def MainMenu(this):
        #Header
        rect = pygame.draw.rect(this.screen,color.WHITE, (0,0,this.DISPLAYWIDTH,this.DISPLAYHEIGHT*0.1),0)
        title = this.TITLEFONT.render("Snake", 1, color.BLACK,None)
        titleInfo = title.get_rect()
        this.screen.blit(title, (this.DISPLAYWIDTH/2 - titleInfo.center[0],this.DISPLAYHEIGHT*0.01))
        #Buttons
        playButton = LevelObjects.Button(this.screen, color.RED, ((this.DISPLAYWIDTH/2)-100,(this.DISPLAYHEIGHT/2),200,(60)),0, "Play", color.BLACK, None)

