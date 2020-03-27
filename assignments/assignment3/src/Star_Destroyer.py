import pygame
import config as C 
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Star_Destroyer(Player):

    def __init__(self):
        super().__init__("pics/star_destroyer.png", C.STAR_W, C.STAR_H, V(C.STAR_POS), C.STAR_CTRL, "pics/green_blast.png")

