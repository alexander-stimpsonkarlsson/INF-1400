import pygame
import parameter as P 
from pygame import Vector2 as V
from player import Player
from pygame.locals import *

class Kim(Player):

    #kim_pos = (500, 500)

    def __init__(self):
        kim_ctrl = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
        super().__init__("pics/star_destroyer.png", 60, 80, V(1400, 800), kim_ctrl)

