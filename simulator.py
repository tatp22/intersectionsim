import numpy as np

class Intersecton:
  def __init__(self,lanes):
    self.time = 0
    #This is for where the cars actually cross each other
    #Assume cars are two units long, one unit wide
    self.grid = np.zeros((lanes*2,lanes*2))
    self.map = np.zeros((200,200)) #for coming up to the intersection

class Car:
  def __init__(self,number,posX,posY,direction):
    self.number = number #identifier
    self.speed = 3 #move 3 tiles at a time. Speed goes from 0-3
    self.posX = posX #position of FRONT bumper
    self.posY = posY #position of FRONT bumper
    self.direction = direction #direction of travel
  
  def speedUp(self):
    pass
    
  def slowDown(self):
    pass
    
  def reserve(self,Intersection):
    #See paper. This reserves a space in the intersection
    pass

def spawnCar():
  pass

def runSimulator(i):
  pass

def main():
  Intersection i(1) #1 lane
  runSimulator(i)
  
main()
