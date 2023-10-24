import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
n=nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
print(g.nodes())
print(g.edges())
nx.draw(g)
plt.show()