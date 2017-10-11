(define (domain CarsIntersection)
    (:requirements :strips :equality :fluents)
    (:predicates (Car ?car)
                 (Intersection ?i)
                 (Passed ?car)
    )

    (:functions  (t ?car ?i)
                 (speed ?car)
    )

    (:action SpeedUp
        :parameters (?car ?i)
        :precondition (and (Car ?car) (Intersection ?i) (not (= (speed ?car) 3)))
        :effect (and (increase (speed ?car) 1) (decrease (t ?car ?i) 1))
    )
    
    (:action SlowDown
        :parameters (?car ?i)
        :precondition (and (Car ?car) (Intersection ?i) (not (= (speed ?car) 0)))
        :effect (and (decrease (speed ?car) 1) (increase (t ?car ?i) 1))
    )
    
    (:action MoveTwo
        :parameters (?car1 ?car2 ?i)
        :precondition (and (Car ?car1) (Car ?car2) (Intersection i) (not (= (speed ?car1) 0)) (not (= (speed ?car2) 0)) (not (= (t ?car1 ?i) (t ?car2 ?i))))
        :effect (and (decrease (t ?car1 ?i) 1) (decrease (t ?car2 ?i) 1))
    )

    (:action MoveOne
        :parameters (?car1 ?car2 ?i)
        :precondition (and (Car ?car1) (Car ?car2) (Intersection i) (= (speed ?car1) 0) (not (= (speed ?car2) 0)))
        :effect (decrease (t ?car2 ?i) 1)
    )

    (:action Finish
        :parameters (?car ?i)
        :precondition (and (Car ?car) (Intersection i) (= (t ?car ?i) 0))
        :effect (Passed ?car)
    )
)
