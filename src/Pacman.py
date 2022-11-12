import pygame
import random

class Pacman(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.lives = 3
    self.health = 15
    self.width = 2
    self.speed = 3
    self.damage = 10
    self.image = pygame.image.load("Pacman.png")
    self.rect = self.image.get_rect()
    keyPressed = ("up, down, right, left")
  def X(self):
    return self.x
  def Y(self):
    return self.y
    
  def leftright(self):
    if keyPressed("left"):
     self.x -= 3
    else: 
     self.x += 3
  def movedownup(self):
    if keyPressed("down"):
    self.y -= 3
    else:
    self.y += 3 
  #movement function
    
