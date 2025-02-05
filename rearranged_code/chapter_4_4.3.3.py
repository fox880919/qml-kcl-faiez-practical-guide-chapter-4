import dimod

y0, y1 = dimod.Binaries(["y0", "y1"])

cqm = dimod.ConstrainedQuadraticModel()

cqm.set_objective(-2*y0-3*y1)

cqm.add_constraint(y0 + 2*y1 <= 2)

qubo, invert = dimod.cqm_to_bqm(cqm, lagrange_multiplier = 5)
print(qubo)

from dwave.system import DWaveSampler
from dwave.system import EmbeddingComposite 

sampler = EmbeddingComposite(DWaveSampler()) 
result = sampler.sample(qubo, num_reads=10)
print("The solutions that we have obtained are")
print(result)

samples = [] 
occurrences = []
for s in result.data():
    samples.append(invert(s.sample))
    occurrences.append(s.num_occurrences)
sampleset = dimod.SampleSet.from_samples_cqm(samples,cqm,
num_occurrences=occurrences)
print("The solutions to the original problem are") 
print(sampleset)


final_sols = sampleset.filter(lambda s: s.is_feasible) 
final_sols = final_sols.aggregate()
print("The final solutions are")
print(final_sols)