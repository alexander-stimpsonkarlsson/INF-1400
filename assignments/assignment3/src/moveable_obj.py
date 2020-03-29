import pygame
import config as C 
from pygame import Vector2 as V
from screen_objects import Screen_Obj

# Parent class for all moveable objects, inherits from screen_obj

class Moveable_Obj(Screen_Obj):

    def __init__(self, pics, x, y, pos):
        super().__init__(pics, x, y, pos)

        self.speed  = V(0, 0)
        self.dir    = 0
    
    #def check_collision(self, obj1, obj2):



    






    

