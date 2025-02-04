
import dimod

J = {(0,1):1, (0,2):1}

h = {}

problem = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("The problem we are going to solve is:") 

print(problem)

from dwave.system import DWaveSampler

from dwave.system import EmbeddingComposite 

# from dwave.drivers import __license__

dwaveSampler = DWaveSampler(token='')

sampler = EmbeddingComposite(dwaveSampler) 

result = sampler.sample(problem, num_reads=10) 

print("The solutions that we have obtained are")

print(result)

# api token is needed but I can't sign up 

