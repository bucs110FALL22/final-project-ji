import json
import pygame

#x: Start
def initialhighscores():
  
  try:
      with open('highscore.txt', 'r') as f:
          highscores = json.load(f)
  except FileNotFoundError:
      # If the file doesn't exist, use your default values
      highscores = 0
  return highscores
  
def newhighscore(score,highscores):
  if highscores > score:
    with open('highscore.txt', 'w') as f:
      json.dump(highscores, f)
