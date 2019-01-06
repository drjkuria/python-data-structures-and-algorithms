from graph import Graph

# Set up Graph
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# Test get_edge_list
print(graph.get_edge_list()) # [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]

# Test get_adjacency_list
print(graph.get_adjacency_list()) # [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]

