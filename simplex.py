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

def makeTBounds():
    '''Returns tuple of tuples of each (min,max) bounds'''
    ret = []
    '''Simple Scenario, 2 cars going to hit at same time. One will slow down'''
    ret.append((None,None))
    ret.append((None,None))
    ret.append((16.55,None))
    ret.append((16.05,None))
    
    ret.append((None,None))
    ret.append((16.5,None))
    ret.append((16.0,None))
    ret.append((None,None))
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

def getA(t_bounds,vMax,vMin,orderOfInt):
    '''Constructs A matrix'''
    numCars = len(t_bounds)//4
    #A = np.zeros(((numCars*3+numCars*(numCars+1)/2),numCars*4+(numCars*3+numCars*(numCars+1)/2)))
    A = np.zeros(((numCars*3+numCars*(numCars+1)//2-1),(numCars*3+numCars*(numCars+1)//2-1)))
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
    
    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    for i in range(numCars):
        off = numCars*2
        firstIdx = i*4+orderOfInt[i][0]
        secondIdx = i*4+orderOfInt[i][1]
        A[i+off][firstIdx] = 1
        A[i+off][secondIdx] = -1
        #A[i+off][i+numCars*4+off] = 1
    
    # Constraint 4: One car can have a position in intersection at once
    '''Bigger num is negative, smaller is positive'''
    count = 0
    for i in range(numCars):
        for j in range(i,numCars-1):
            off = numCars*3
            firstIdx = count+off
            secondIdx1 = i*4+orderOfInt[i][0]
            secondIdx2 = j*4+orderOfInt[j][0]
            secondIdx3 = count+off+numCars*4
            if t_bounds[i*4+orderOfInt[i][0]][0] < t_bounds[j*4+orderOfInt[j][0]][0]:
                A[firstIdx][secondIdx1] = 1
                A[firstIdx][secondIdx2] = -1
            else:
                A[firstIdx][secondIdx1] = -1
                A[firstIdx][secondIdx2] = 1
            #A[firstIdx][secondIdx3] = 1
            count += 1
    
    return A

def getB(t_bounds,vMax,vMin,orderOfInt):
    '''Constructs B matrix'''
    numCars = len(t_bounds)//4
    b = []
    # Constraint 1: Driver has an earliest arrival time
    for i in range(numCars):
        di = t_bounds[i*4+orderOfInt[i][0]][0]
        b.append(-di/vMax)
    
    # Constraint 2: Driver has a latest arrival time
    for i in range(numCars):
        di = t_bounds[i*4+orderOfInt[i][0]][0]
        b.append(di/vMin)
    
    # Constraint 3: Correct way of crossing the intersection (doesn't go backwards)
    for i in range(numCars):
        b.append(0)
    
    # Constraint 4: One car can have a position in intersection at once
    for i in range((numCars*(numCars+1))//2-1):
        b.append(-1)
        
    return b

def main():
    numCars = 2
    lanes = 1
    vMax = 60
    vMin = 20
    c = np.zeros(3*numCars+numCars*(numCars+1)//2-1)
    c.fill(1)
    t_bounds = makeTBounds()
    orderOfInt = getOrder(t_bounds)
    A = getA(t_bounds,vMax,vMin,orderOfInt)
    b = getB(t_bounds,vMax,vMin,orderOfInt)
    t_bounds = tuple(t_bounds)
    print(len(A),len(A[0]),len(b),len(c))
    res = linprog(c,A_ub=A,b_ub=b,bounds=t_bounds,options={"disp":True})
    print(res)

main()
