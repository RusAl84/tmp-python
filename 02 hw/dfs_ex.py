import networkx as nx
import matplotlib.pyplot as plt

#https://networkx.guide/algorithms/graph-traversals/dfs/

with open("graph.txt") as f:
    lines = f.readlines()

edgeList = [line.strip().split() for line in lines]

g = nx.Graph()
g.add_edges_from(edgeList)

pos = nx.planar_layout(g)

nx.draw(g, pos, with_labels=True, node_color="#f86e00")

dfs = nx.dfs_tree(g, source="go")

nx.draw(dfs, pos, with_labels=True, node_color="#f86e00", edge_color="#dd2222")

plt.show()