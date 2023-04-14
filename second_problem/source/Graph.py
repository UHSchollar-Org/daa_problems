

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

        Returns:
            dict[Any:list]
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
            self.adj_dict[node_for_adding] = []
            
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
            self.adj_dict[u].remove(n)
        del self.adj_dict[n]
        for edge in self._edges:
            if edge[0]==n or edge[1]==n:
                self._edges.remove(edge)
    
    def add_edge(self, u_of_edge, v_of_edge):
        """Add edge between u and v. The node u and v will be 
        automatically added if they are not already in the graph.

        Args:
            u_of_edge (Any): A node can be any hashable Python object except None.
            v_of_edge (Any): A node can be any hashable Python object except None.
        """
        u,v = u_of_edge, v_of_edge
        if u is None or v is None:
            raise ValueError("None cannot be a node")
        if u not in self._nodes:
            self._nodes.append(u)
            self.adj_dict[u] = [v]
        elif v not in self.adj_dict[u]:
            self.adj_dict[u].append(v)
        if v not in self._nodes:
            self._nodes.append(v)
            self.adj_dict[v] = [u]
        elif u not in self.adj_dict[v]:
            self.adj_dict[v].append(u)
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
            #TODO remove edge in self._edges
        except:
            raise KeyError(f"The edge {u}-{v} is not in the graph")
        
    def clear(self):
        """Remove all nodes and edge from the graph
        """
        self._nodes.clear()
        self._edges.clear()
        self.adj_dict.clear()
    