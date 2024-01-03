import networkx as nx
import random

d = [0.01 , 0.05 , 0.1 , 0.5 , 0.9]
t = [100, 250, 500, 750, 1000]

for density in d:
    for size in t:
        for i in range(5):
            seed = random.randint(1,1000000)
            nx_temp = nx.fast_gnp_random_graph(size, density, seed=seed)
            random.seed(seed)
            for (u,v,w) in nx_temp.edges(data=True):
                w['weight'] = round(random.uniform(-10.000, 10.000), 3)
                while (w['weight'] == 0):
                    w['weight'] = round(random.uniform(-10.000, 10.000), 3)
            nx_temp = nx.relabel.convert_node_labels_to_integers(nx_temp)
            graph = nx.Graph()
            graph.add_nodes_from(sorted(nx_temp.nodes()))
            graph.add_edges_from(nx_temp.edges(data=True))
            with open(f"../gb_m10_10f/gb_m10_10f_{size}_{density}_{i}", 'w') as file:
                
                file.write(f"# graph with density {density} created with networkx fast_gnp_random_graph with seed {seed} and edges weighted randomly from [-10,-0.001] and [0.001,10] including three decimals\n")

                file.write(f"{graph.number_of_nodes()} {graph.number_of_edges()}\n")

                # Write each edge along with its weight
                for edge in graph.edges(data=True):
                    node1, node2, data = edge
                    weight = data.get('weight', 1.0)  # If no weight attribute, default to 1.0
                    file.write(f"{node1+1} {node2+1} {weight}\n")
