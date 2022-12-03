from src.Box import Box
from src.treat import Treat
from src.dog import Pepsi
import random
import pygame
import sys
import random
import src.highscore
from src.ball import Ball
import json
class Controller:
  '''
  controller of game
  ''' 
  def __init__(self, speed, amount_of_pepsis, screen ):
    '''
    initializes variables
    '''
    self.speed = speed
    self.screen = screen 
    self.box = Box(750,500)
    self.player = Treat(self.box.getcenter()[0], self.box.getcenter()[1], self.box.getbounds(), speed, (50,50))
    self.pepsis = []
    self.amount_of_pepsis = amount_of_pepsis
  def mainloop(self):
    '''
    initializing key recognition to move and determining how you can die from hitting the dogs
    '''
    #screen.blit(background, (0,0))
    Death = 0
    Score = 0
    self.pepsis = [Pepsi(random.randint(self.box.getbounds()[3], self.box.getbounds()[2]), random.randint(self.box.getbounds()[1], self.box.getbounds()[0]), self.box, (51,51), -2, 4) for x in range (self.amount_of_pepsis)]
    clock = pygame.time.Clock()
    balleaten = True
    ball = Ball(self.box)
    while Death == 0:
      
      
      self.box.drawbox(self.screen)
      for pepsi in self.pepsis: 
        pepsi.movedog()
        pepsi.drawimage(self.screen)
      for pepsi in self.pepsis: 
        Death += pepsi.iscollided(self.player)
        
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
        self.player.moveup()
      if keys[pygame.K_s]:
        self.player.movedown()
      if keys[pygame.K_a]:
        self.player.moveleft()
      if keys[pygame.K_d]:
        self.player.moveright()
      if balleaten == True:
        ball = Ball(self.box)
        balleaten = False
      ball.drawball(self.screen)
      if ball.getcollision(self.player):
        balleaten = True
        Score += 1
        print("Collided: " , Score)
        self.pepsis.append(Pepsi(random.randint(self.box.getbounds()[3], self.box.getbounds()[2]), random.randint(self.box.getbounds()[1], self.box.getbounds()[0]), self.box, (51,51), random.randint(-5,5), random.randint(-5,5)))
      self.player.drawimage(self.screen)
      
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      pygame.display.update()
      clock.tick(60)
    self.menuloop(Score)
    
  def isballeaten(self, ball): 
    '''
    determines if ball is eaten by treat
    '''
    istouching = 0
    playerbound = self.player.gethitbox()
    ballcorners = ball.ballcorners()
    for corner in ballcorners: 
      if corner[0] < playerbound[0] and corner[0] > playerbound[1] and corner[1] > playerbound[2] and corner[1] < playerbound[3]:
        istouching = 1
    return istouching 
  
  
  def menuloop (self,highscore): 
    '''
    making menu loop 
    '''
    Loop = 0
    Brown = (101, 67, 33)
    self.box.drawmenubackground(self.screen)
    
    play_coordinates = self.makebuttons(200, 250, 100, 420, Brown, "Click to Play")
    src.highscore.newhighscore(src.highscore.initialhighscores(),highscore)
    self.printscore(src.highscore.initialhighscores())
    while Loop == 0:
          
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               
            elif event.type == pygame.MOUSEBUTTONUP:
               mousepos = pygame.mouse.get_pos()
               if mousepos[0] < play_coordinates[2] and mousepos[0] > play_coordinates[0] and mousepos[1] > play_coordinates[1] and mousepos[1] < play_coordinates [3]: 
                 Loop = 1
      pygame.display.flip()
    self.mainloop()
      
  def printscore(self,score):
    '''
    High score printer
    '''
    Black = (0,0,0)
    font = pygame.font.Font(None, 100)
    text = font.render("High Score: " + str(score), True, Black)
    self.screen.blit(text,(150,100))
  def makebuttons(self, left, top, height, width, color, text): 
    '''
    buttons on menu
    '''
    Black = (0,0,0)
    font = pygame.font.Font(None, 100)
    text = font.render(text, True, Black)
    pygame.draw.rect(self.screen, color, pygame.Rect(left, top, width, height))
    self.screen.blit(text, (left, top))
    return (left, top, left + width, top + height)
    
    
  
