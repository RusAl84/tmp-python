import networkx as nx

G = nx.path_graph(17)
nx.write_adjlist(G, "test.adjlist")
nx.write_graphml_lxml(G, "fourpath.graphml")

nx.draw(G)
import matplotlib.pyplot as plt
plt.show()
