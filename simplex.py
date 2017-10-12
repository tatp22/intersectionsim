import numpy as np
from scipy.optimize import linprog

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

def makeTBounds(vMax,vMin):
    '''Returns tuple of tuples of each (min,max) bounds'''
    ret = []
    '''Simple Scenario, 2 cars going to hit at same time. One will slow down'''
    ret.append((1600.0/vMax,1600.0/vMin))
    ret.append((1600.5/vMax,1600.5/vMin))
    
    ret.append((1600.0/vMax,1600.0/vMin))
    ret.append((1600.5/vMax,1600.5/vMin))
    
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

def getA(t_bounds,vMax,vMin,orderOfInt,numCars):
    '''Constructs A matrix'''
    A = np.zeros(((numCars+numCars*(numCars+1)//2-numCars),numCars*2))
    '''
    # Constraint 1: Driver has an earliest arrival time
    for i in range(numCars):
        posToIdx = i*4+orderOfInt[i][0]
        A[i][posToIdx] = -1
        #A[i][i+numCars*4] = 1
    
    # Constraint 2: Driver has a latest arrival time
    for i in range(numCars):
        off = numCars
        posToIdx = i*4+orderOfInt[i][0]
        A[i+off][posToIdx] = 1
        #A[i+off][i+numCars*4+off] = 1
    '''
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
    for i in range(numCars):
        for j in range(i,numCars):
            if i == j:
                continue
            off = numCars
            firstIdx = count+off
            secondIdx1 = i*2
            secondIdx2 = j*2
            if t_bounds[i*2][0] < t_bounds[j*2][0]:
                A[firstIdx][secondIdx1] = 1
                A[firstIdx][secondIdx2] = -1
            else:
                A[firstIdx][secondIdx1] = -1
                A[firstIdx][secondIdx2] = 1
            count += 1
    
    return A

def getB(t_bounds,vMax,vMin,orderOfInt,numCars):
    '''Constructs B matrix'''
    b = []
    '''
    # Constraint 1: Driver has an earliest arrival time
    for i in range(numCars):
        di = t_bounds[i*4+orderOfInt[i][0]][0]
        b.append(-di/vMax)
    
    # Constraint 2: Driver has a latest arrival time
    for i in range(numCars):
        di = t_bounds[i*4+orderOfInt[i][0]][0]
        b.append(di/vMin)
    '''
    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    for i in range(numCars):
        b.append(-1)
    
    # Constraint 4: One car can have a position in intersection at once
    for i in range((numCars*(numCars+1))//2-numCars):
        b.append(-2)
        
    return b

def main():
    numCars = 2
    lanes = 1
    vMax = 60
    vMin = 20
    c = np.zeros(numCars*2)
    c.fill(1)
    t_bounds = makeTBounds(vMax,vMin)
    orderOfInt = getOrder(t_bounds)
    A = getA(t_bounds,vMax,vMin,orderOfInt,numCars)
    b = getB(t_bounds,vMax,vMin,orderOfInt,numCars)
    t_bounds = tuple(t_bounds)
    print(len(A),len(A[0]),len(b),len(c))
    print(A)
    print(b)
    print(c)
    print(t_bounds)
    res = linprog(c,A_ub=A,b_ub=b,bounds=t_bounds,options={"disp":True})
    print(res)

main()
