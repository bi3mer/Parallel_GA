import networkx as nx
import matplotlib.pyplot as plt

G0 = nx.connected_caveman_graph(6,4)
G1 = nx.random_reference(G0)

G = nx.connected_watts_strogatz_graph(50, 4, 0.7)

# print(nx.sigma(G0), nx.sigma(G1))
# print(nx.omega(G0), nx.omega(G1))

nx.draw(G)
plt.show()