import pygame
import math as M
import parameter as P 
from pygame import Vector2 as V
from screen_objects import Screen_Obj

# Parent class for all moveable objects

class Moveable_Obj(Screen_Obj):

    def __init__(self, pics, x, y, pos):
        super().__init__(pics, x, y, pos)

        self.speed  = V(0, 0)
        self.dir    = 0

    #def edge(self):

        #x = self.pos[0]
        #y = self.pos[1]

        #if self.rect.centerx < 0 + P.WALL_DIST:




    

