import pygame
import math as M
import config as C 
from pygame         import Vector2 as V
from moveable_obj   import Moveable_Obj

# Class for blasters, used in player class, inherits from moveable obj

class Blasters(Moveable_Obj):

    """ Child class of moveable_obj. Passes on x and y (length and height) in inheritance tree. Takes pics, pos and direction
        as input arguments
    """

    def __init__(self, pos, direction, speed, pics):
        super().__init__(pics, C.BLASTER_W, C.BLASTER_H, pos)

        self.dir    = direction
        self.pos    = pos
        self.speed  = speed

    def update(self):

        """ Updates position of blaster object depending on speed, takes fps as input arguments to set frequence of update
        """

        self.rotate()
        self.pos += self.speed
        self.rect.center = self.pos 

    def rotate(self):

        """ Rotates blaster object so that blaster image is pointing at the direction its travelling
        """

        self.image = pygame.transform.rotate(self.rotation_img, -self.dir)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect[0] -= 20
        self.rect[1] -= 30
    
        

        