from dwave.cloud import Client

#token is needed
for solver in Client.from_config().get_solvers():
    print(solver)


from dwave.system import DWaveSampler 
sampler=DWaveSampler(solver='DW_2000Q_6') 
print("Name:",sampler.properties["chip_id"])
print("Number of qubits:",sampler.properties["num_qubits"]) 
print("Category:",sampler.properties["category"])
print("Supported problems:",sampler.properties["supported_problem_types"])
print("Topology:",sampler.properties["topology"])
print("Range of reads:",sampler.properties["num_reads_range"])

sampler=DWaveSampler(solver='DW_2000Q_6') 
print("Couplings:",sampler.properties["couplers"])

J = {(0,1):1, (0,2):1, (1,2):1}
h = {}
triangle = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

# Embed it and solve it on the DW_2000Q_6 annealer
sampler = EmbeddingComposite(DWaveSampler(solver = "DW_2000Q_6"))
result = sampler.sample(triangle, num_reads=10,
return_embedding = True)
print("The samples obtained are")
print(result)
print("The embedding used was")
print(result.info["embedding_context"])

sampler = DWaveSampler(solver = "Advantage_system4.1") 
print("The default annealing time is",
sampler.properties["default_annealing_time"],"microseconds") 
print("The possible values for the annealing time (in microseconds)"\
    " lie in the range",sampler.properties["annealing_time_range"])


J = {(0,1):1, (0,2):1, (1,2):1}
h = {}
triangle = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
sampler = EmbeddingComposite(DWaveSampler(solver = "DW_2000Q_6")) 
result = sampler.sample(triangle, num_reads=10, annealing_time = 100) 
print("The samples obtained are")
print(result)


forward_schedule=[[0.0, 0.0], [5.0, 0.25], [25, 0.75], [30, 1.0]]

forward_schedule=[[0.0, 0.0], [5.0, 0.25], [25, 0.75], [30, 1.0]]
sampler = EmbeddingComposite(DWaveSampler())
result = sampler.sample(triangle, num_reads=10,
    anneal_schedule = forward_schedule)

reverse_schedule=[[0.0, 1.0], [10.0, 0.5], [20, 1.0]]

reverse_schedule=[[0.0, 1.0], [10.0, 0.5], [20, 1.0]]
initial_state = {0:1, 1:1, 2:1}
sampler = EmbeddingComposite(DWaveSampler())
result = sampler.sample(triangle, num_reads=10,
    anneal_schedule = reverse_schedule,
    reinitialize_state=False, initial_state = initial_state)
print("The samples obtained are") 
print(result)

sampler = DWaveSampler("Advantage_system4.1")
print("The coupling strength range is", sampler.properties["h_range"])


sampler = EmbeddingComposite(DWaveSampler("Advantage_system4.1"))
# Define the problem
x0 = dimod.Binary("x0")
x1 = dimod.Binary("x1")
x2 = dimod.Binary("x2")
blp = dimod.ConstrainedQuadraticModel()
blp.set_objective(-5*x0+3*x1-2*x2)
blp.add_constraint(x0 + x2 <= 1, "First constraint")
blp.add_constraint(3*x0 -x1 + 3*x2 <= 4, "Second constraint")

# Convert the problem and run it
qubo, invert = dimod.cqm_to_bqm(blp, lagrange_multiplier = 10)
result = sampler.sample(qubo, num_reads=100)
# Aggregate and show the results
samples = []
occurrences = []
for s in result.data():
    samples.append(invert(s.sample))
    occurrences.append(s.num_occurrences)
sampleset = dimod.SampleSet.from_samples_cqm(samples,blp,
num_occurrences=occurrences)
print("The solutions to the original problem are") 
print(sampleset.filter(lambda s: s.is_feasible).aggregate())


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