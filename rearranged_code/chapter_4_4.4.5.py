import dimod


import greedy
import dimod
J = {(0,1):1, (1,2):1, (2,3):1, (3,0):1}
h = {}
problem = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN) # Sample with SteepestDescentSolver
solver = greedy.SteepestDescentSolver()
solution = solver.sample(problem, num_reads = 10) 
print(solution.aggregate())


import tabu
solver = tabu.TabuSampler()
solution = solver.sample(problem, num_reads = 10) 
print(solution.aggregate())


import neal
solver = neal.SimulatedAnnealingSampler() 
solution = solver.sample(problem, num_reads = 10) 
print(solution.aggregate())


import dwave.system
sampler = dwave.system.LeapHybridSampler() 
solution = solver.sample(problem, num_reads = 10) 
print(solution.aggregate())