import config as C
import pygame
from screen_objects import Screen_Obj

class Fuel(Screen_Obj):

    def __init__(self, pos):
        super().__init__("pics/fuel.png", 50, 50, pos)
