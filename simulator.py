import numpy as np

class Intersecton:
  def __init__(self,lanes):
    self.time = 0
    #This is for where the cars actually cross each other
    #Assume cars are two units long, one unit wide
    self.grid = np.zeros((lanes*2,lanes*2))

class Car:
  def __init__(self,name,posX,posY,direction):
    self.name = name
    self.speed = 60 #km/s
    self.posX = posX
    self.posY = posY
    self.direction = direction
  
  def speedUp(self):
    pass
    
  def slowDown(self):
    pass
    
  def reserve(self,Intersection):
    #See paper. This reserves a space in the intersection
    pass

def main():
  pass
  
main()
