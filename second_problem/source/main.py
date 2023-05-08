import Graph as gr

def init_nodes_dict(graph, value):
    dic = {}
    for u in graph.nodes:
        dic[u] = {}
        for v in graph.nodes:
            dic[u][v] = value
    return dic
    
def sol(w_edges):
    g = gr.graph_from_edges(w_edges)
    
    min_dists = gr.floyd_warshall(g)
    
    w = init_nodes_dict(g, 0)
    sol = init_nodes_dict(g, 0)
    
    for edge in g.edges:
        for node in g.nodes:
            if min_dists[node][edge[0]] + g[edge[0]][edge[1]]['w'] == min_dists[node][edge[1]]:
                w[node][edge[1]] += 1
            if min_dists[node][edge[1]] + g[edge[0]][edge[1]]['w'] == min_dists[node][edge[0]]:
                w[node][edge[0]] += 1

    for u in g.nodes:
        for v in g.nodes:
            for w in g.nodes:
                if min_dists[u][w] + min_dists[w][v] == min_dists[u][v]:
                    sol[u][v] += w[u][w]
    
    return sol
