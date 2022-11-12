import pygame
import random

class Ghost(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.image = pygame.image.load("Ghost.png")
    self.rect = self.image.get_rect()
    self.health = 10
    self.speed = 4
    self.width = 2
    self.damage = 1
    self.alive = True
    self.x = x
    self.y = y
  def XCoordinate(self):
  return self.x
  def YCoordinate(self):
  return self.y
  goto(pacman.x + 1, pacman.y + 1)
#movement/track to pacman rough draft
  