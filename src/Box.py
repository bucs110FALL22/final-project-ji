import turtle
import pygame
class Box: 
  def __init__(self, lengthx, lengthy):
      '''
      initializes variables
      '''
      #bounds (max y, min y, max x, min x)
      self.x = lengthx
      self.y = lengthy
     
  def drawbox(self):
      '''
      draws box
      '''
      turtles = turtle.Turtle()
      self.center = (turtle.pos[0] - (self.x/2),turtle.pos[1])
      
      turtles.forward(self.y) 
      turtles.left(90) 
      self.quad1 = turtle.pos
      turtles.forward(self.x) 
      turtles.left(90) 
      self.quad2 = turtle.pos 
      turtles.forward(self.y) 
      turtles.left(90) 
      self.quad3 = turtle.pos
      turtles.forward(self.x) 
      turtles.left(90) 
      self.quad4 = turtle.pos
  def getbounds(self): 
    return (self.quad1[1], self.quad4[1], self.quad1[0], self.quad4[0])
    #bounds (max y, min y, max x, min x)
  def getcenter(self): 
    return self.center