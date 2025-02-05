import dimod

from dwave.system import DWaveSampler 
from dwave.system import EmbeddingComposite 


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
