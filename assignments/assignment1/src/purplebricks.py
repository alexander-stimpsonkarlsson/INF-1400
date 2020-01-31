import pygame
from pygame.math import Vector2 as vec 

(width, height) = (1645, 1200)
screen = pygame.display.set_mode((width, height))
screen_res = (1645, 1200)

class purple_brick: #classe for purple objects
    def __init__(self,screen,x,y):
        self.color=(106,13,173)
        self.x = x
        self.y = y
        self.w = 200
        self.h = 75
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

bricks = []                           #adds bricks to list 
brick1 = purple_brick(screen,5,5) 
bricks.append(brick1)           
brick2 = purple_brick(screen,210,5)   
bricks.append(brick2)
brick3 = purple_brick(screen,415,5)   
bricks.append(brick3)
brick4 = purple_brick(screen,620,5)  
bricks.append(brick4)
brick5 = purple_brick(screen,825,5) 
bricks.append(brick5)  
brick6 = purple_brick(screen,1030,5)  
bricks.append(brick6) 
brick7 = purple_brick(screen,1235,5)   
bricks.append(brick7)
brick8 = purple_brick(screen,1440,5)  
bricks.append(brick8)