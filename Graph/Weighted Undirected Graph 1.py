import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_weighted_edgelist('edge_list.txt', delimiter=" ")
population = {
        'Kolkata' : 4486679,
        'Delhi' : 11007835,
        'Mumbai' : 12442373,
        'Guwahati' : 957352,
        'Bangalore' : 8436675,
        'Pune' : 3124458,
        'Hyderabad' : 6809970,
        'Chennai' : 4681087,
        'Thiruvananthapuram' : 460468,
        'Bhubaneshwar' : 837737,
        'Varanasi' : 1198491,
        'Surat' : 4467797,
        'Goa' : 40017,
        'Chandigarh' : 961587
        }
for i in list(G.nodes()):
    G.nodes[i]['population'] = population[i]
nx.draw_networkx(G, with_labels=True)
plt.show()