# import networkx as nx
# import matplotlib.pyplot as plt

# G0 = nx.connected_caveman_graph(6,4)
# G1 = nx.random_reference(G0)

# G = nx.connected_watts_strogatz_graph(50, 4, 0.7)

# # print(nx.sigma(G0), nx.sigma(G1))
# # print(nx.omega(G0), nx.omega(G1))

# nx.draw(G)
# plt.show()

# from Utility.Stochastic import weighted_sample_tup
# a = [(3,'a'), (5,'b'), (20,'c')]
# print(weighted_sample_tup(a, 2, reverse=True))

from Utility.Iterator import float_range
from itertools import product
# for f in float_range(0,1.01,0.01):
#     print(f)
# print(len(list(float_range(0.01,1.01,0.01))))

migration_rates = list(float_range(0.01,1.01,0.01))
epochs_till_migration = list(range(1,15))

for k in product(migration_rates, epochs_till_migration):
    print(k)

print(len(list(product(migration_rates, epochs_till_migration))))