import pygame 
import random
from param import param1
from boid import Boid

white_color = (255, 255, 255)
red_color = (240, 0, 30)
black_color = (0, 0, 0)

(screen_width, screen_height) = (1400, 1000)                        # screen spesifications.


def main():                                                         # Function for running the program.

    pygame.init()                                                   # Initialize pygame.
    screen_size = [screen_width, screen_height]                     # Defines screen area.
    screen = pygame.display.set_mode(screen_size)                   # Represents the screen.
    background_image = pygame.image.load("Pics/bcg.png")
    background_image = pygame.transform.scale(background_image, (1400, 1000))
    pygame.display.set_caption("Boids n' voids")
    font = pygame.font.Font('freesansbold.ttf', 32)                 
    
    running = True
    time = pygame.time.Clock()

    boid = Boid(screen, 500, 500)

    while running:
        for event in pygame.event.get():                            # Game loop initialize. 
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))                       # Draws background.    

        menu = font.render("Press SPACE to start", running, white_color, black_color) 
        menu_text = menu.get_rect()
        menu_text.center = (screen_width/2, screen_height/2)
        screen.blit(menu, menu_text)

        boid.update()

        time.tick(60)                                               # Computes how many ms have passed 
                                                                    # since prev call, game wont run 
                                                                    # higher than 60 fps/ticks. 
        pygame.display.flip()                                       # Updates surface area

if __name__ == "__main__":                                          # Calls main function and starts
    main()                                                          # the game.

    




