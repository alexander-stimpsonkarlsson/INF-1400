import pygame
import config as C
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Millennium_Falcon(Player):

    def __init__(self):
        super().__init__("pics/milenium_falcon.png", C.MILLENIUM_W, C.MILLENIUM_H, V(C.MILLENNIUM_POS), C.MILLENIUM_CTRL, "pics/red_blast.png")

                
    
