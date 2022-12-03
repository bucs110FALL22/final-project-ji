import pygame
from src.Box import Box
from src.controller import Controller
def main():
    pygame.init()
    screen = pygame.display.set_mode((750,500))
    pygame.display.flip()

    #Create an instance on your controller object
    #Call your mainloop
    pygame.display.update()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
    
    newgame = Controller(5, 2, screen)
    newgame.menuloop(0)
if __name__ == '__main__':
    main()

