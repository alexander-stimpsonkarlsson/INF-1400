import pygame
import config as C
from os import path

img_dir = path.join(path.dirname(__file__), "animation")

explosion_animation = {}
explosion_animation["standard"] = []

for i in range(9):
    filename = "explosion0{}.png".format(i)
    image = pygame.image.load(path.join(img_dir, filename)).convert()
    image.set_colorkey(C.BLACK)
    img_standard = pygame.transform.scale(image, (200, 200))
    explosion_animation["standard"].append(img_standard)

class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_animation["standard"][0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.frame = 0
        self.prev_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self, fps):

        time = pygame.time.get_ticks()

        if time - self.prev_update > self.frame_rate:
            self.prev_update = time
            self.frame += 1 
            if self.frame == len(explosion_animation["standard"]):
                self.kill()
            else: 
                center = self.rect.center
                self.image = explosion_animation["standard"][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

            
