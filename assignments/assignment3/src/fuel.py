import config as C
import pygame
from screen_objects import Screen_Obj

class Fuel(Screen_Obj):

    """ Object that passes arguments upwards in the inheritance tree. Passes on arguments for 
        pics, x and y. Takes pos as inpurt arguments.
    """

    def __init__(self, pos):
        super().__init__("pics/fuel.png", 50, 50, pos)
