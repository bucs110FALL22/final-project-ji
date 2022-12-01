import json
import pygame

#x: Start

def __init__(self): 
  self.score = json.loads(open("assets/highscore.json").read()) #for strings

def verifyscore(self, score):
  self.score = sorted(self.score)
  if sorted[0] > score:
    self.add_score(score)
  self.score[:3]

def add_score(self): 
  fref = open("assets/highscore.json", w)
  json.dump(fref, self.score)
  fref.close()