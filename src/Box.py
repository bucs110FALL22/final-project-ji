import pygame
class Box: 
  '''
  creating screen/box
  '''
  def __init__(self, lengthx, lengthy):
      '''
      initializes variables
      '''
      #bounds (max y, min y, max x, min x)
      self.x = lengthx
      self.y = lengthy
      self.minx = 0
      self.miny = 0
      self.maxx = self.minx + self.x
      self.maxy = self.miny + self.y
      self.image = pygame.image.load("assets/gui.jpg").convert()
      self.sizedimage = pygame.transform.scale(self.image, (self.x + self.minx, self.y + self.miny))
  def drawbox(self, surface):
      #pygame.draw.rectangle
      '''
      draws box via pygame
      '''
      white = (255,255,255)
      pygame.draw.rect(surface, white, pygame.Rect(self.minx, self.miny, self.maxx, self.maxy),  2)
      surface.blit(self.sizedimage, (self.minx, self.miny))
  def getbounds(self):
    '''
    certifies the bounds on the screen
    '''
    return (self.maxy + self.miny , self.miny, self.maxx + self.minx, self.minx)
    #bounds (max y, min y, max x, min x)
  def getcenter(self): 
    '''
    determines position
    '''
    return (self.minx + self.maxx/2, self.miny + self.maxy/2)
  def drawmenubackground(self, surface): 
    '''
    draws menu background
    '''
    white = (255,255,255)
    pygame.draw.rect(surface, white, pygame.Rect(self.minx, self.miny, self.maxx, self.maxy))

    
    #pygame.image.load("assets/dogTreat.jpg")

    
    #X = 100
    #Y = 100
    imp = pygame.image.load("assets/dogTreat.jpg").convert()
    scaledimage = pygame.transform.scale(imp, (self.x + self.minx, self.y + self.miny))
    surface.blit(scaledimage, (self.minx, self.miny))
    Black = (0,0,0)
    font = pygame.font.Font(None, 50)
    text = font.render("WASD to move, dodge dog, eat ball", True, Black)
    surface.blit(text, (100, 200))
    #pygame.display.flip()
    
    #OMG YES
    
