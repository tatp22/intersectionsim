import numpy as np
import queue 
import random

class Intersecton:
  '''Intersection class'''
  cars = 0
  def __init__(self,lanes):
    self.time = 0
    #This is for where the cars actually cross each other
    #Assume cars are two units long, one unit wide
    self.grid = np.zeros((lanes*2,lanes*2))
    self.lanes = [[],[],[],[]] # coming FROM N,E,S,W  (Direction,lane,car)
    self.width = lanes
    for i in range(4):
      for j in range(lanes):
        self.lanes[i].append([])

class Car:
  '''Car class'''
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
    if self.speed > 0:
      self.speed -= 1
    
  def reserve(self,Intersection):
    #See paper. This reserves a space in the intersection
    pass

def moveCars(i):
  '''Moves each car their respective speeds in the intersection'''
  for i in range

def spawnCar(i):
  '''Spawns cars into the intersection at random'''
  c = Car()
  # Chance of putting a car in the intersection at all
  chance = random.randint(0,10)
  for ind in range(4):
    for j in range(i.width):
      if chance == 1:
        #put car in the intersection if there is room
        canInsert = True
        if len(i.lanes[ind][j]) != 0):
          nextCar = i.lanes[ind][j][0]
          canInsert = nextCar.pos == 97 and nextCar.speed == 3 or
                      nextCar.pos == 96 and (nextCar.speed == 3 or nextCar.speed == 2) or
                      nextCar.pos == 95 and (nextCar.speed == 3 or nextCar.speed == 2 or nextCar.speed == 1) or
                      nextCar.pos <= 94
        if canInsert:
          i.lanes[ind][j].append(c)

def carReserve(i):
  '''The first car in each lane reserves a spot in the intersection if it can'''
  pass
  
def adjustSpeeds(i):
  '''Adjust the speeds of every car in the intersection to make sure crashes don't happen in each lane'''
  for ind in range(4):
    for j in range(i.width):
      for k in range(len(i.lanes[ind][j])-1,0,-1):
        #current car
        currCar = i.lanes[ind][j][k]
        if k == len(i.lanes[ind][j])-1:
          #This car worries about the reserved spots in the intersection. This is the only one that looks ahead.
          pass
        else:
          #These cars only worry about the car in front of it.
          carInFront = i.lanes[ind][j][k+1]
          if carInFrontTooClose:
            currCar.slowDown()
          if currCarFarAwayEnough:
            currCar.speedUp()
        

def runSimulator(i):
  '''Runs the simulation for T time steps'''
  t = 0
  T = 1000
  # continue simulation for T time steps
  while t < T:
    moveCars(i)
    spawnCar(i)
    carReserve(i)
    adjustSpeeds(i)
    printInfo(i)

def main():
  '''Starts Simulation'''
  Intersection i(1) #1 lane
  runSimulator(i)
  
main()
