import pygame
from pygame.locals import *
import colors

class LevelObjects(object):
    """description of class"""
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.DISPLAYWIDTH = this.screen.get_width()
        this.DISPLAYHEIGHT = this.screen.get_height()
        this.eventHandler = _eventHandler

    def Button(this, _color, size, fill, text, _colorText, font, background = None):
        button = pygame.draw.rect(this.screen, _color, size, fill)
        text = font.render(text, 1, _colorText, background)
        textInfo = text.get_rect()
        this.screen.blit(text, (this.DISPLAYWIDTH/2-textInfo.center[0], this.DISPLAYHEIGHT/2+textInfo.center[1]/2))
    def ButtonPlay(size):
        if (this.eventHandler.getMouseDown()):
            if (pygame.mouse.get_pos()[0]):
                return


