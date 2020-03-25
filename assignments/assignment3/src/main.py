import pygame
import parameter as P 
from screen_objects import Screen_Obj
from kim import Kim
from trump import Trump
from moveable_obj import Moveable_Obj
from player import Player

def main():

    pygame.init()

    screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(screen_size)                   
    background_image = pygame.image.load("pics/background.png")
    background_image = pygame.transform.scale(background_image, (P.SCREEN_WIDTH, P.SCREEN_HEIGHT))

    pygame.display.set_caption("Mayhem: World leader edition")
    font = pygame.font.Font('freesansbold.ttf', 32) 

    running = True 
    time = pygame.time.Clock()

    # Tests

    kim = Kim()
    trump = Trump()
    player_list = pygame.sprite.Group(kim, trump)


    # Test end 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))

        fps = time.tick(60)
        player_list.draw(screen)                                        # Blit bilde, test

        kim.control()
        kim.update(fps)

        trump.control()
        trump.update(fps)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()