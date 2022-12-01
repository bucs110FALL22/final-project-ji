import pygame
class Pepsi(pygame.sprite.Sprite): 
  '''
  creating the "Pepsi" class, or the dogs you will have to avoid in the game
  '''
  def __init__(self, x, y, box):
    '''
    initializes variables
    '''
    self.x = x
    self.y = y
    self.bounds = box
    self.rect = self.image.get_rect()
    self.image = pygame.image.load("/assets/dog.png")
    
#speed (y,x)
#bounds (max y, min y, max x, min x)
  def move(self, speed):
    '''
    initializes boundaries within the game
    '''
    if self.y >= self.bounds [0] or self.y <= self.bounds[1]: 
      speed [0] = -speed[0]
    if self.x >= self.bounds [2] or self.x <= self.bounds[3]: 
      speed [1] = -speed[1]
    self.y += speed[0]
    self.x += speed[1]