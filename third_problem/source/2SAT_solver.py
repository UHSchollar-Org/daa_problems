# -*- coding: utf-8 -*-
from utils import parse_formula
from networkx import DiGraph, topological_sort
from networkx.algorithms.components.strongly_connected import strongly_connected_components
import networkx as nx
#from networkx.algorithms.shortest_paths import *

class TwoSAT_Solver:
    """An entry is established with the following characteristics:
    n m c
    where:
    n is the number of boolean variables in the formula.
    m is the number of clauses in the formula.
    c is the list of size m with the clauses of the formula
    C1
    C2
    ...
    cm
    Ci represents a clause of the formula, which is a disjunction of literals separated by spaces.
    """
    def __init__(self) -> None:
        """
        """
        pass #TODO: implement init
    
    def build_graph(self, formula):
        """Build the implication graph of the formula. The implication graph is a directed graph G = (V, E) where:
        V = {x1, x2, ..., xn, -x1, -x2, ..., -xn} is the set of vertices. Each vertex represents a boolean variable or its negation.
        E = {(xi, -xj), (-xi, xj)} is the set of edges. Each edge represents an implication between two boolean variables. 
        """
        G = DiGraph()
        for clause in formula:
            G.add_edge(-int(clause[0]), int(clause[1]))
            G.add_edge(-int(clause[1]), int(clause[0]))
		
        return G
    
    def Solve(self,n,m,c):
        """
        Args:
            n (int): is the number of boolean variables in the formula.
            m (int): is the number of clauses in the formula.
            c (list): is the list of size m with the clauses of the formula
        """
        formula = parse_formula(c)
        G = self.build_graph(formula)
        scc = list(strongly_connected_components(G))
        print(scc)
        
        if self.contradictory_variables(scc):
            return self.get_variables_Values(G, scc, n)
        else:
            return None
    
    def contradictory_variables(self, scc):
        """Check if there is a variable and its negation in the same strongly connected component.
        """
        for component in scc:
            seen = set()
            for literal in component:
                v = abs(literal)
                if v in seen:
                    return False
                else:
                    seen.add(v)
        return True

    def get_variables_Values(self, G, scc, n):
        """Get the truth values of the variables in the formula.

        Args:
            scc : strongly connected components of the implication graph
            G : implication graph
        """
        variables = [0] * n
        assigments = [False] * n
        
        compressed_graph = self.compress_graph(G, scc)
        topological_order = list(reversed(list(topological_sort(compressed_graph))))
        
        for component in topological_order:
            nodes = compressed_graph.nodes[component]["strongly_connected_component"]
            if not self.contradictory_component(nodes, variables, assigments):
                for node in nodes:
                    literal = abs(node)
                    assigments[literal - 1] = True
                    variables[literal - 1] = 1 if node >= 0 else 0
        
        return variables
    
    def compress_graph(self, G, scc):
        # Create the compressed graph
        compressed_graph = nx.DiGraph()

        # Map each strongly connected component to a node in the compressed graph
        for i, component in enumerate(scc):
            compressed_graph.add_node(i, strongly_connected_component=component)

        # Traverse all edges of the original graph
        for u, v in G.edges():
            component_u = None
            component_v = None

            # Find the strongly connected component to which nodes u and v belong
            for i, component in enumerate(scc):
                if u in component:
                    component_u = i
                if v in component:
                    component_v = i

            # If nodes u and v belong to different strongly connected components,
            # add an edge between the corresponding nodes in the compressed graph
            if component_u != component_v:
                compressed_graph.add_edge(component_u, component_v)

        return compressed_graph

    def contradictory_component(self, nodes, variables, assigments):
        """Check if there is a contradiction between assigning truth values to the nodes 
        of the strongly connected component and the already made assignments."

        Args:
            nodes (list): Nodes belonging to a strongly connected component
            variables (list): List of values assigned to each literal
            assigments (list): Boolean list representing whether the literal was assigned

        Returns:
            bool: If there is a contradiction return True
        """
        for node in nodes:
            literal = abs(node)
            contradiction = variables[literal-1] != int(node>=0)
            if assigments[literal - 1] and contradiction:
                return True
        return False


