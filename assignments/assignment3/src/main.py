import pygame
import parameter as P 

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        screen.blit(background_image, (0, 0))

        time.tick(60)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()