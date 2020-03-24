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

        self.image = pygame.transform.rotate(self.image, self.dir)
        self.rect = self.image.get_rect()

    def update(self):

        self.control()

    def control(self):

        key = pygame.key.get_pressed()

        if key[self.ctrl[0]]:           # up
            self.speed = V(2, 2)
        if key[self.ctrl[1]]:           # left
            self.rotate(2) 
        if key[self.ctrl[2]]:           # right
            self.rotate(-2) 






