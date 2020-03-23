import pygame 
import parameter as P

screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
screen = pygame.display.set_mode(screen_size) 

# Parent class for all on screen objects

class Screen_Obj(pygame.sprite.Sprite):

    def __init__(self, pics, length, height, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image  = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_HEIGHT])     # Where the image is to be
        self.image  = pygame.image.load(pics)                               # Loads iamge
        self.image  = pygame.transform.scale(self.image, (length, height))  # Transform image to given scale
        self.pos    = pos                                                   # On screen position
        self.rect   = self.image.get_rect(center = (pos))                   # Center of image is center of rectangle
                                                                            # Pos of where image is draw also
