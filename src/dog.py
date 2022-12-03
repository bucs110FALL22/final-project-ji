import pygame
import math
class Pepsi(pygame.sprite.Sprite): 
  '''
  creating the "Pepsi" class, or the dogs you will have to avoid in the game
  '''
  def __init__(self, x, y, box, size, speedx, speedy):
    '''
    initializes variables
    '''
    self.x = x
    self.y = y
    self.bounds = box
    self.speedx = speedx
    self.speedy = speedy
    self.size = size #(x,y)
    self.image = pygame.image.load("assets/dog.png").convert()
    self.sizedimage = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
  def gethitbox(self): 
    '''
    determines dog hitbox
    '''
 #right, left, down, up #bounds (max y, min y, max x, min x)
    rightbound = self.x + self.size[0]
    leftbound = self.x
    downbound = self.y + self.size[1]
    upbound = self.y
    return (rightbound, leftbound, downbound, upbound)
  def movedog(self): 
    '''
    dog movements
    '''
    hitbox = self.gethitbox()
    bounds = self.bounds.getbounds()
    if hitbox[0] >= bounds[2]: 
      self.speedx = -self.speedx
    if hitbox[1] <= bounds[3]: 
      self.speedx = -self.speedx
    if hitbox[2] <= bounds[1]: 
      self.speedy = -self.speedy
    if hitbox[3] >= bounds[0]: 
      self.speedy = -self.speedy
    self.x += self.speedx
    self.y += self.speedy
  def drawimage(self, screen):
    '''
    draws dog image
    '''
    screen.blit(self.sizedimage, self.getcenter())
  def getcenter(self): 
    '''
    position center
    '''
    return (self.x + self.size[0]/2, self.y + self.size[1]/2)
  def getcorners(self): 
    '''
    corners initialized
    '''
    getbounds = self.gethitbox()
    return ((getbounds[0], getbounds[3]), (getbounds[1], getbounds[3]), (getbounds[1], getbounds[2]), (getbounds[0], getbounds[2]))
  def iscollided(self,player):
    '''
    collisions
    '''
    if math.sqrt(math.pow(abs(player.getcenter()[0] - self.x),2) + math.pow(abs(player.getcenter()[1] - self.y),2)) < 40:
      return True
    else:
      return False
      