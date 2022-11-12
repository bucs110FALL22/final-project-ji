milestone 2 template
======================================================================

# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1
class Pacman
  def Pacman()
    self.lives = 3
    self.health = 15
    self.block = False
    self.width = 2
    self.speed = 3
    self.damage = 10
  methods:
    reset()
    move_right()
    move_left()
    move_down()
    move_up()
    
   

## Class Interface 2
class Ghost
    def Ghost()
    self.health = 10
    self.speed = 4
    self.width = 2
    self.damage = 1
  methods: 
    move_right()
    move_left()
    move_down()
    move_up()
    

## Class Interface 3
class Food
    def Food()
    self.replenish = 5
    self.move
  methods:
    add_food()
    health_boost()


======================================================================
