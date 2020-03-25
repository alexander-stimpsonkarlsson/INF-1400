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

    def player_rotate(self, n):

        self.dir += n  

        prev_center = self.rect.center
        self.image = pygame.transform.rotate(self.rotation_img, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = prev_center

    def update(self):

        self.gravity()
        self.control()

    def control(self):

        key = pygame.key.get_pressed()

        if key[self.ctrl[0]]: 
            self.player_thrust((0, -8))
        if key[self.ctrl[1]]:           # left
            self.player_rotate(2) 
        if key[self.ctrl[2]]:           # right
            self.player_rotate(-2) 

    def player_thrust(self, power):
        
        self.speed = power
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

    def gravity(self):

        if self.speed[1] < 0:
            self.rect.centery -= P.GRAVITY 
            self.rect.centery *= P.PLAYER_ACC          
        

    #def reset(self):