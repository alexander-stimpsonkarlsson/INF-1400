import pygame 
import parameter as P

# Parent class for all on screen objects

class Screen_Obj(pygame.sprite.Sprite):

    def __init__(self, pics, length, height, x, y)

        self.image = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_HEIGHT])      # Where the image is to be
        self.image = pygame.image.load(pics)                                # Loads iamge
        self.image = pygame.transform.scale(self.image, (length, height))   # Transform image to given scale

        self.pos = x, y                                                     # On screen position

        self.rect = self.image.get_Rect(center = (length/2, height/2))      # Center of image is center of rectangle