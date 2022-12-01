import pygame
from src.box import Box

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.flip()

    #Create an instance on your controller object
    #Call your mainloop
    pygame.display.update()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
    BVariable = Box(80,100)
    BVariable.drawbox()
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
