
from dwave.cloud import Client

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


