#!/user/bin/env python3 -tt
"""
01 Graphs
"""

# Imports
from igraph import Graph as i_Graph, plot
import numpy as np
import operator
import igraph
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.assortativity.neighbor_degree import average_neighbor_degree
from networkx.algorithms.cluster import average_clustering
from networkx.generators import directed
import snap


def greedy_attack(path):
    '''Sequentially removes the vertex with the highest degree from the given graph
    and plots the remaining amount of edges in the graph for each removal step
    '''
    graph = nx.read_edgelist(path=path)
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
    line_value = np.interp(40000, xvalues, yvalues)

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


def main():
    g_i: i_Graph = i_Graph.Read_Edgelist('graphs/facebook_combined.txt', directed=False)
    g_nx: nx.Graph = nx.read_edgelist(path='graphs/facebook_combined.txt')

    #Facebook Graph, loaded with SNAP 
    G1 = snap.LoadEdgeList(snap.TNGraph, 'graphs/facebook_combined.txt', 0, 1)
    
    #Epinions Graph, loaded with SNAP 
    G2 = snap.LoadEdgeList(snap.TNGraph, "graphs/soc-Epinions1.txt", 0, 1)
    
    #Metrics for Facebook Graph (G1)
    #Average clustering coefficient
    print("Facebook Graph:")
    print("Average clustering coefficient: " + str(G1.GetClustCf()))
    #Number of triangles
    print("Number of triangles: " + str(G1.GetTriads()))


    #Metrics for Epinions Graph (G2)
    #Average clustering coefficient
    print("Epinions Graph:")
    print("Average clustering coefficient: " + str(G2.GetClustCf()))
    #Number of triangles
    print("Number of triangles: " + str(G2.GetTriads()))
    print("Number of edges: " + str(G2.GetEdges()))
    print("Number of edges: " + str(G2.GetEdges()))


    ## metrics
    order: int = g_i.vcount()
    #size: int = g_i.ecount() # 88234
    #density: int = (2*size) / (order*(order - 1)) # 0.010819963503439287
    #aspl: int = nx.average_shortest_path_length(g_nx, False) # 3.6925068496963913

    #print("Order: " + str(order)) # 4    print(sorted_neighbours_dict)039
    #print("Size: " + str(size)) # 88234
    #print("Density: " + str(density)) # 0.010819963503439287
    #print("Average Shortest Path Length: " + str(aspl)) # 3.6925068496963913


    # Visualize the graph
    # layout = g.layout("kk")
    # layout = g.layout_kamada_kawai()


    # print("Plotting graph, close window to continue...")
    # Maybe you want to save the graph to a file
    # instead of plotting it here
    # plot(g, layout = layout)

    # Fancy Metric: number of neighbours per node index
    neighbours = list()
    average_neighbors = 0

    # - Iterate all nodes
    for v in g_i.vs:
        # - Get their number of neighbours
        n = v.degree()

        average_neighbors += n
        # - Store this number
        neighbours.append(n)
    # - Print it
    # average metrik
    avg = average_neighbors/order
    print(avg)

    greedy_attack('graphs/facebook_combined.txt')


    # neighbours_list = ["{}:{}".format(i, n) for i, n in enumerate(neighbours)]
    #print(neighbours_list)
    #mean_dis = mean_distance(g_i, directed = False, unconnected = False)


    print(avg)
    # Vizualize the metric
    X = range(len(neighbours))
    Y = neighbours
    # plt.plot(list(X), Y, 'ro')
    # plt.xlabel('Node Index')
    # plt.ylabel('Number of Neighbors')
    # plt.show()

    #print(mean_dis)
# Main body
if __name__ == '__main__':
    main()
