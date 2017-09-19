import pygame
import sys
import colors
from pygame.locals import *

class EventHandler():
    """Handles input from user"""
    def __init__(this):
        this.mouseDown = False
        this.xDirection = 1
        this.yDirection = 0
    def Update(this):
       this.mouseDown = False
       for event in pygame.event.get():
            if event.type == QUIT:
                #print("QUITTING PROGRAM...")
                sys.exit(0)
            if pygame.mouse.get_pressed()[0]:
                this.mouseDown = True
            if pygame.key.get_pressed()[K_RIGHT]:
                if (this.xDirection == 0):
                    this.xDirection = 1
                    this.yDirection = 0
            elif pygame.key.get_pressed()[K_DOWN]:
                if (this.yDirection == 0):
                    this.yDirection = 1
                    this.xDirection = 0
            elif pygame.key.get_pressed()[K_UP]:
                if (this.yDirection == 0):
                    this.yDirection = -1
                    this.xDirection = 0
            elif pygame.key.get_pressed()[K_LEFT]:
                if (this.xDirection == 0):
                    this.xDirection = -1
                    this.yDirection = 0
    def getMouseDown(this):
        return this.mouseDown
    def getXDirection(this):
        #print(this.direction)
        return this.xDirection
    def getYDirection(this):
        #print(this.direction)
        return this.yDirection