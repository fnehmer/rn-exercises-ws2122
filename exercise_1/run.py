#!/user/bin/env python3 -tt
"""
01 Graphs
"""

# Imports
from igraph import Graph as i_Graph, plot
import networkx as nx
import matplotlib.pyplot as plt

def main():
    g_i: i_Graph = i_Graph.Read_Edgelist('graphs/facebook_combined.txt', directed=False)
    g_nx: nx.Graph = nx.read_edgelist(path='graphs/facebook_combined.txt')

    ## metrics
    order: int = g_i.vcount()
    size: int = g_i.ecount() # 88234
    density: int = (2*size) / (order*(order - 1)) # 0.010819963503439287
    aspl: int = nx.average_shortest_path_length(g_nx, False) # 3.6925068496963913

    print("Order: " + str(order)) # 4039
    print("Size: " + str(size)) # 88234
    print("Density: " + str(density)) # 0.010819963503439287
    print("Average Shortest Path Length: " + str(aspl)) # 3.6925068496963913



    # Visualize the graph
    # layout = g.layout("kk")
    # layout = g.layout_kamada_kawai()


    # print("Plotting graph, close window to continue...")
    # Maybe you want to save the graph to a file
    # instead of plotting it here
    # plot(g, layout = layout)

    # # Fancy Metric: number of neighbours per node index
    # neighbours = list()
    # # - Iterate all nodes
    # for v in g.vs:
    #     # - Get their number of neighbours
    #     n = v.degree()
    #     # - Store this number
    #     neighbours.append(n)
    # # - Print it
    # print(["{}:{}".format(i, n) for i, n in enumerate(neighbours)])

    # # Vizualize the metric
    # X = range(len(neighbours))
    # Y = neighbours
    # plt.plot(list(X), Y, 'ro')
    # plt.xlabel('Node Index')
    # plt.ylabel('Number of Neighbors')
    # plt.show()

# Main body
if __name__ == '__main__':
    main()
