import networkx as nx
import matplotlib.pyplot as plt
g=nx.barabasi_albert_graph(20,2)
nx.draw(g)
plt.show()
nx.write_gexf(g,"graphing.gexf")