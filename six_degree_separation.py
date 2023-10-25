import networkx as nx
import numpy
g=nx.read_edgelist("facebook_combined.txt.gz")


n=list(g.nodes())
spll=[]
for u in n:
    for v in n:
        if u!=v:
            l=nx.shortest_path_length(g,u,v)
            print("The shortest length between",u,"and",v,"is: ",l)
            spll.append(l)
min_spll=min(spll)
max_spll=max(spll)
avg_spll=numpy.average(spll)
print("The minimum shortest path: ",min_spll)
print("The maximum shortest path: ",max_spll)
print("The average shortest path: ",avg_spll)