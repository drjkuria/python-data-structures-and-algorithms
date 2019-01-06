class Node:
    """Basic element of a graph."""
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    """A connection between two nodes."""
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    """A graph representation with edges and nodes and operations."""
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

