import networkx as nx
import matplotlib.pyplot as plt
edges = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6),
         (3, 4), (3, 5), (4, 8), (4, 9), (6, 7)]

G = nx.Graph()
G.add_edges_from(edges)
print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("list of all nodes: ", list(G.nodes()))
print("list of all edges:", list(G.edges()))
print("Degree of all nodes: ", dict(G.degree()))
print("list of all nodes we can go to in a single step from node 2: ",
      list(G.neighbors(2)))
nx.draw(G)
plt.show()
