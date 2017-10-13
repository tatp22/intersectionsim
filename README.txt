----------- Traffic Intersection Planning Problem - Model with PDDL -------------
Domain file: domain.pddl
Problem file: problem1.pddl

Use any solver for PDDL to run it and get a feasible solution. The planner requires to manage :equiality and :fluents (level of PDDL 2.1).

For example, use Metric FF (code to download available here: ), build it and run:

./ff -p path_to_this_directory -o domain.pddl -f problem1.pddl
