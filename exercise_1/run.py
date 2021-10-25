#!/user/bin/env python3 -tt
"""
01 Graphs
"""

# Imports
from igraph import Graph, plot
import matplotlib.pyplot as plt

def main():
    g: Graph = Graph.Read_Edgelist('graphs/facebook_combined.txt', directed=False)

    ## EASY metrics
    order: int = g.vcount()
    size: int = g.ecount()
    density: int = (2*size) / (order*(order - 1))

    print("Order: " + str(order))
    print("Size: " + str(size))
    print("Density: " + str(density))



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
