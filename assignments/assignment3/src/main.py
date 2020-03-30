import pygame
import config as C 
from game import Game

# Main loop

def main():

    pygame.init()                           # Pygame initiazer       

    running = True 

    time = pygame.time.Clock()              # Gets time, used for update frequenzy

    game = Game()                           # Create game object

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Exit by closing window
                running = False
            
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:            # Exit by pressing ESC
            running = False

        fps = time.tick(60)                 # Set update frequency(fps) to 60

        game.update(fps)                    # Updates game 

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()