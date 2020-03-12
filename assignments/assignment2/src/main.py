import pygame 
import parameter as P
from pygame.locals import *
from boid import Boid
from hoik import Hoik
from obstacle import Obstacle


""" Flocking simulation including predators and obstacles. The boid and hoiks class both inherit from 
    the parent class in parent.py. THe program is run by running the main.py file. Spawning boids is 
    done by clicking left click and for hoiks its right click. Obstacles can be spawned by pressing 
    down on the scroll wheel. Clear the window by pressing left key. """


def main():                                                         # Function for running the program.

    pygame.init()                                                   # Initialize pygame.

    screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]                 # Defines screen area.
    screen = pygame.display.set_mode(screen_size)                   # Represents the screen.
    background_image = pygame.image.load("pics/background.png")
    background_image = pygame.transform.scale(background_image, (P.SCREEN_WIDTH, P.SCREEN_HEIGHT))

    pygame.display.set_caption("Boids n' hoiks")
    font = pygame.font.Font('freesansbold.ttf', 32)   
    icon = pygame.image.load("pics/reddit.png")
    pygame.display.set_icon(icon)

    
    running = True
    time = pygame.time.Clock()

    flock = []                                                      # Lists
    hoikers = []
    obstacles = []

    while running:
        for event in pygame.event.get():                            # Game loop initialize. 
            if event.type == pygame.QUIT:
                running = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1: # When left button is clicked
                boid = Boid()
                flock.append(boid)                                  # Adds boid
            
            if event.type == MOUSEBUTTONDOWN and event.button == 3: # When right button is clicked
                hoik = Hoik()
                hoikers.append(hoik)                                # Adds hoik
            
            if event.type == MOUSEBUTTONDOWN and event.button == 2: # When scrool button is clicked
                asteroid = Obstacle()
                obstacles.append(asteroid)                          # Adds obstacle 
            
        key = pygame.key.get_pressed()                              

        if key[pygame.K_LEFT]:                                      # If left button is pressed, all lists are cleared
            flock.clear()
            hoikers.clear()
            obstacles.clear()

        screen.blit(background_image, (0, 0))                       # Draws background.   

        for boid in flock:                                          # Updates boids
            boid.update(flock, obstacles)

        for hoik in hoikers:                                        # Updates hoiks
            hoik.update(flock, obstacles)
        
        for asteroid in obstacles:                                  # Updates asteroids
            asteroid.update()

        time.tick(60)                                               # Computes how many ms have passed 
                                                                    # since prev call, game wont run 
                                                                    # higher than 60 fps/ticks. 
        pygame.display.flip()                                       # Updates surface area

    pygame.quit()
    
if __name__ == "__main__":                                          # Calls main function and starts
    main()                                                          # the game.




