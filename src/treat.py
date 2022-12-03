import pygame
class Treat(pygame.sprite.Sprite):
  '''
  treat creation class
  '''
  def __init__(self, x, y, box, speed, size):
    '''
    initializes variables
    '''
    #bounds (max y, min y, max x, min x)
    self.x = x
    self.y = y
    self.bounds = box
    self.speed = speed
    self.lengthtowidth = size #(x,y)
    self.image = pygame.image.load("assets/treat.jpg")
    self.sizedimage = pygame.transform.scale(self.image, (self.lengthtowidth[0], self.lengthtowidth[1]))
  def getimage(self): 
    '''
    gets treat image
    '''
    return self.image
  def movedown(self): 
    '''
    makes treat move down
    '''
    #right, left, down, up
    if self.gethitbox()[2] >= self.bounds[0]: 
      self.y -= 1
    else: 
      self.y += self.speed
  def moveleft(self): 
    '''
    makes treat move left
    '''
    if self.gethitbox()[1] <= self.bounds[3]: 
      self.x += 1
    else: 
      self.x -= self.speed
  def moveright(self):
    '''
    makes treat move right 
    '''
    if self.gethitbox()[0] >= self.bounds[2]: 
      self.x -= 1
    else: 
      self.x += self.speed
  def moveup(self): 
    '''
    makes treat move up
    '''
    if self.gethitbox()[3] <= self.bounds [1]: 
      self.y += 1
    else: 
      self.y -= self.speed
  def getpos(self): 
    '''
    gets position for treat
    '''
    return (self.x, self.y)
  def getcenter(self): 
    '''
    fixes position
    '''
    return (self.x - self.lengthtowidth[0]/2, self.y - self.lengthtowidth[1]/2)
  def gethitbox(self): 
    '''
    gets the hitbox for treat
    '''
    center = self.getcenter()
    #rightbound, leftbound, upbound, downbound
    rightbound = center[0] + self.lengthtowidth[0]
    leftbound = center[0]
    upbound = center[1] + self.lengthtowidth[1]
    downbound = center[1] 
    #implement with range if inbetween right and left and if between up and down
    return (rightbound, leftbound, upbound, downbound)
  def drawimage(self,screen): 
    '''
    intializes treat image
    '''
    screen.blit(self.sizedimage, self.getcenter())
    