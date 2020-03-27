import pygame 
import config as C

# Parent class for all on screen objects

class Screen_Obj(pygame.sprite.Sprite):

    def __init__(self, pics, length, height, pos):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.image          = pygame.Surface([C.SCREEN_WIDTH, C.SCREEN_HEIGHT])     # Where the image is to be
        self.image          = pygame.image.load(pics)                               # Loads iamge
        self.image          = pygame.transform.scale(self.image, (length, height))  # Transform image to given scale
        self.rect           = self.image.get_rect()                                 # Center of image is center of rectangle
        self.rect.center    = self.pos                                              # Pos of where image is draw also
        self.rotation_img   = self.image
       