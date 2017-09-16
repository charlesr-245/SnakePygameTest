import pygame
import sys
import colors
from pygame.locals import *

class EventHandler():
    """Handles input from user"""
    def __init__(this):
        this.mouseDown = False
    def Update(this):
       this.mouseDown = False
       for event in pygame.event.get():
            if event.type == QUIT:
                print("QUITTING PROGRAM...")
                sys.exit(0)
            elif pygame.mouse.get_pressed()[0]:
                this.mouseDown = True
    def getMouseDown():
        return this.mouseDown