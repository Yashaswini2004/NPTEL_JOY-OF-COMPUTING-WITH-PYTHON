import networkx as nx
import matplotlib.pyplot as plt
g=nx.gnp_random_graph(20,0.9)
print(g.nodes())
print(g.edges())
print("degree:",g.degree(0))
nx.draw(g)
plt.show()
