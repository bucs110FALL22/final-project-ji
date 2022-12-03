import pygame
import random
import math
class Ball: 
  '''
  ball to get on screen
  '''
  def __init__(self, box):
    '''
    initializes variables
    '''
    self.bounds = box.getbounds() 
    self.x = random.randint(self.bounds[3], self.bounds[2])
    self.y = random.randint(self.bounds[1], self.bounds[0])
    self.image = pygame.image.load("assets/ball.png").convert()
    self.sizedimage = pygame.transform.scale(self.image, (50, 50))
  def drawball(self, screen): 
    '''
    draws ball onto screen
    '''
    screen.blit(self.sizedimage, (self.x, self.y))
  def ballcorners(self):
    '''
    identifies ball corners
    '''
    return ((self.x + 50, self.y), (self.x, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50))
  def getcollision(self, player):
    '''
    get collisions
    '''
    if math.sqrt(math.pow(abs(player.getcenter()[0] - self.x),2) + math.pow(abs(player.getcenter()[1] - self.y),2)) < 40:
      return True
    else:
      return False