from game import Game
import pygame
import cProfile
#cProfile.run('re.compile("foo|bar")')


# Main loop

def main():

    """Runs game loop and cprofiler"""

    pr = cProfile.Profile()
    pr.enable()
    game = Game()       # Create game object
    game.run()       # Updates game 
    pr.disable()
    pr.print_stats()

if __name__ == "__main__":
    main()