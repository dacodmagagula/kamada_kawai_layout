# Create Network 4
N4 = nx.Graph()

# Create all Nodes
for x in range(1,7):
    N4.add_node(x)

# Create all edges

N4.add_edge(1,3)
N4.add_edge(2,3)
N4.add_edge(4,3)
N4.add_edge(4,5)
N4.add_edge(6,5)
N4.add_edge(7,5)

N4.edges()

list(nx.isolates(N4))
pos = nx.drawing.layout.kamada_kawai_layout(N4)
nx.drawing.nx_pylab.draw_kamada_kawai(N4, node_size = 15, node_color=cols) 