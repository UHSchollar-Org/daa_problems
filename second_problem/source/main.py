import Graph as gr

def init_nodes_dict(graph, value):
    dic = {}
    for u in graph.nodes:
        dic[u] = {}
        for v in graph.nodes:
            dic[u][v] = value
    return dic

def sol1(w_edges):
    g = gr.graph_from_edges(w_edges)
    
    
    
def sol2(w_edges):
    g = gr.graph_from_edges(w_edges)
    
    min_dists = gr.floyd_warshall(g)
    
    inEdges = init_nodes_dict(g, 0)
    sol = init_nodes_dict(g, 0)
    
    for edge in g.edges:
        for node in g.nodes:
            if min_dists[node][edge[0]] + g[edge[0]][edge[1]]['w'] == min_dists[node][edge[1]]:
                inEdges[node][edge[1]] += 1
            if min_dists[node][edge[1]] + g[edge[0]][edge[1]]['w'] == min_dists[node][edge[0]]:
                inEdges[node][edge[0]] += 1

    for v in g.nodes:
        for u in g.nodes:
            for k in g.nodes:
                if min_dists[v][k] + min_dists[k][u] == min_dists[v][u]:
                    sol[v][u] += inEdges[v][k]
    
    return sol
