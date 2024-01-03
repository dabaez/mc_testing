from maxcutf import MaxCut
import random
import json
import sys
import networkx as nx

# MaxCut(nx_graph, runtime_limit, dim_embedding , hidden_dim , learning_rate , dropout , seed_value = 1)

with open(sys.argv[1], 'r') as file:
    data = json.load(file)

dim_embedding = int(data["dim_embedding"])
hidden_dim = data["hidden_dim"]
learning_rate = float(data["learning_rate"])
dropout = float(data["dropout"])

filename = sys.argv[2]
runtime_limit = float(sys.argv[3])

G = nx.Graph()
with open(filename, 'r') as file:
    while True:
        line = file.readline().strip()
        if not line.startswith('#'):
            break
    num_nodes, num_edges = map(int, line.split())
    for _ in range(num_edges):
        line = file.readline().split()
        node1 = int(line[0])
        node2 = int(line[1])
        weight = float(line[2])
        G.add_edge(node1, node2, weight=weight)
G = nx.relabel.convert_node_labels_to_integers(G)
nx_graph = nx.OrderedGraph()
nx_graph.add_nodes_from(sorted(G.nodes()))
nx_graph.add_edges_from(G.edges(data=True))

time, mc = MaxCut(nx_graph, runtime_limit , dim_embedding , hidden_dim , learning_rate , dropout ,random.randint(1,1000000))

print(str(mc) + "," + str(time))