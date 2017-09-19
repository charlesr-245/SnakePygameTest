import pygame
from pygame.locals import *
import colors
import random
from array import *
import os

#TODO reset snake direction upon death

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
            text2 = font.render(str(this.size[0]), 1, colors.RED)
            text3 = font.render(str(this.size[0]+this.size[2]), 1, colors.BLUE)
            text4 = font.render(str(this.size[1]), 1, colors.GREEN)
            text5 = font.render(str(this.size[3]+this.size[3]), 1, colors.ORANGE)
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
    def __init__(this, color, size, parts, screen, manager, collectable):
        this.manager = manager
        this.color = color
        this.size = size
        this.pos = (this.size,this.size,this.size,this.size)
        this.parts = parts
        this.screen = screen
        this.lastDirX = 1
        this.lastDirY = 0
        this.dirX = 1
        this.dirY = 0
        this.speed = 0.75
        this.posToAppend = this.pos
        this.snakeHead = SnakeHead(this)
        this.collectable = collectable
        this.posArray = [array('f'), array('f'), array('f'), array('f')] #Deprecated, used for pos display
        #this.snakeBody = [SnakeBody(this, i) for i in range(1, this.parts)]
        this.snakeBody = [SnakeBody(this,i) for i in range(1, this.parts)]
        #this.snakeBody[6].pos = (100,100,this.size,this.size)
        this.font = pygame.font.Font(None, 50)
    def Update(this, dirX, dirY):
        if (dirX != this.lastDirX or dirY != this.lastDirY):
            '''
            this.posArray[0].append(this.snakeHead.pos[0])
            this.posArray[1].append(this.snakeHead.pos[0])
            this.posArray[2].append(dirX)
            this.posArray[3].append(dirY)'''
            for i in range(1, this.parts-1):
                this.snakeBody[i].AddPos((this.snakeHead.pos[0],this.snakeHead.pos[1],dirX, dirY))

        this.lastDirX = dirX
        this.lastDirY = dirY
        this.dirX = dirX
        this.dirY = dirY
        '''
        if (len(this.posArray[0]) != 0):
            pos = str(this.posArray[0][0]) + " , " + str(this.posArray[1][0]) + " , " + str(this.posArray[2][0]) + " , " + str(this.posArray[3][0]) 
            text = this.font.render(pos,1, colors.ORANGE)
            this.screen.blit(text, (200,100,0,0))'''
        this.snakeHead.Update(dirX,dirY)
        for i in range (1, this.parts-1):
            this.snakeBody[i].Update(this)
        this.CheckCollectable()

    def AddPart(this):
        this.parts+=1
        this.snakeBody.append(SnakeBody(this,this.parts))
        this.collectable.ResetPos(this.collectable)

    def CheckCollectable(this):
        if (this.snakeHead.pos[0]>= this.collectable.pos[0] - this.collectable.size and this.snakeHead.pos[0]<= this.collectable.pos[0] + this.collectable.size):
            if (this.snakeHead.pos[1]>= this.collectable.pos[1] - this.collectable.size and this.snakeHead.pos[1]<= this.collectable.pos[1] + this.collectable.size):
                this.AddPart()

    def ResetPositions(this):
        this.pos = (this.size,this.size,this.size)
        this.snakeHead.pos = this.pos
        this.dirX = 1
        this.dirY = 0
        this.posArray.clear()
        this.snakeHead.dirX = 1
        this.snakeHead.dirY = 0
        #print(this.snakeHead.dirX)
        this.lastDirX = 1
        this.lastDirY = 0
        for i in range (1, this.parts-1):
            this.snakeBody[i].pos = (this.pos[0]-(i*(this.size+5)),this.pos[1],this.size,this.size)
            this.snakeBody[i].dirX = 1
            this.snakeBody[i].dirY = 0
            this.snakeBody[i].posArray = [array('f'), array('f'), array('f'), array('f')]
            #print(this.posArray)
        #print(this.dirX)
        #print(this.dirY)

class SnakeHead(object):
    def __init__(this, snake):
        this.pos = snake.pos
        this.size = snake.size
        this.screen = snake.screen
        this.dirX = snake.dirX
        this.dirY = snake.dirY
        this.speed = snake.speed
    def Update(this,dirX, dirY):
        this.dirX = dirX
        this.dirY = dirY
        this.pos = (this.pos[0]+(this.speed*dirX), this.pos[1]+(this.speed*dirY), this.size,this.size)
        pygame.draw.rect(this.screen,colors.GREEN,this.pos)


class SnakeBody(object):
    def __init__(this, snake, i):
        this.part = i
        this.size = snake.size
        this.screen = snake.screen
        this.dirX = snake.dirX
        this.dirY = snake.dirY
        this.speed = snake.speed
        if (snake.snakeHead.dirX != 0):
            if (this.part > 4):
                this.pos = (snake.snakeHead.pos[0]-((i-2)*(this.size+5)*snake.snakeHead.dirX),snake.snakeHead.pos[1],this.size,this.size)
            else:
                this.pos = (snake.snakeHead.pos[0]-((i-1)*(this.size+5)*snake.snakeHead.dirX),snake.snakeHead.pos[1],this.size,this.size)
        else:
            if (this.part > 4):
                this.pos = (snake.snakeHead.pos[0],snake.snakeHead.pos[1]-((i-2)*(this.size+5)*snake.snakeHead.dirY),this.size,this.size)
            else:
                this.pos = (snake.snakeHead.pos[0],snake.snakeHead.pos[1]-((i-1)*(this.size+5)*snake.snakeHead.dirY),this.size,this.size)
        this.font = pygame.font.Font(None,50)
        this.posArray = [array('f'), array('f'), array('f'), array('f')]
        this.manager = snake.manager
        #print(this.part)
    def Update(this, snake):
        #snake.snakeBody.append(SnakeBody(this,8))
        if (len(this.posArray[0]) != 0):
            if ((this.pos[0] > this.posArray[0][0] - 0.375) and (this.pos[0] < this.posArray[0][0]+0.375)): #Within coordinates' x location
                if ((this.pos[1] > this.posArray[1][0] - 0.375) and (this.pos[1] < this.posArray[1][0]+0.375)): #Within coordinates' y location
                    #Set the position to the coords for accuracy
                    this.pos = (this.posArray[0][0], this.posArray[1][0],this.size,this.size)
                    #Set the direction to that of when the head changed directions
                    this.dirX = this.posArray[2][0]
                    this.dirY = this.posArray[3][0]
                    #Erase the point and it's information from the array
                    this.posArray[0].pop(0)
                    this.posArray[1].pop(0)
                    this.posArray[2].pop(0)
                    this.posArray[3].pop(0)
            '''if (this.part == 2):
                pos = str(this.pos[0]) + " , " + str(this.pos[1]) + " , " + str(this.dirX) + " , " + str(this.dirY) 
                text = this.font.render(pos,1, colors.ORANGE)
                this.screen.blit(text, (100,400,0,0))'''
        this.pos = (this.pos[0]+(this.speed*this.dirX),this.pos[1]+(this.speed*this.dirY),this.size,this.size)
        pygame.draw.rect(this.screen, colors.RED, this.pos)
        this.BoundaryCheck(snake)

    def AddPos(this, pos):
        this.posArray[0].append(pos[0])
        this.posArray[1].append(pos[1])
        this.posArray[2].append(pos[2])
        this.posArray[3].append(pos[3])

    def BoundaryCheck(this, snake):
        if (this.part == 2):
                pos = str(round(this.pos[0],3)) + " , " + str(round(this.pos[1],3))
                pos2 = str(round(snake.snakeHead.pos[0],3)) + " , " + str(round(snake.snakeHead.pos[1],3)) 
                text = this.font.render(pos,1, colors.ORANGE)
                text2 = this.font.render(pos2, 1 , colors.BLUE)
                #this.screen.blit(text, (100,400,0,0))
                #this.screen.blit(text2, (100,500,0,0))
        if (this.pos[0] >= snake.snakeHead.pos[0] - 0.5 * this.size  and this.pos[0] <= snake.snakeHead.pos[0] + 0.5 * this.size):
            if (this.pos[1] >= snake.snakeHead.pos[1] - 0.5*this.size and this.pos[1] <= snake.snakeHead.pos[1] + 0.5*this.size):
                #print("Player hit snake")
                SendCommand(this.manager,"l 0", snake)

def SendCommand(manager, command, snake):
    if (list(command)[0] == 'l'):
        snake.ResetPositions()
        manager.eventHandler.xDirection = 1
        manager.eventHandler.yDirection = 0
        manager.previousLevel = 1
        manager.currentLevel = int(list(command)[2])
        #print(manager.currentLevel)

class Collectable(object):
    def __init__(this, screen):
        this.size = 10
        this.screen = screen
        this.pos = (random.randint(0,780), random.randint(0,580),this.size,this.size)
        #this.pos = (40,40,this.size,this.size)
    def Update(this):
        pygame.draw.rect(this.screen,colors.YELLOW,this.pos)
    def ResetPos(snake, collectable):
        collectable.pos = (random.randint(0,780), random.randint(0,580),collectable.size,collectable.size)