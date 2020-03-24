import pygame
import math as M
import parameter as P 
from moveable_obj import Moveable_Obj
from pygame.locals import *

class Player(Moveable_Obj):

    def __init__(self, pics, x, y, pos, ctrl):
        super().__init__(pics, x, y, pos)

        self.up     = 0
        self.down   = 0
        self.right  = 0
        self.left   = 0
        self.ctrl   = ctrl

    def update(self):

        x = self.rect.centerx
        y = self.rect.centery

        self.speed = (self.up)

        if self.speed > P.PLAYER_SPEED:
            self.speed = P.PLAYER_SPEED
        
        if self.speed < -P.PLAYER_FALL:
            self.speed = -P.PLAYER_FALL
        
        self.dir += (self.left + self.right)
        angle = self.dir * M.pi / 180

        x += -self.speed*M.sin(angle)
        y += -self.speed*M.cos(angle)

        self.image = pygame.transform.rotate(self.image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        


    def control(self):

        key = pygame.key.get_pressed()

        if key[self.ctrl[0]]:
            self.up = 1 * 2
        if key[self.ctrl[1]]:
            self.right = 1 * -2
        if key[self.ctrl[2]]:        
            self.left = 1 * 2






