import pygame
from pygame.locals import *
import colors
import random
from array import *

class Button(object):
    def __init__(this, _color, _size, fill, text, _colorText, font, _screen, _eventHandler, command, debug = False, background = None):
        this.screen = _screen
        this.DISPLAYWIDTH = this.screen.get_width()
        this.DISPLAYHEIGHT = this.screen.get_height()
        this.eventHandler = _eventHandler
        this.size = _size
        button = pygame.draw.rect(this.screen, _color, this.size, fill)
        text = font.render(text, 1, _colorText, background)
        textInfo = text.get_rect()
        if(debug == True):
            text2 = font.render(str(size[0]), 1, colors.RED)
            text3 = font.render(str(size[0]+size[2]), 1, colors.BLUE)
            text4 = font.render(str(size[1]), 1, colors.GREEN)
            text5 = font.render(str(size[3]+size[3]), 1, colors.ORANGE)
            mousePosX = font.render(str(pygame.mouse.get_pos()[0]),1,colors.RED)
            mousePosY = font.render(str(pygame.mouse.get_pos()[1]),1,colors.BLUE)
            this.screen.blit(text, (this.DISPLAYWIDTH/2-textInfo.center[0], this.DISPLAYHEIGHT/2+textInfo.center[1]/2))
            this.screen.blit(text2, (0,50,0,0))
            this.screen.blit(text3, (0,100,0,0))
            this.screen.blit(text4, (0,150,0,0))
            this.screen.blit(text5, (0,200,0,0))
            this.screen.blit(mousePosX, (300,150,0,0))
            this.screen.blit(mousePosY, (450,150,0,0))
        this.screen.blit(text, (this.DISPLAYWIDTH/2-textInfo.center[0], this.DISPLAYHEIGHT/2+textInfo.center[1]/2))
        this.loadLevel = -1;

    def Boundaries(this, size):
        if (this.eventHandler.getMouseDown()):
            if (pygame.mouse.get_pos()[0] >= size[0] and pygame.mouse.get_pos()[0] <= size[0]+size[2] and pygame.mouse.get_pos()[1] >= size[1] and pygame.mouse.get_pos()[1] <= size[1]+size[3]):
                return True
        return False
    
    def ButtonPress(this):
        if (list(command)[0] == 'l'):
            this.loadLevel = list(command[2])
            return true
        return False

class Snake(object):
    def __init__(this, color, size, parts, screen):
        this.color = color
        this.size = size
        this.pos = (this.size,this.size,this.size,this.size)
        this.parts = parts
        this.screen = screen
        this.lastDirX = 1
        this.lastDirY = 0
        this.dirX = 1
        this.dirY = 0
        this.speed = 0.1
        this.posArray = [array('f'), array('f'), array('i'), array('i')]
        this.posArray[0].append(0)
        this.posArray[1].append(0)
        this.posArray[2].append(1)
        this.posArray[3].append(0)
        this.snakeHead = SnakeHead(this)
        this.snakeBody = [SnakeBody(this.snakeHead, i) for i in range(this.parts)]
    def Update(this, dirX, dirY):
        this.posArray[0].append(this.snakeHead.pos[0])
        this.posArray[1].append(this.snakeHead.pos[1])
        this.posArray[2].append(dirX)
        this.posArray[3].append(dirY)

        this.lastDirX = dirX
        this.lastDirY = dirY
        this.dirX = dirX
        this.dirY = dirY


        this.snakeHead.Update(dirX,dirY)
        for i in range (this.parts):
            this.snakeBody[i].Update(this)

class SnakeHead(object):
    def __init__(this, snake):
        this.color = snake.color
        this.size = snake.size
        this.pos = snake.pos
        this.speed = snake.speed
        this.screen = snake.screen
    
    def Update(this, dirX, dirY):
        if (dirX != 0):
            this.pos = (this.pos[0]+dirX*this.speed,this.pos[1],this.size,this.size)
        elif (dirY != 0):
            this.pos = (this.pos[0],this.pos[1]+dirY*this.speed,this.size,this.size)
        pygame.draw.rect(this.screen,this.color,this.pos)

class SnakeBody(object):
    def __init__(this, snake, i):
        this.color = snake.color
        this.size = snake.size
        this.part = i
        this.screen = snake.screen
        this.pos = (snake.pos[0]-this.part*(this.size+10),snake.pos[1],this.size,this.size)
        this.dirX = 0
        this.dirY = 0
        this.font = pygame.font.Font(None, 20)

    def Update(this, snake):
        if ((this.pos[0] > snake.posArray[0][0]-1 and this.pos[0] < snake.posArray[0][0] + 1) and (this.pos[1] > snake.posArray[1][0] -1 and this.pos[1] < snake.posArray[1][0]-1)):
            snake.posArray[0].pop([0])
            snake.posArray[1].pop([0])
            snake.posArray[2].pop([0])
            snake.posArray[3].pop([0])
        this.pos = (this.pos[0]+(snake.speed*snake.posArray[2][0]),this.pos[1]+(snake.speed*snake.posArray[3][0]),this.size,this.size)
        pygame.draw.rect(this.screen, this.color, this.pos)