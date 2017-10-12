import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

'''
Intersection:
0 1
3 2

Maximize:
-sum(t)
where t is the vector of times for each car and when it will hit the intersection
constraints:
'''
def getPosT(i,j):
    '''Gets the position in the t vector'''
    return i*4+j

def makeTBounds(vMax,vMin,case):
    '''Returns tuple of tuples of each (min,max) bounds'''
    ret = []
    dirArr = []
    if case == "simple":
        '''Simple Scenario, 2 cars going to hit at same time. One will slow down'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(0)
        
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        dirArr.append(1)
        
    if case == "three":
        '''Three cars. Two coming at each other, one perp'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(0)
        
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        dirArr.append(1)
        
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(2)
        
    if case == "four":
        '''Four cars going to cross intersection at the same time'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(0)
        
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        dirArr.append(1)
        
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(2)
        
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        dirArr.append(3)
    
    if case == "madeToHit":
        '''3 cars each lane. All come to intersection at same time'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(0)
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        dirArr.append(0)
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        dirArr.append(0)
        
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(1)
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        dirArr.append(1)
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        dirArr.append(1)
        
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(2)
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        dirArr.append(2)
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        dirArr.append(2)
        
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(3)
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        dirArr.append(3)
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        dirArr.append(3)
    
    if case == "complicated":
        '''Total mess here. 3+ cars in each lane, 15 total'''
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(0)
        ret.append((1900.05/vMax,1900.05/vMin))
        ret.append((1900.55/vMax,1900.55/vMin))
        dirArr.append(0)
        ret.append((2600.05/vMax,2600.05/vMin))
        ret.append((2600.55/vMax,2600.55/vMin))
        dirArr.append(0)
        
        ret.append((2000.0/vMax,2000.0/vMin))
        ret.append((2000.5/vMax,2000.5/vMin))
        dirArr.append(1)
        ret.append((2400.0/vMax,2400.0/vMin))
        ret.append((2400.5/vMax,2400.5/vMin))
        dirArr.append(1)
        ret.append((2660.0/vMax,2660.0/vMin))
        ret.append((2660.5/vMax,2660.5/vMin))
        dirArr.append(1)
        ret.append((2810.0/vMax,2810.0/vMin))
        ret.append((2810.5/vMax,2810.5/vMin))
        dirArr.append(1)
        
        ret.append((1200.05/vMax,1200.05/vMin))
        ret.append((1200.55/vMax,1200.55/vMin))
        dirArr.append(2)
        ret.append((1600.05/vMax,1600.05/vMin))
        ret.append((1600.55/vMax,1600.55/vMin))
        dirArr.append(2)
        ret.append((2300.05/vMax,2300.05/vMin))
        ret.append((2300.55/vMax,2300.55/vMin))
        dirArr.append(2)
        
        ret.append((1100.0/vMax,1100.0/vMin))
        ret.append((1100.5/vMax,1100.5/vMin))
        dirArr.append(3)
        ret.append((1400.0/vMax,1400.0/vMin))
        ret.append((1400.5/vMax,1400.5/vMin))
        dirArr.append(3)
        ret.append((1600.0/vMax,1600.0/vMin))
        ret.append((1600.5/vMax,1600.5/vMin))
        dirArr.append(3)
        ret.append((2000.0/vMax,2000.0/vMin))
        ret.append((2000.5/vMax,2000.5/vMin))
        dirArr.append(3)
        ret.append((2400.0/vMax,2400.0/vMin))
        ret.append((2400.5/vMax,2400.5/vMin))
        dirArr.append(3)
        
    return ret,dirArr

def getOverpass(t):
    '''Gets the ideal time that each car would go thru the intersection'''
    ret = 0
    for i in range(len(t)):
        ret += t[i][0]
    return ret
    
 
def getStoplight(t,dirArr,stopTime):
    '''Gets the time if there were a stoplight in the intersection'''
    '''0/2 go first, then 1/3'''
    ret = 0
    for i in range(len(t)):
        if (t[i][0]//stopTime)%2 != dirArr[i//2]%2:
            '''can't go thru has to wait'''
            ret += (((t[i][0]//stopTime)+1)*stopTime+10)
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

def getA(t_bounds,vMax,vMin,orderOfInt,numCars,dirArr):
    '''Constructs A matrix'''
    A = np.zeros(((numCars+numCars*(numCars+1)//2-numCars),numCars*2))
    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    for i in range(numCars):
        off = 0
        firstIdx = i*2
        secondIdx = i*2+1
        A[i+off][firstIdx] = 1
        A[i+off][secondIdx] = -1
    
    # Constraint 4: One car can have a position in intersection at once
    '''Bigger num is negative, smaller is positive'''
    count = 0
    cArr = []
    for i in range(numCars):
        for j in range(i,numCars):
            if i == j:
                continue
            off = numCars
            firstIdx = count+off
            secondIdx1 = i*2
            secondIdx2 = j*2
            if dirArr[i]%2 != dirArr[j]%2:
                cArr.append(1)
                if t_bounds[i*2][0] <= t_bounds[j*2][0]:
                    A[firstIdx][secondIdx1] = 1
                    A[firstIdx][secondIdx2] = -1
                else:
                    A[firstIdx][secondIdx1] = -1
                    A[firstIdx][secondIdx2] = 1
            else:
                cArr.append(0)
                A[firstIdx][secondIdx1] = 0
                A[firstIdx][secondIdx2] = 0
            count += 1
    
    return A,cArr

def getB(t_bounds,vMax,vMin,orderOfInt,numCars,cArr):
    '''Constructs B matrix'''
    b = []
    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    for i in range(numCars):
        currBegin = t_bounds[i][0]
        currEnd = t_bounds[2*i][0]
        b.append(-1)
    
    # Constraint 4: One car can have a position in intersection at once
    for i in range((numCars*(numCars+1))//2-numCars):
        if cArr[i] == 0:
            b.append(0)
        else:
            b.append(-1)
        
    return b

def testOneCase(cars,case):
    '''Test one case for the cars, returns the min function value'''
    numCars = cars
    lanes = 1
    vMax = 60
    vMin = 20
    c = np.zeros(numCars*2)
    c.fill(1)
    t_bounds,dirArr = makeTBounds(vMax,vMin,case)
    overpass = getOverpass(t_bounds)
    stoplight = getStoplight(t_bounds,dirArr,20)
    orderOfInt = getOrder(t_bounds)
    A,cArr = getA(t_bounds,vMax,vMin,orderOfInt,numCars,dirArr)
    b = getB(t_bounds,vMax,vMin,orderOfInt,numCars,cArr)
    t_bounds = tuple(t_bounds)
    '''
    print(len(A),len(A[0]),len(b),len(c))
    print(A)
    print(b)
    print(c)
    print(t_bounds)
    '''
    res = linprog(c,A,b,bounds=t_bounds,options={"disp":False})
    #print(res)
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
    width = .4
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, below_threshold, width, color="g")
    rects2 = ax.bar(ind, above_threshold, width, color="r",bottom=below_threshold)
    rects3 = ax.bar(ind+width,below_stop, width, color="g")
    rects4 = ax.bar(ind+width,above_stop, width, color="y",bottom=below_threshold)
    
    ax.set_ylabel('Fraction Of Time Over Overpass')
    ax.set_title('Time Lost With Intersection Over Overpass')
    ax.set_xticks(ind+width/2)
    ax.set_xticklabels(('Two',
                        'Three Cars', 
                        'Four Cars', 
                        'Cars Made to hit', 
                        'Real Life Complex Intersection'))

    ax.legend((above_threshold[0], below_threshold[0], below_stop[0]),
              ('Overpass'        , 'AI Intersection' , 'Stoplight'))
    
    ax.plot([0, 4.5], [thresh, thresh], "k--")
    plt.show() 
    

def main():
    cars = [2,3,4,12,15]
    case = ["simple","three","four","madeToHit","complicated"]
    times = []
    for i in range(len(cars)):
        times.append(testOneCase(cars[i],case[i]))
    normTimes,stopTimes = makeNorm(times)
    plot(normTimes,stopTimes)

main()
