import numpy as np
import queue 

class Intersecton:
  def __init__(self,lanes):
    self.time = 0
    #This is for where the cars actually cross each other
    #Assume cars are two units long, one unit wide
    self.grid = np.zeros((lanes*2,lanes*2))
    self.lanes = [[],[],[],[]] # coming FROM N,E,S,W  (Direction,lane,car)
    for i in range(4):
      for j in range(lanes):
        self.lanes[i].append([])

class Car:
  totalCars = 0
  
  def __init__(self):
    self.number = totalCars #identifier
    self.speed = 3 # move 3 tiles at a time. Speed goes from 0-3
    self.pos = 100 # 100 tiles to the intersection
    totalCars += 1
  
  def speedUp(self):
    if self.speed < 3:
      self.speed += 1
    
  def slowDown(self):
    
    
  def reserve(self,Intersection):
    #See paper. This reserves a space in the intersection
    pass

def spawnCar():
  pass

def runSimulator(i):
  

def main():
  Intersection i(1) #1 lane
  runSimulator(i)
  
main()
