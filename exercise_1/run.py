#!/user/bin/env python3 -tt
"""
01 Graphs
"""

# Imports
from igraph import Graph as i_Graph, plot
import numpy as np
import operator
import igraph as igraph
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.assortativity.neighbor_degree import average_neighbor_degree
from networkx.algorithms.cluster import average_clustering
from networkx.generators import directed
import snap as snap


def greedy_attack(path, is_directed):
    '''Sequentially removes the vertex with the highest degree from the given graph
    and plots the remaining amount of edges in the graph for each removal step
    @param path: Path to a graph file in edgelist format
    '''
    
    if is_directed:
        graph: nx.DiGraph = nx.read_edgelist(path=path)
    else:
        graph: nx.Graph = nx.read_edgelist(path=path)

    graph_degree_view = graph.degree
    graph_degree_dict = {}
    
    for vertex in graph_degree_view:
        graph_degree_dict[vertex[0]] = vertex[1]
    
    graph_degree_dict_sorted = sorted(graph_degree_dict.items(), key=operator.itemgetter(1), reverse=True)
    
    remaining_edges = [graph.number_of_edges()]

    for vertex in graph_degree_dict_sorted:
        if vertex[0] in graph:
            graph.remove_node(vertex[0])
            remaining_edges.append(graph.number_of_edges())
    
    # Plot
    xvalues = range(0, len(graph_degree_dict_sorted)+1)
    yvalues = remaining_edges

    plt.title("Edge persistence under greedy attack")

    # x-value of the point, where 50% of the edges got removed
    idx_50 = len([x for x in yvalues if x >= yvalues[0]*0.5])
    idx_80 = len([x for x in yvalues if x >= yvalues[0]*0.2])
    idx_90 = len([x for x in yvalues if x >= yvalues[0]*0.1])

    plt.axvline(x=idx_50, color="#d3ffcf", label="50% of edges removed", linestyle="--")
    plt.axvline(x=idx_80, color="#fff1cf", label="80% of edges removed", linestyle="--")
    plt.axvline(x=idx_90, color="#ffcfd2", label="90% of edges removed", linestyle="--")
    plt.plot(xvalues, yvalues)

    plt.xlabel("Number of vertices greedily removed")
    plt.ylabel("Number of edges in graph")
    plt.legend()
    plt.show()


def order(path, is_directed):
    graph = i_Graph.Read_Edgelist(path, directed=is_directed)
    return graph.vcount()


def size(path, is_directed):
    graph = i_Graph.Read_Edgelist(path, directed=is_directed)
    return graph.ecount()


def density(path, is_directed):
    graph = i_Graph.Read_Edgelist(path, directed=is_directed)
    order = graph.vcount()
    size = graph.ecount()
    return (2*size) / (order*(order - 1))


def average_shortest_path(path, is_directed):
    if(is_directed):
        graph: nx.DiGraph = nx.read_edgelist(path=path)
    else:
        graph: nx.Graph = nx.read_edgelist(path=path)
    return nx.average_shortest_path_length(graph)


def average_neighbours(path, is_directed, show_plot):
    graph = i_Graph.Read_Edgelist(path, directed=is_directed)

    # Fancy Metric: number of neighbours per node index
    neighbours = list()
    average_neighbors = 0

    # - Iterate all nodes
    for v in graph.vs:
        # - Get their number of neighbours
        n = v.degree()

        average_neighbors += n
        # - Store this number
        neighbours.append(n)

    if show_plot:
        # Plot
        X = range(len(neighbours))
        Y = neighbours
        plt.plot(list(X), Y, 'ro')
        plt.xlabel('Node Index')
        plt.ylabel('Number of Neighbors')
        plt.show()
    else:
        return average_neighbors/order(path, is_directed)


def average_clustering_coefficient(path, is_directed):
    if is_directed:
        graph = snap.LoadEdgeList(snap.TNGraph, path, 0, 1)
    else:
        graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1)
    return graph.GetClustCf()


def number_of_triangles(path, is_directed):
    if is_directed:
        graph = snap.LoadEdgeList(snap.TNGraph, path, 0, 1)
    else:
        graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1)
    return graph.GetTriads()


def main():
    FACEBOOK_GRAPH_PATH = "graphs/facebook_combined.txt"
    FACEBOOK_GRAPH_IS_DIRECTED = False
    EPINION_GRAPH_PATH = "graphs/soc-Epinions1.txt"
    EPINION_GRAPH_IS_DIRECTED = True

    print("#### FACEBOOK SOCIAL CIRCLES ####\n")
    print("Order = " + str(order(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))
    print("Size = " + str(size(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))
    print("Density = " + str(density(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))
    print("Average Neighbours = " + str(average_neighbours(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED, False)))
    print("Average Clustering Coefficient = " + str(average_clustering_coefficient(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))
    print("Number of triangles = " + str(number_of_triangles(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))

    # WARNING: High computation time 
    # print("Average Shortest Path Length = " + str(average_shortest_path(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)))

    # Plot edge persistence under greedy attack
    # greedy_attack(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED)

    # Plot nodes/neighbours amount
    # average_neighbours(FACEBOOK_GRAPH_PATH, FACEBOOK_GRAPH_IS_DIRECTED, True)

    print("\n###########################################\n")

    print("#### EPINION TRUST GRAPH ####\n")
    print("Order = " + str(order(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))
    print("Size = " + str(size(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))
    print("Density = " + str(density(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))
    print("Average Neighbours = " + str(average_neighbours(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED, False)))
    print("Average Clustering Coefficient = " + str(average_clustering_coefficient(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))
    print("Number of triangles = " + str(number_of_triangles(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))

    # WARNING: High computation time
    # print("Average Shortest Path Length = " + str(average_shortest_path(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)))

    # Plot edge persistence under greedy attack
    # greedy_attack(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED)

    # Plot nodes/neighbours amount
    # average_neighbours(EPINION_GRAPH_PATH, EPINION_GRAPH_IS_DIRECTED, True)

# Main body
if __name__ == '__main__':
    main()
