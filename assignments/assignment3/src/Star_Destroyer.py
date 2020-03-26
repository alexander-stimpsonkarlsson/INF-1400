import pygame
import config as P 
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Star_Destroyer(Player):

    def __init__(self):
        super().__init__("pics/star_destroyer.png", P.STAR_W, P.STAR_H, V(P.STAR_POS), P.STAR_CTRL)

