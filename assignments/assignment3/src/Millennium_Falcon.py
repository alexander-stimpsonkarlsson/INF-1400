import pygame
import config as P 
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Millennium_Falcon(Player):

    def __init__(self):
        super().__init__("pics/milenium_falcon.png", P.MILLENIUM_W, P.MILLENIUM_H, V(P.MILLENNIUM_POS), P.MILLENIUM_CTRL)

                
    
