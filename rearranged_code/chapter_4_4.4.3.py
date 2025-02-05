import dimod

from dwave.system import DWaveSampler 
from dwave.system import EmbeddingComposite 

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
