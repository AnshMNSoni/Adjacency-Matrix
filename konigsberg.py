from collections import namedtuple
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt

def undirected(Graph, vertices):
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


def directed(Graph, vertices):
    try:
        edges = []
        
        for i in vertices:
            for j in range(len(vertices)):
                num = int(input("Number of edges between " + i + "-" + vertices[j] + ": "))
                for k in range(num):
                    edges.append((i, vertices[j]))
        
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
        
        print("\nAdjacency Matrix:\n") 
        print(tabulate(adjacency_matrix(G), tablefmt='fancy_grid'))
    except ValueError:
        print("\nSorry! Invalid Input.\n") 


def undiGraph():
    cnt = 0
    edges = []
    
    for i in vertices:
        for j in range(cnt, len(vertices)):
            num = int(input("Number of edges between " + i + "-" + vertices[j] + ": "))
            for k in range(num):
                edges.append((i, vertices[j]))
        cnt += 1
    
    plotGraph = nx.Graph()
    plotGraph.add_nodes_from(vertices)
    plotGraph.add_edges_from(edges)

    nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')

    plt.show()


def diGraph(vertices):
    edges = []
        
    for i in vertices:
        for j in range(len(vertices)):
            num = int(input("Number of edges between " + i + "-" + vertices[j] + ": "))
            for k in range(num):
                edges.append((i, vertices[j]))
    
    plotGraph = nx.DiGraph()
    plotGraph.add_nodes_from(vertices)
    plotGraph.add_edges_from(edges)

    nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')

    plt.show()
    
    
# G(V, E)
Graph = namedtuple('Graph', ['vertices', 'edges'])

# Konigsberg:
vertices = [node for node in input("Enter the vertices of the Graph: ").upper().split()]

# Undirected graph:
# undirected(Graph, vertices)
    
# Directed Graph:
# directed(Graph, vertices)

# diGraph(vertices)
# undiGraph(vertices)