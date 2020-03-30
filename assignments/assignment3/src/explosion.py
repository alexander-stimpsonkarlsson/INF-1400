import pygame
import config as C

class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image          = C.EXPLOSION_ANIMATION[0]
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect           = self.image.get_rect(center = pos)
        self.frame          = 0
        self.prev_update    = pygame.time.get_ticks()
        self.fps            = 50
    
    def update(self):

        tick = pygame.time.get_ticks()
        
        if tick - self.prev_update > self.fps:
            self.prev_update = tick
            self.frame += 1
        if self.frame == len(C.EXPLOSION_ANIMATION):
            self.kill()
        else:
            self.image = C.EXPLOSION_ANIMATION[self.frame]
            self.rect = self.image.get_rect(center = self.rect.center)

