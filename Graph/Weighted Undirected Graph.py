import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
G = nx.Graph()
edges = [(1, 2, 19), (1, 6, 15), (2, 3, 6), (2, 4, 10),
         (2, 6, 22), (3, 4, 51), (3, 5, 14), (4, 8, 20),
         (4, 9, 42), (6, 7, 30)]

G.add_weighted_edges_from(edges)
nx.draw_networkx(G, with_labels=True)

# G = nx.read_edgelist('edge_list.txt', data=[('weight', int)])
df = pd.read_csv('edge_list.txt', delim_whitespace=True, header=None,
                 names=['n1', 'n2', 'weight'])
G = nx.from_pandas_edgelist(df, 'n1', 'n2', edge_attr='weight')
print(list(G.edges(data = True)))
plt.show()