(define (domain CarsIntersection)
  (:requirements :strips :equality :adl)
  (:predicates (CarUp?cu)
               (CarRight?cr)
               (Has?car?speed)
               (At?car?posx?posy)
               (Occupied?x?y)
  )

  (:action Move0Right
    :parameters (?car ?speed ?x ?y)
    :precondition CarRight(car) and At(car,x,y) and Has(car,speed) and Occupied(x+1,y) 
    :effect (not Has(car,speed)) and Has(car,0)
   )

  (:action Move0Up
    :parameters (?car ?speed ?x ?y)
    :precondition CarUp(car) and At(car,x,y) and Has(car,speed) and Occupied(x,y+1)
    :effect (not Has(car,speed)) and Has(car,0)
   )

  (:action Move1Right
    :parameters (?car ?speed ?x ?y)
    :precondition CarRight(car) and At(car,x,y) and Has(car,speed) and (speed<=2) and (not Occupied(x+1,y)) and Occupied(x+2,y)
    :effect (not Has(car,speed)) and Has(car,1) and (not At(car,x,y)) and (not Occupied(x,y)) and At(car,x+1,y) and Occupied(x+1,y)
   )

  (:action Move1Up
    :parameters (?car ?speed ?x ?y)
    :precondition CarUp(car) and At(car,x,y) and Has(car,speed) and (speed<=2) and (not Occupied(x,y+1)) and Occupied(x,y+2)
    :effect (not Has(car,speed)) and Has(car,1) and (not At(car,x,y))  and (not Occupied(x,y)) and At(car,x,y+1) and Occupied(x,y+1)
   )

  (:action Move2Right
    :parameters (?car ?speed ?x ?y)
    :precondition CarRight(car) and At(car,x,y) and Has(car,speed) and (speed>=1) and (speed<=3) and (not Occupied(x+1,y)) and (not Occupied(x+2,y)) and Occupied (x+3,y)
    :effect (not At(car,x,y))  and (not Occupied(x,y)) and (not Has(car,speed)) and Has(car,2) and At(car,x+2,y) and Occupied(x+2,y)
   )

    (:action Move2Up
    :parameters (?car ?speed ?x ?y)
    :precondition CarUp(car) and At(car,x,y) and Has(car,speed) and (speed>=1) and (speed<=3) and (not Occupied(x,y+1)) and (not Occupied(x,y+2)) and Occupied (x,y+3)
    :effect (not At(car,x,y))  and (not Occupied(x,y)) and (not Has(car,speed)) and Has(car,2) and At(car,x,y+2) and Occupied(x,y+2)
   )

    (:action Move3Right
    :parameters (?car ?speed ?x ?y)
    :precondition CarRight(car) and At(car,x,y) and Has(car,speed) and (speed>=2) and (not Occupied(x+1,y)) and (not Occupied(x+2,y)) and (not Occupied(x+3,y))
    :effect (not At(car,x,y)) and (not Occupied(x,y)) and (not Has(car,speed)) and Has(car,3) and At(car,x+3,y) and Occupied(x+3,y)
   )

    (:action Move3Up
    :parameters (?car ?speed ?x ?y)
    :precondition CarUp(car) and At(car,x,y) and Has(car,speed) and (speed>=2) and (not Occupied(x,y+1)) and (not Occupied(x,y+2)) and (not Occupied(x,y+3))
    :effect (not At(car,x,y)) and (not Occupied(x,y)) and (not Has(car,speed)) and Has(car,3) and At(car,x,y+3) and Occupied(x,y+3)
   )
)


(define (problem testCase1)
  (:domain CarsIntersection)
  (:objects c1 c2)
  (:init CarRight(c1) CarUp(c2) At(c1,0,5) At(c2,5,0) Has(c1,2) Has(c2,2) Occupied(5,0) Occupied(0,5))
  (:goal At(c1,6,5) and At(c2,5,6))
)

