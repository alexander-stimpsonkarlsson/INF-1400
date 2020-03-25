import pygame
import math as M
import parameter as P 
from pygame import Vector2 as V
from moveable_obj import Moveable_Obj
from pygame.locals import *

class Player(Moveable_Obj):

    def __init__(self, pics, x, y, pos, ctrl):
        super().__init__(pics, x, y, pos)

        self.ctrl   = ctrl
        self.left   = 0
        self.right  = 0
        self.up     = 0

    #def player_rotate(self, n):
    #
    #    self.dir += n  

    #    prev_center = self.rect.center
    #    self.image = pygame.transform.rotate(self.rotation_img, self.dir)
    #    self.rect = self.image.get_rect()
    #    self.rect.center = prev_center

    def update(self, fps):

        #self.gravity()
        self.speed += self.up

        if self.speed > P.MAX_THRUST:
            self.speed = P.MAX_THRUST

        self.dir += (self.left + self.right)

        x, y = self.pos
        angle = self.dir * M.pi / 180
        x += -self.speed*M.sin(angle)
        y += -self.speed*M.cos(angle)
        self.pos = (x, y)

        self.image = pygame.transform.rotate(self.rotation_img, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def control(self):

        for event in pygame.event.get():
            if not hasattr(event, 'key'): 
                continue
            
            activate = event.type == KEYDOWN

            if event.key == self.ctrl[0]:
                self.up = activate * 2
            if event.key == self.ctrl[1]:
                self.left = activate * 5
            if event.key == self.ctrl[2]:
                self.right = activate * -5
        
        if(self.speed != 0):
            if self.speed > 0:
                self.speed -= 0.5
            elif self.speed < 0:
                self.speed += 0.5
                
    #def control(self):
    #
    #    key = pygame.key.get_pressed()
    #
    #    if key[self.ctrl[0]]: 
    #        self.player_thrust((0, -8))
    #    if key[self.ctrl[1]]:           # left
    #        self.player_rotate(2) 
    #    if key[self.ctrl[2]]:           # right
    #        self.player_rotate(-2) 

    #def player_thrust(self, power):
        
    #    self.speed = power
    #    self.rect.centerx += self.speed[0]
    #    self.rect.centery += self.speed[1]

    #def gravity(self):

    #    if self.speed[1] < 0:
    #        self.rect.centery -= P.GRAVITY 
    #        self.rect.centery *= P.PLAYER_ACC          
        

    #def reset(self):"""