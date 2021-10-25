#!/user/bin/env python3 -tt
"""
01 Graphs
"""

# Imports
from igraph import Graph, plot
import matplotlib.pyplot as plt

def main():
    g = Graph.Read_Ncol('graphs/facebook_combined.txt', directed=False)


    # Visualize the graph
    layout = g.layout("kk")
    layout = g.layout_kamada_kawai()
    print("Plotting graph, close window to continue...")
    # Maybe you want to save the graph to a file
    # instead of plotting it here
    plot(g, layout = layout)

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
