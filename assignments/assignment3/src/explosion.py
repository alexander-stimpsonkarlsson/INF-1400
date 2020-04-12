import pygame
import config as C
from os import path

class Explosion(pygame.sprite.Sprite):

    """ Explosion object, takes position as input. 
    """
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image          = C.IMAGE 
        self.rect           = self.image.get_rect()
        self.rect.center    = pos
        self.frame          = 0
        self.prev_update    = pygame.time.get_ticks()
        self.frame_rate     = 30
    
    def update(self):
        
        """ Updates explosion object, takes fps as input which is used for update frequency. Uses dictonary to cycle 
            through images in animation folder. Uses pygame time.get_ticks to set delay between each append of image. If 
            currenct time minus prev_update exceeds the frame_rate limit a new frame (image index) is set. This frame is 
            then used to add the next image in the animation folder thus creating the appearance of animation. When all 
            pictures are cycled through the object is removed (kill).
        """

        time = pygame.time.get_ticks()

        if time - self.prev_update > self.frame_rate:
            self.prev_update = time
            self.frame += 1 
            if self.frame == len(C.EXPLOSION_ANIMATION["standard"]):
                self.kill()
            else: 
                center = self.rect.center
                self.image = C.EXPLOSION_ANIMATION["standard"][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    

        
        