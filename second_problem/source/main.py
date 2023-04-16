import graph as gr

g = gr.Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)

print(g.edges)

g.remove_edge(3,4)
print(g.edges)