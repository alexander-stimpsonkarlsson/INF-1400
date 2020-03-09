import pygame 
import random
from pygame.locals import *
from boid import Boid
import param as P


def main():                                                         # Function for running the program.

    pygame.init()                                                   # Initialize pygame.
    screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]                     # Defines screen area.
    screen = pygame.display.set_mode(screen_size)                   # Represents the screen.
    background_image = pygame.image.load("Pics/bcg.png")
    background_image = pygame.transform.scale(background_image, (P.SCREEN_WIDTH, P.SCREEN_HEIGHT))
    pygame.display.set_caption("Boids n' voids")
    font = pygame.font.Font('freesansbold.ttf', 32)                 
    
    running = True
    time = pygame.time.Clock()

    flock = pygame.sprite.Group()
    Boid.box = flock

    while running:
        for event in pygame.event.get():                            # Game loop initialize. 
            if event.type == pygame.QUIT:
                running = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1: # When button is clicked
                Boid()                                              # Adds one boid to the sprite group
                
        screen.blit(background_image, (0, 0))                       # Draws background.   

        flock.update()
        flock.draw(screen)

        time.tick(60)                                               # Computes how many ms have passed 
                                                                    # since prev call, game wont run 
                                                                    # higher than 60 fps/ticks. 
        pygame.display.flip()                                       # Updates surface area

    pygame.quit()
    
if __name__ == "__main__":                                          # Calls main function and starts
    main()                                                          # the game.




