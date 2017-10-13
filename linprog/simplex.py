import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def getPosT(i,j):
    '''Gets the position in the t vector'''
    return i*4+j

def makeTBounds(vMax,vMin,case):
    '''Returns tuple of tuples of each (min,max) bounds'''
    ret = []
    dirArr = []
    tiles = []

    if case == "simple":
        '''Simple Scenario, 2 cars going to hit at same time. One will slow down'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([1,2])
        dirArr.append(0)

        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([3,2])
        dirArr.append(1)

    if case == "three":
        '''Three cars. Two coming at each other, one perp'''
        #car 1
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)

        #car 2
        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)

        #car 3
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)

    if case == "four":
        '''Four cars going to cross intersection at the same time'''
        #car 1
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)

        #car 2
        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)

        #car 3
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)

        #car 4
        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)

    if case == "madeToHit":
        '''3 cars each lane. All come to intersection at same time'''
        #lane 1
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)
        ret.append('new car')
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)
        ret.append('new car')
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)

        #lane 2
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([4,2])
        dirArr.append(1)
        ret.append('new car')
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        tiles.append([4,2])
        dirArr.append(1)
        ret.append('new car')
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        tiles.append([4,2])
        dirArr.append(1)

        #lane 3
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)
        ret.append('new car')
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)
        ret.append('new car')
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)

        #lane 4
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        tiles.append([1,3])
        dirArr.append(3)

    if case == "complicated":
        '''Total mess here. 3+ cars in each lane, 15 total'''
        #lane 1
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)
        ret.append('new car')
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)
        ret.append('new car')
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        tiles.append([3,4])
        dirArr.append(0)

        #lane 2
        ret.append('new car')
        ret.append((2000.0/vMax,2000.0/vMin))
        ret.append((2000.5/vMax,2000.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)
        ret.append('new car')
        ret.append((2400.0/vMax,2400.0/vMin))
        ret.append((2400.5/vMax,2400.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)
        ret.append('new car')
        ret.append((2660.0/vMax,2660.0/vMin))
        ret.append((2660.5/vMax,2660.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)
        ret.append('new car')
        ret.append((2810.0/vMax,2810.0/vMin))
        ret.append((2810.5/vMax,2810.5/vMin))
        tiles.append([4,2])
        dirArr.append(1)

        #lane 3
        ret.append('new car')
        ret.append((1200.05/vMax,1200.05/vMin))
        ret.append((1200.55/vMax,1200.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)
        ret.append('new car')
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)
        ret.append('new car')
        ret.append((2300.05/vMax,2300.05/vMin))
        ret.append((2300.55/vMax,2300.55/vMin))
        tiles.append([2,1])
        dirArr.append(2)

        #lane 4
        ret.append('new car')
        ret.append((1100.0/vMax,1100.0/vMin))
        ret.append((1100.5/vMax,1100.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((1400.0/vMax,1400.0/vMin))
        ret.append((1400.5/vMax,1400.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((2000.0/vMax,2000.0/vMin))
        ret.append((2000.5/vMax,2000.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)
        ret.append('new car')
        ret.append((2400.0/vMax,2400.0/vMin))
        ret.append((2400.5/vMax,2400.5/vMin))
        tiles.append([1,3])
        dirArr.append(3)

    if case == "turn":
        '''2 cars, one of them turns'''
        #car 1 - turn
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        ret.append((1601.05/vMax,1601.05/vMin))
        tiles.append([4,2,1])
        dirArr.append(0)

        #car 2 - straight
        ret.append('new car')
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        tiles.append([3,4])
        dirArr.append(1)

    return ret,dirArr,tiles

def getOverpass(t):
    '''Gets the ideal time that each car would go thru the intersection'''
    ret = 0
    for i in range(len(t)):
        ret += t[i][0]
    return ret

def getStoplight(t,dirArr,stopTime,case):
    '''Gets the time if there were a stoplight in the intersection'''
    '''0/2 go first, then 1/3'''
    ret = 0
    if case == 'turn':
        for i in range(len(t)):
            if i <= 2:
                '''can't go thru has to wait'''
                ret += (((t[i][0]//stopTime)+1)*stopTime+10) # +10 is to simulate slowing down and speeding up again
            else:
                '''can go thru'''
                ret += t[i][0]
    else:
        for i in range(len(t)):
            if (t[i][0]//stopTime)%2 != dirArr[i//2]%2:
                '''can't go thru has to wait'''
                ret += (((t[i][0]//stopTime)+1)*stopTime+10) # +10 is to simulate slowing down and speeding up again
            else:
                '''can go thru'''
                ret += t[i][0]
    return ret

def getOrder(t):
    '''Gets the order of which blocks the car will hit'''
    '''(cars*[first,last])'''
    ret = []
    # For i cars
    for i in range(len(t)//4):
         #finds the min idx
         minVal = 99999999
         minIdx = 0
         for j in range(4):
            if t[getPosT(i,j)][0] != None and t[getPosT(i,j)][0] < minVal:
                minIdx = j
                minVal = t[getPosT(i,j)][0]
         maxIdx = (minIdx+3)%4
         ret.append([minIdx,maxIdx])

    return ret

def getA(t_bounds,vMax,vMin,tiles,numCars):
    '''Constructs A matrix'''

    # Get the width for the matrix, this should be equal to the number of
    # tiles, which is the number of entries in t_bounds that are not "new cars"
    width = 0
    for el in t_bounds:
        if not el == "new car":
            width += 1

    A = []
    currRow = 0

    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    offset = 0
    for r in range(0, len(t_bounds), 2):
        if t_bounds[r] == "new car":
            #the column of interest shifts one to the right if it concerns a new car
            offset += 1
        else:
            column = currRow+offset

            #construct a new row t_i,k - t_i,l
            row = [0] * width
            row[column] = 1
            row[column+1] = -1
            currRow += 1

            #add the row to the A matrix
            A.append(row)

    # Constraint 4: tile can't be occupied by multiple cars at the time
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
            for k in range(len(tiles[i])):
                if tiles[i][k] in tiles[j]:
                    #construct a new row t_i,k != t_j,k
                    row = [0] * width
                    row[k] = 1
                    row[tiles[j][tiles[j].index(tiles[i][k])]] = -1
                    currRow += 1

                    #add the row to the A matrix
                    A.append(row)

    return A

def getB(t_bounds,vMax,vMin,tiles,numCars):
    '''Constructs B matrix'''
    b = []

    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    x = 0
    for r in range(0, len(t_bounds), 2):
        if t_bounds[r] == "new car":
            #the column of interest shifts one to the right if it concerns a new car
            x += 1
        else:
            b.append(0)

    # Constraint 4: tile can't be occupied by multiple cars at the time
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
            for k in range(len(tiles[i])):
                if tiles[i][k] in tiles[j]:
                    b.append(-1)

    return b

def printCarTimes(t,dirs,t_bounds):
    '''Prints the times that each car reached the intersection'''
    for i in range(len(t)//2):
        print("Car {0:02d}, direction {1}: Time = {2:.2f}, Ideal = {3:.2f}".format(i+1,dirs[i],t[2*i],t_bounds[2*i][0]))
    print()

def testOneCase(cars,case):
    '''Test one case for the cars, returns the min function value'''
    numCars = cars
    lanes = 1
    vMax = 60
    vMin = 20
    t_bounds,dirArr,tiles = makeTBounds(vMax,vMin,case)

    #get A matrix and b vector
    A = getA(t_bounds,vMax,vMin,tiles,numCars)
    b = getB(t_bounds,vMax,vMin,tiles,numCars)

    #clean up t_bounds, remove "new car" identifiers
    t_bounds = list(filter(lambda a: a != "new car", t_bounds))

    #get c vector
    c = np.zeros(len(t_bounds))
    c.fill(1)

    #calculate solution
    t_bounds = tuple(t_bounds)
    res = linprog(c,A,b,bounds=t_bounds,options={"disp":False})
    carTimes = res["x"]

    #other scenarios
    overpass = getOverpass(t_bounds)
    stoplight = getStoplight(t_bounds,dirArr,20,case) #20 Second Stoplights
    orderOfInt = getOrder(t_bounds)

    #print case
    print("Case :", case)
    printCarTimes(carTimes,np.zeros(100),t_bounds)

    return res["fun"],overpass,stoplight

def makeNorm(times):
    '''Norm the times to one'''
    ret = []
    ret2= []
    for i in range(len(times)):
        ret.append(times[i][0]/times[i][1])
        ret2.append(times[i][2]/times[i][1])
    return ret,ret2

def plot(t,stopTimes):
    '''fancy bar plotter'''
    N = len(t)
    thresh = 1
    values = np.array(t)
    stopVal = np.array(stopTimes)

    above_threshold = np.maximum(values - thresh, 0)
    below_threshold = np.minimum(values, thresh)

    above_stop = np.maximum(stopVal - thresh, 0)
    below_stop = np.minimum(stopVal, thresh)

    ind = np.arange(N)
    width = .33
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, below_threshold, width, color="r")
    rects2 = ax.bar(ind, above_threshold, width, color="r",bottom=below_threshold)
    rects3 = ax.bar(ind+width,below_stop, width, color="y")
    rects4 = ax.bar(ind+width,above_stop, width, color="y",bottom=below_threshold)

    ax.set_ylabel('Fraction Of Time Over Overpass')
    ax.set_title('Time Lost With Intersection Over Overpass (No. of Cars)')
    ax.set_xticks(ind+width/2)
    ax.set_xticklabels(('Two cars (2)',
                        'Three Cars (3)',
                        'Four Cars (4)',
                        'Cars Made to hit (12)',
                        'Real Life Complex Intersection (15)',
                        'Turning cars (2)'))

    rects = ax.plot([-.2, 5.9], [thresh, thresh], "k--")

    ax.legend((rects[0], rects2[0], rects4[0]),
              ("Overpass Effeciency", 'AI Intersection','Simulated Stoplight'))

    plt.show()

def main():
    cars = [2,3,4,12,15,2]
    case = ["simple","three","four","madeToHit","complicated","turn"]
    times = []
    for i in range(len(cars)):
        times.append(testOneCase(cars[i],case[i]))
    normTimes,stopTimes = makeNorm(times)
    plot(normTimes,stopTimes)

main()
