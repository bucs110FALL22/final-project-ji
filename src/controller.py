from Box import Box
from treat import Treat
from dog import Pepsi
class Controller:
  
  def __init__(self, box, speed, amount_of_pepsis):
    '''
    initializes variables
    '''
    self.box = box
    self.player = Treat(box.getcenter[0], box.getcenter[1], box.getbounds(), speed)
    self.dogs = [Pepsi(random.randint(box.getbounds()[3], box.getbounds()[2]), random.randint(box.getbounds()[1], box.getbounds()[0]), box.getbounds()) for x in range (amount_of_pepsis)]
  def mainloop(self):
    '''
    initializing key recognition to move and determining how you can die from hitting the dogs
    '''
    Death = 0
    while Death == 0:
      for dog in self.dogs: 
        dog.move(self.speed)
      for event in pygame.event.get():
        if event.key in [pygame.K_a, pygame.K_LEFT]:
            self.player.moveleft()
        elif event.key in [pygame.K_d, pygame.K_RIGHT]:
            self.player.moveright()
        elif event.key in [pygame.K_w, pygame.K_UP]:
            self.player.moveup()
        elif event.key in [pygame.K_s, pygame.K_DOWN]: 
            self.player.movedown()

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
