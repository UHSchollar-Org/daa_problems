# -*- coding: utf-8 -*-
from utils import parse_formula
from networkx import DiGraph, topological_sort
from networkx.algorithms.components.strongly_connected import strongly_connected_components
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
        scc = strongly_connected_components(G)
        
        if self.contradictory_variables(scc):
            return self.get_variables_Values(scc, G)
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

    def get_variables_Values(self, scc, G):
        """Get the truth values of the variables in the formula.

        Args:
            scc : strongly connected components of the implication graph
            G : implication graph
        """
        #TODO: implement get_variables_Values
        #return list(scc)
        #return list(topological_sort(G))

method = TwoSAT_Solver()
#formula = [ "1 3", "-1 2", "-2 3"]
formula = [ "1 2", "-2 -3", "-1 3", "3 -2"]
print(method.Solve(3,4,formula))