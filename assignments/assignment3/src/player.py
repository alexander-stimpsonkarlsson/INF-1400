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

    def rotate(self, n):

        self.dir += n  
        self.image = pygame.transform.rotate(self.rotation_img, self.dir)
        
        #self.rect.center = self.pos

    def update(self):

        self.control()
        thrust = self.control()

        self.speed = thrust
        self.pos += self.speed

    def control(self):

        key = pygame.key.get_pressed()
        vector = V(0, 0)

        if key[self.ctrl[0]]:           # up
            vector += V(2, 2)
        if key[self.ctrl[1]]:           # left
            self.rotate(3) 
        if key[self.ctrl[2]]:           # right
            self.rotate(-3) 

        return vector





