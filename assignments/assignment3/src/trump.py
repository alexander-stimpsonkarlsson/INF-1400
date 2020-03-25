import pygame
import parameter as P 
from player import Player
from pygame.locals import *

class Trump(Player):

    #trump_pos = (300, 600)

    def __init__(self):
        trump_ctrl = [pygame.K_w, pygame.K_a, pygame.K_d]
        super().__init__("pics/smoosh.png", 80, 80, (200, 800), trump_ctrl)

                
    
