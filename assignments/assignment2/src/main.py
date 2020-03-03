import pygame 
import random
from pygame.locals import *
from boid import Boid

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000                   

WHITE_COLOR = (255, 255, 255)
RED_COLOR = (240, 0, 30)
BLACK_COLOR = (0, 0, 0)

#white_color = (255, 255, 255)
#red_color = (240, 0, 30)
#black_color = (0, 0, 0)

#(screen_width, screen_height) = (1400, 1000)                        # screen spesifications.

def main():                                                         # Function for running the program.

    pygame.init()                                                   # Initialize pygame.
    screen_size = [SCREEN_WIDTH, SCREEN_HEIGHT]                     # Defines screen area.
    screen = pygame.display.set_mode(screen_size)                   # Represents the screen.
    background_image = pygame.image.load("Pics/bcg.png")
    background_image = pygame.transform.scale(background_image, (1400, 1000))
    pygame.display.set_caption("Boids n' voids")
    font = pygame.font.Font('freesansbold.ttf', 32)                 
    
    running = True
    time = pygame.time.Clock()

    flock = []

    while running:
        for event in pygame.event.get():                            # Game loop initialize. 
            if event.type == pygame.QUIT:
                running = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1: # When button is clicked
                boids = Boid()                                # Adds one boid to the list
                flock.append(boids)

        screen.blit(background_image, (0, 0))                       # Draws background.   

        for boids in flock:                                     # Draws all boids
            boids.draw(screen)
            boids.movement()
            boids.avoid_edge()

        time.tick(60)                                               # Computes how many ms have passed 
                                                                    # since prev call, game wont run 
                                                                    # higher than 60 fps/ticks. 
        pygame.display.flip()                                       # Updates surface area

if __name__ == "__main__":                                          # Calls main function and starts
    main()                                                          # the game.

    


