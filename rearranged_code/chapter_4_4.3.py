import dimod

x0 = dimod.Binary("x0")
x1 = dimod.Binary("x1")
x2 = dimod.Binary("x2")

blp = dimod.ConstrainedQuadraticModel()

blp.set_objective(-5*x0+3*x1-2*x2)

blp.add_constraint(x0 + x2 <= 1, "First constraint")

blp.add_constraint(3*x0 -x1 + 3*x2 <= 4, "Second constraint")

print("Our variables are:") 
print(blp.variables) 
print("Our objective is:") 
print(blp.objective) 
print("Our constraints are:") 
print(blp.constraints)

sample1 = {"x0":1, "x1":1, "x2":1}
print("The assignment is", sample1)
print("Its cost is", blp.objective.energy(sample1)) 
print("Is it feasible?",blp.check_feasible(sample1)) 
print("The violations of the constraints are")
print(blp.violations(sample1))

sample2 = {"x0":0, "x1":0, "x2":1}
print("The assignment is", sample2)
print("Its cost is", blp.objective.energy(sample2)) 
print("Is it feasible?",blp.check_feasible(sample2)) 
print("The violations of the constraints are") 
print(blp.violations(sample2))

solver = dimod.ExactCQMSolver()
solution = solver.sample_cqm(blp)
print("The list of assignments is")
print(solution)

feasible_sols = solution.filter(lambda s: s.is_feasible)
print(feasible_sols.first)