import pygame
import config as C

class Explosion(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.rect           = self.image.get_rect(center = pos)
        self.frame          = 0
        self.prev_update    = pygame.time.get_ticks()
        #self.fps            = 50
    
    def update(self, pos, fps):
        
        for x in range(15):
            self.frame += 1
            print(self.frame)
            self.static_image = pygame.image.load(C.EXPLOSION_ANIMATION[self.frame])
            self.image = pygame.transform.scale(self.static_image, (400, 400))
            self.rect = self.image.get_rect(center = pos)
            
        #if self.frame == len(C.EXPLOSION_ANIMATION):
        #    self.kill()

            
