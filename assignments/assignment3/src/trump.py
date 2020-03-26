import pygame
import parameter as P 
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Trump(Player):

    #trump_pos = (300, 600)

    def __init__(self):
        trump_ctrl = [pygame.K_w, pygame.K_a, pygame.K_d]
        super().__init__("pics/milenium_falcon.png", 70, 80, V(200, 800), trump_ctrl)

                
    
