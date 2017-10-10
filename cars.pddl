(define (domain CarsIntersection)
  (:requirements :strips :equality)
  (:predicates (Car ?car)
               (Intersection ?i)
               (Reach ?c ?t)
               (Occupied ?int ?t)
               (Has ?car ?speed)
               (Passed ?car)
  )

  (:functions
            (t ?x)
  )

    (:action SpeedUp
        :parameters (?car ?i ?speed ?t)
        :precondition (and (Car ?car) (Intersection ?i) (Has ?car ?speed) (not (= (?speed 3))) (Reach ?car ?t) (not (Occupied ?i (- (t 1)))))
        :effect (and (not (Has ?car ?speed)) (Has ?car ?speed+1) (Reach ?car ?t-1) (Occupied ?i ?t-1))
    )
    
    (:action SlowDown
        :parameters (?car ?i ?speed ?t)
        :precondition (and (Car ?car) (Intersection ?i) (Has ?car ?speed) (not (= (?speed 0)) (Reach ?car ?t) (Occupied ?i ?t) (not (Occupied ?i ?t+1))
        :effect (and (not (Has ?car ?speed)) (Has ?car ?speed-1) (Reach ?car ?t+1) (Occupied ?i ?t+1))
    )
    
    (:action MoveTwo
        :parameters (?car1 ?car2 ?t1 ?t2 ?s1 ?s2)
        :precondition (and (Car ?car1) (Car ?car2) (Has ?car1 ?s1) (Has ?car2 ?s2) (not (= (?s1 0))) (not (= (?s2 0))) (Reach ?car1 ?t1) (Reach ?car2 ?t2) (not (= (?t1 ?t2))))
        :effect (and (Reach ?car1 ?t1-1) (Reach ?car2 ?t2-1))
    )

    (:action MoveOne
        :parameters (?car1 ?car2 ?t1 ?t2)
        :precondition (and (Car ?car1) (Car ?car2) (Has ?car1 ?s1) (Has ?car2 ?s2) (= ?s1 0))
        :effect (Reach ?car2 ?t2-1)
    )

    (:action Finish
        :parameters (?car)
        :precondition (and (Car ?car) (Reach ?car 0))
        :effect (Passed ?car)
    )
)
