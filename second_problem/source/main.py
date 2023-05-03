import Graph as gr

g = gr.Graph()
g.add_edge(1,2,w=1)
g.add_edge(1,3,w=1)
g.add_edge(2,4,w=1)
g.add_edge(2,5,w=2)
g.add_edge(2,6,w=4)
g.add_edge(3,4,w=1)
g.add_edge(3,5,w=2)

print(gr.floyd_warshall(g))

    