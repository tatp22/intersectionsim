----------- Traffic Intersection Planning Problem - Model with PDDL -------------
Domain file: pddl/domain.pddl
Problem file: pddl/problem1.pddl

Use any solver for PDDL to run it and get a feasible solution. The planner requires to manage :equiality and :fluents (level of PDDL 2.1).

For example, use Metric FF (code to download available here: https://fai.cs.uni-saarland.de/hoffmann/metric-ff.html), build it and run:

./ff -p <path_to_this_directory>/pddl/ -o domain.pddl -f problem1.pddl

------- Traffic Intersection Planning Problem - Model with Linear Programming ---
Python File: linprog/simplex.py

Run the simulator for different configurations of cars coming up to an intersection, coming up with a local maximum.

To run: python3 linprog/simplex.py
