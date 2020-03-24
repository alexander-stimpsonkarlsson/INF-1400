import pygame
import parameter as P 
from player import Player
from pygame.locals import *

class Kim(Player):

    #kim_pos = (500, 500)

    def __init__(self):
        kim_ctrl = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
        super().__init__("pics/kimgethit.png", 60, 60, (500, 500), kim_ctrl)

