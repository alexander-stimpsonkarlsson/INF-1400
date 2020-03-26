import pygame
import math as M
import config as P 
from pygame import Vector2 as V
from blaster import Blasters
from pygame.locals import *

class Green_Blast(Blasters):

    def __init__(self):
        super().__init__("pics/star_destroyer.png", P.G_W, P.G_H)