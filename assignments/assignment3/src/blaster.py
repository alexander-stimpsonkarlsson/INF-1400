import pygame
import math as M
import config as P 
from pygame import Vector2 as V
from moveable_obj import Moveable_Obj
from pygame.locals import *

screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
screen = pygame.display.set_mode(screen_size) 

class Blasters(Moveable_Obj):

    def __init__(self, pos, direction, speed):
        super().__init__("pics/green_blast.png", P.G_W, P.G_H, pos)

        self.dir = direction
        self.pos = V(pos)
        self.speed = speed

    def update(self):

        self.rotate()
        self.pos += self.speed
        self.rect.center = self.pos 

    def rotate(self):

        self.image = pygame.transform.rotate(self.rotation_img, -self.dir)
        self.rect = self.image.get_rect(center=self.rect.center)
    
        

        