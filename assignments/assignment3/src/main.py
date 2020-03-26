import pygame
import config as P 
from screen_objects import Screen_Obj
from Star_Destroyer import Star_Destroyer
from Millennium_Falcon import Millennium_Falcon
from moveable_obj import Moveable_Obj
from player import Player
from blaster import Blasters

def main():

    pygame.init()

    screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(screen_size)                   
    background_image = pygame.image.load("pics/bg.png")
    background_image = pygame.transform.scale(background_image, (P.SCREEN_WIDTH, P.SCREEN_HEIGHT))

    pygame.display.set_caption("Mayhem: World leader edition")
    font = pygame.font.Font('freesansbold.ttf', 32) 

    running = True 
    time = pygame.time.Clock()

    # Tests

    millennium_falcon = Millennium_Falcon()
    star_destroyer = Star_Destroyer()
    player_list = pygame.sprite.Group(millennium_falcon, star_destroyer)


    # Test end 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            running = False

        screen.blit(background_image, (0, 0))

        fps = time.tick(60)
        player_list.draw(screen)                                        # Blit bilde, test

        star_destroyer.update(fps)

        millennium_falcon.update(fps)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()