

class Graph:
    """Base class for undirected graphs
    
    The Graph class allows any hashable object as a node.
    Self-loops are allowed but multiple edges are not
    """
    
    def __init__(self):
        """Initialize a graph. An empty graph is created
        """
        self._nodes = []
        self._edges = []
        self.adj_dict = {}
    
    @property
    def nodes(self):
        """List of all nodes from the graph

        Returns:
            list[Any]
        """
        return self._nodes
    
    @property
    def edges(self):
        """Graph tuples set holding all the edges 

        Returns:
            list[tuple]
        """
        return self._edges
    
    @property
    def adj(self):
        """Graph adjacency object holding the neighbors of each node.
        The neighbor-dict is keyed by neighbor to the edge-data-dict.  
        So `G.adj[3][2]['color'] = 'blue'` sets the color of the edge 
        `(3, 2)` to `"blue"`.

        Returns:
            dict[Any:dict]
        """
        return self.adj_dict
    
    def __iter__(self):
        """Iterate over the nodes. Use: 'for n in G'.
        """
        return iter(self._nodes)
    
    def __len__(self):
        """Return the number of nodes in the graph. Use: 'len(G).
        """
        return len(self._nodes)
    
    def __contains__(self, n):
        """Return True if n is a node, False otherwise. Use: 'n in G'.

        Args:
            n (Any): A node in the graph.
        """
        try:
            return n in self._nodes
        except TypeError:
            return False
    
    def __getitem__(self, n):
        """Returns a list of neighbors of node n. Use: 'G[n]'.
        
        Args:
            n (Any): A node in the graph.
        """    
        return self.adj_dict[n]
    
    def add_node(self, node_for_adding):
        """Add a single node 'node_for_adding'.

        Args:
            node_for_adding (Any): A node can be any hashable Python object except None.
        """
        if node_for_adding not in self._nodes:
            if node_for_adding is None:
                raise ValueError("None cannot be a node")
            self._nodes.append(node_for_adding)
            self.adj_dict[node_for_adding] = {}
            
    def remove_node(self, n):
        """Remove node n and all adjcent edges.
        If n is a non-existent node will raise an exception.

        Args:
            n (Any): A node in the graph
        """
        try:
            neighbors = self.adj_dict[n]
            self._nodes.remove(n)
        except:
            raise KeyError(f"The node {n} is not in the graph")
        
        for u in neighbors:
            del self.adj_dict[u][n]
        del self.adj_dict[n]
        for edge in self._edges:
            if edge[0]==n or edge[1]==n:
                self._edges.remove(edge)
    
    def add_edge(self, u_of_edge, v_of_edge, **attr):
        """Add edge between u and v. The node u and v will be 
        automatically added if they are not already in the graph.
        Edge attributes can be specified with keywords or by directly
        accessing the edge's attribute dictionary.

        Args:
            u_of_edge (Any): A node can be any hashable Python object except None.
            v_of_edge (Any): A node can be any hashable Python object except None.
            attr : keyword arguments, optional
        """
        u,v = u_of_edge, v_of_edge
        if u is None or v is None:
            raise ValueError("None cannot be a node")
        if u not in self._nodes:
            self._nodes.append(u)
            self.adj_dict[u] = {v:{}}
        """elif v not in self.adj_dict[u]:
            self.adj_dict[u].append(v)"""
        if v not in self._nodes:
            self._nodes.append(v)
            self.adj_dict[v] = {u:{}}
        """elif u not in self.adj_dict[v]:
            self.adj_dict[v].append(u)"""
            
        datadict = self.adj_dict[u].get(v, {})
        datadict.update(attr)
        self.adj_dict[u][v] = datadict
        self.adj_dict[v][u] = datadict
        
        if (u,v) not in self._edges and (v,u) not in self._edges:
            self._edges.append((u,v))  
            
    def remove_edge(self, u, v):
        """Remove the edge between u and v.

        Args:
            u (Any): _description_
            v (Any): _description_
        """
        try:
            self.adj_dict[u].remove(v)
            if u != v:
                self.adj_dict[v].remove(u)
            for edge in self._edges:
                if (edge[0]==u and edge[1]==v) or (edge[0]==v and edge[1]==u):
                    self._edges.remove(edge)
        except:
            raise KeyError(f"The edge {u}-{v} is not in the graph")
        
    def clear(self):
        """Remove all nodes and edge from the graph
        """
        self._nodes.clear()
        self._edges.clear()
        self.adj_dict.clear()
        

def BFS(g: Graph, s):
    """Breadth-first search algorithm

    Args:
        g (Graph): Graph object
        s (Any): Starting node

    Returns:
        dict[Any:int]: Dictionary with the distance from s to each node
    """
    distances = {}
    distances[s] = 0
    queue = []
    queue.append(s)
    
    while queue:
        u = queue.pop(0)
        for v in g.adj[u].keys():
            if v not in distances:
                distances[v] = distances[u] + 1
                queue.append(v)
    
    return distances
