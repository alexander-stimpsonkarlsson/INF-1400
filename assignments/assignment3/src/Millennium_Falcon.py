import pygame
import config as C
from pygame import Vector2 as V
from player import Player

# Millenium falcon class, inherits from player class

class Millennium_Falcon(Player):

    def __init__(self):
        super().__init__("pics/milenium_falcon.png",                # Picture 
        C.MILLENIUM_W, C.MILLENIUM_H, V(C.MILLENNIUM_POS),          # Size and position
        C.MILLENIUM_CTRL, "pics/red_blast.png", C.MILLENIUM_SOUND)  # Controls, blaster picture and sound of blaster

                
    
