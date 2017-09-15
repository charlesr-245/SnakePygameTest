import pygame
import sys
from pygame.locals import *

class EventHandler():
    """Handles input from user"""
    def Update():
        for event in pygame.event.get():
            if event.type == QUIT:
                print("QUITTING PROGRAM...")
                sys.exit(0)