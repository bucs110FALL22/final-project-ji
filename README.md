:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### F
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/jnzvgnaepz-horrify

https://docs.google.com/presentation/d/1s4SJGUp03pBpi-xLsY1T6WCk-SG05SoBTsgxCXb9z4w/edit#slide=id.p

### Team: ji
#### Danielle Gray, Jared Chan

***

## Project Description

Our goal was to create a game based off the arcade game Snake, but instead, you are playing as a dog treat while trying to eat a dodge bouncing dogs as obstacles, with the dogs moving faster and multiplying overtime. Try to get the highest score as possible.

***    

## User Interface Design

- **Initial Concept**
  Menu Screen: A menu screen with a Play! button
  GUI Screen: A nintendogs background with dogs bouncing and you playing as the treat
--------------------------------------------------------------------------
  **bugs**: sometimes the ball/dog spawns outside the barriers
            images have boxes around them
    
    
- **Final GUI**
  - GUI IN-GAME:  https://gyazo.com/21c85ce730cedc17d83cfcac2b2e9387
  - MENU: https://gyazo.com/423b5fc0fe85724b714f55c46050685e

***        

## Program Design
Our goal was to create a game based off the arcade game Snake, but instead, you are playing as a dog treat while trying to eat a dodge bouncing dogs as obstacles, with the dogs moving faster and multiplying overtime. Try to get the highest score as possible.
* Non-Standard libraries
**Pygame**: https://www.pygame.org/docs/ Set of Python modules designed for writing video games
**Math**: https://docs.python.org/3/library/math.html This module provides access to the mathematical functions defined by the C standard.
**Json**: https://docs.python.org/3/library/json.html: A lightweight data interchange format inspired by JavaScript object literal syntax
**Random**: https://www.toppr.com/guides/python-guide/tutorials/modules/modules/random/use-random-module-to-generate-random-numbers-in-python/#:~:text=Q1.-,What%20is%20import%20random%20in%20Python%3F,random%20number%20generation%2Drelated%20functions. Defines a series of functions for generating or manipulating random integers.


* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    Ball: defines the ball boundaries and creates ball
    Box: Draws the screen and addds the background
    Controller: defines text colors, movement of the treat, boundaries of the dog, controls the game itself.
    Pepsi: "Pepsi" class, or the dogs you will have to avoid in the game
    Treat: Creates the treat, what you will be 

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    ball.py
    Box.py
    button.py
    controller.py
    dog.py
    highscore.py
    screen.py
    treat.py
* assets
    ball.png
    dog.png
    dogTreat.jpg
    gui.jpg
    highscore.json
    treat.jpg
* etc
    midterm2.md

***

## Tasks and Responsibilities 

   Danielle and Jared - ball.py
   Jared and Danielle- controller.py
   Jared - highscore.py
   Jared - treat.py
   Danielle - dog.py
   

## Testing
We coded each class bit by bit and tested each method individually.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Open terminal, enter 'python3 main.py' // Run Counter Program  |GUI window appears with High Score = 10 (current high score), move treat to dodge dog, and eat ball; "Click to Play" button on the screen.  |
|  2                   | Click play button   | Display changes to the 2nd GUI screen, with dogs bouncing off the screen and a tennis ball for you to eat.      |
|  3                   | Use the WASD keys to move away from the dog | If dog comes in contact with treat(you), game is over - goes back to the starting menu; if not the game continues. If you continue to eat the tennis ball, your score will increase, and if you beat the high score, your score, or the new high score, will be listed on the menu.    |