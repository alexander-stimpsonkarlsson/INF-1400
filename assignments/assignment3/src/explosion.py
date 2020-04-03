import pygame
import config as C
from os import path

class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image          = C.IMAGE 
        self.rect           = self.image.get_rect()
        self.rect.center    = pos
        self.frame          = 0
        self.prev_update    = pygame.time.get_ticks()
        self.frame_rate     = 30
    
    def update(self, fps):

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
    

        
        