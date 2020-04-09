import pygame
import config as C 
from pygame         import Vector2 as V
from screen_objects import Screen_Obj

# Parent class for all moveable objects, inherits from screen_obj

class Moveable_Obj(Screen_Obj):

    """ Child class, inherits from screen_obj but adds speed and direction arguments to objects. Takes in same 
        arguments as screen_obj. 
    """

    def __init__(self, pics, x, y, pos):
        super().__init__(pics, x, y, pos)

        self.speed  = V(0, 0)
        self.dir    = 0
    



    






    

