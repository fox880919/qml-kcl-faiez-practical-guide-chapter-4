
import dimod

J = {(0,1):1, (0,2):1}

h = {}

problem = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("The problem we are going to solve is:") 

print(problem)

from dwave.system import DWaveSampler

from dwave.system import EmbeddingComposite 

dwaveSampler = DWaveSampler()

sampler = EmbeddingComposite(dwaveSampler) 

result = sampler.sample(problem, num_reads=10) 

print("The solutions that we have obtained are")

print(result)


# from dwave.drivers import __license__

# access token: vnTVmTNnAo4Mch6LjBovLo8Z7VDH8r

