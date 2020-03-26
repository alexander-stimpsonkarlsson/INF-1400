import pygame
import math as M
import parameter as P 
from pygame import Vector2 as V
from moveable_obj import Moveable_Obj
from pygame.locals import *

class Player(Moveable_Obj):

    def __init__(self, pics, x, y, pos, ctrl):
        super().__init__(pics, x, y, pos)

        self.ctrl = ctrl
        self.acc = V(0, -0.2)
        self.dir_speed = 0

    def player_rotate(self):                            # rotates player 
    
        self.acc.rotate_ip(self.dir_speed)
        self.dir += self.dir_speed

        if self.dir > 360:
            self.dir -= 360
        elif self.dir < 0:
            self.dir += 360 
        self.image = pygame.transform.rotate(self.rotation_img, -self.dir)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, fps):
        
        self.edge()
        key = pygame.key.get_pressed()
    
        if key[self.ctrl[1]]:                           # left, rotates
            self.dir_speed = -3
            self.player_rotate() 
        if key[self.ctrl[2]]:                           # right, rotate
            self.dir_speed = 3
            self.player_rotate() 
        
        if key[self.ctrl[0]]:                           # thrust upwards
            self.speed += self.acc
        
        if self.speed.length() > P.MAX_THRUST:          # restricts max thrust
            self.speed.scale_to_length(P.MAX_THRUST)
        
        self.speed += P.GRAVITY
        self.pos += self.speed                          # updates position 
        self.rect.center = self.pos 
    
    def edge(self):

        if self.rect.centerx < 0:
            self.pos[0] = P.SCREEN_WIDTH
        if self.rect.centerx > P.SCREEN_WIDTH:
            self.pos[0] = 0
        if self.rect.centery < 0:
            self.pos[1] = P.SCREEN_HEIGHT
        if self.rect.centery > P.SCREEN_HEIGHT:
            self.pos[1] = 0

    #def reset(self):"""

    #def update(self, fps):

        #self.gravity()
    #    self.speed += self.up

    #    if self.speed > P.MAX_THRUST:
    #        self.speed = P.MAX_THRUST

    #    self.dir += (self.left + self.right)

    #    x, y = self.pos
    #    angle = self.dir * M.pi / 180
    #    x += -self.speed*M.sin(angle)
    #    y += -self.speed*M.cos(angle)
    #    self.pos = (x, y)

    #    self.image = pygame.transform.rotate(self.rotation_img, self.dir)
    #    self.rect = self.image.get_rect()
    #    self.rect.center = self.pos


    #def control(self):

    #    for event in pygame.event.get():
    #        if not hasattr(event, 'key'): 
    #            continue
    #        
    #        activate = event.type == KEYDOWN

    #        if event.key == self.ctrl[0]:
    #            self.up = activate * 2
    #        if event.key == self.ctrl[1]:
    #            self.left = activate * 5
    #        if event.key == self.ctrl[2]:
    #            self.right = activate * -5
        
    #    if(self.speed != 0):
    #        if self.speed > 0:
    #            self.speed -= 0.5
    #        elif self.speed < 0:
    #            self.speed += 0.5
                
   