import pygame
class Treat(pygame.sprite.Sprite):
  def __init__(self, x, y, box, speed):
    '''
    initializes variables
    '''
    #bounds (max y, min y, max x, min x)
    self.x = x
    self.y = y
    self.bounds = box
    self.speed = speed
    self.rect = self.image.get_rect()
    self.image = pygame.image.load("../assets/treat.png")
  def moveup(self): 
    '''
    makes treat move up
    '''
    if self.y >= self.bounds[0]: 
      self.y -= 1
    else: 
      self.y += self.speed
  def moveleft(self): 
    '''
    makes treat move left
    '''
    if self.x <= self.bounds[3]: 
      self.x += 1
    else: 
      self.x -= self.speed
  def moveright(self):
    '''
    makes treat move right 
    '''
    if self.x >= self.bounds[2]: 
      self.x -= 1
    else: 
      self.x += self.speed
  def movedown(self): 
    '''
    makes treat move down
    '''
    if self.y <= self.bounds [1]: 
      self.y += 1
    else: 
      self.y -= self.speed
  