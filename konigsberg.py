from collections import namedtuple
from tabulate import tabulate

# Aim: G(V, E)
Graph = namedtuple('Graph', ['vertices', 'edges'])

# Konigsberg:
vertices = [node for node in input("Enter the vertices of the Graph: ").capitalize().split()]

try:
    cnt = 0
    edges = []
    
    for i in vertices:
        for j in range(cnt, len(vertices)):
            num = int(input("Number of edges between " + i + "-" + vertices[j] + ": "))
            for k in range(num):
                edges.append((i, vertices[j]))
        cnt += 1
    
    G = Graph(vertices=vertices, edges=edges)
    
    def adjacency_matrix(graph):
        length = len(graph.vertices)
        # 
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
    
    print("\nAdjacency Matrix:\n") 
    print(tabulate(adjacency_matrix(G), tablefmt='fancy_grid'))
except ValueError:
    print("\nSorry! Invalid Input.\n")