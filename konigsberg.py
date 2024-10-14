from collections import namedtuple
from tabulate import tabulate

# Aim: G(V, E)
Graph = namedtuple('Graph', ['vertices', 'edges'])

# Konigsberg:
vertices = ['A', 'B', 'C', 'D']
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D"),
]

G = Graph(vertices=vertices, edges=edges)

def adjacency_matrix(graph):
    length = len(graph.vertices)
    
    adj = {vertex: [] for vertex in graph.vertices}
    for edge in graph.edges:
        vertex1, vertex2 = edge[0], edge[1]
        adj[vertex1].append(vertex2)
        adj[vertex2].append(vertex1)  
        
    adj_matrix = [[0 for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            cnt = adj[graph.vertices[i]].count(graph.vertices[j])
            adj_matrix[i][j] = cnt
    
    return adj_matrix
    
print(tabulate(adjacency_matrix(G), tablefmt='fancy_grid'))