from utils import check_formula, parse_formula
import random as rnd
from copy import deepcopy

class DPLL:
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
    def __init__(self, literal_strategy : str = "random", value_strategy : str = "random") -> None:
        """Davis-Putnam-Logemann-Loveland algorithm: It is a recursive algorithm that uses the unit propagation 
        and the pure literal rule to simplify the formula.

        Args:
            literal_strategy (str): Literal selection strategy. Options: "random". Default: "random"
            value_strategy (str): Value selection strategy. Options: "random". Default: "random"
        """
        self.next_literal_selection = literal_strategy
        self.next_value_selection = value_strategy
    
    def Solve(self, n, m, c):
        """
        Args:
            n (int): is the number of boolean variables in the formula.
            m (int): is the number of clauses in the formula.
            c (list): is the list of size m with the clauses of the formula

        Returns:
            bool: True if the formula is satisfied, False otherwise.
        """
        variables = [0] * n
        assignations = [False] * n
        formula = parse_formula(c)
        return self.DPLL_rec(variables, assignations, n, m, formula)[0]
    
    def DPLL_rec(self, variables, assignations, n, m, c):
        """Recursive function that checks if the formula is satisfied with the current assignment of truth values to boolean variables.
        If the formula is not satisfied, it applies the unit propagation and the pure literal rule to simplify the formula and calls itself again.

        Args:
            variables (list): is the list of size n with the truth values of the boolean variables.
            n (int): is the number of boolean variables in the formula.
            m (int): is the number of clauses in the formula.
            c (list): is the list of size m with the clauses of the formula

        Returns:
            bool: True if the formula is satisfied, False otherwise.
        """
        if check_formula(variables, m, c):
            #If the formula is satified return the variablles values and True
            return variables, True
    
        #Select the next literal and its value according de heuristic configured
        literal = self.select_next_literal(variables, assignations)
        assignations[literal - 1] = True
        values = self.select_literal_values()
    
        for value in values:
            variables[literal - 1] = value
            new_formula, valid_solution = self.unit_propagation(literal, value, deepcopy(variables), deepcopy(assignations), deepcopy(c))
            if valid_solution:
                result, valid_solution = self.DPLL_rec(deepcopy(variables),deepcopy(assignations),n,m,new_formula)
                if valid_solution:
                    return result, valid_solution
        return None, False
    
    #region Literal Selection
    def select_next_literal(self, variables, assignations):
        """Select the literal selection method according to the strategy 
        configured in "next_literal_selection"
        """
        match self.next_literal_selection:
            case "random":
                return self.random_next_literal(variables, assignations)
            case _:
                return self.random_next_literal(variables, assignations)
    
    def random_next_literal(self, variables, assignations):
        """Select a random literal among the available ones


        Returns:
            int : return a random literal that assignations[literal] == False 
        """
        literal = rnd.randint(0,len(variables)-1)
        while(assignations[literal] == True):
            literal = rnd.randint(0,len(variables)-1)
        
        return literal + 1
    #endregion

    #region Value Selection
    def select_literal_values(self):
        """Select the value selection method according to the strategy 
        configured in "next_value_selection"
        """
        match self.next_value_selection:
            case "random":
                return self.random_literal_value()
            case _:
                return self.random_literal_value()
    
    def random_literal_value(self):
        """Select a random value from those available

        Returns:
            int: Random integer belonging to the range [0,1]
        """
        values = []
    
        value = rnd.randint(0,1)
        values.append(value)
        values.append(abs(value-1))
    
        return values
    #endregion

    def unit_propagation(self, literal, value, variables, assignations, formula):
        """Given a literal and its value, it is evaluated in the formula and if there is a unit clause left, 
        the corresponding value is assigned to that variable and the process is repeated.

        Args:
            literal (_type_): Variable to assign
            value (_type_): Value to assign
            variables (_type_): List of values assigned to each variable
            assignations (_type_): Boolean list representing whether the ith variable was assigned
            formula (_type_): Formula to evaluate

        Returns:
            list, bool: returns the formula resulting from the process 
            and a bool representing whether the assignments were successful
        """
        change = True
        while change:
            formula, valid_solution = self.evaluate(literal, value, variables, formula)
            if valid_solution:
                if formula:
                    for clause in formula:
                        if len(clause) == 1:
                            if clause[0][0] == '-':
                                literal = abs(int(clause[0]))
                                value = 0
                                variables[literal - 1] = value
                                assignations[literal - 1] = True
                            else:
                                literal = abs(int(clause[0]))
                                value = 1
                                variables[literal - 1] = value
                                assignations[literal - 1] = True
                            change = True
                            break
                        else:
                            change = False   
                else:
                    change = False
            else:
                return None, False
        return formula, True

    def evaluate(self, literal, value, variables, formula):
        """Evaluates the value of the literal in the formula by reducing and/or eliminating clauses

        Returns:
            list, bool: returns the formula resulting from the process 
            and a bool representing whether the assignments were successful
        """
        new_formula = []
        for clause in formula:
            #If the clause is unitary, the variable to be evaluated is found in it and its evaluation is 0 
            # then the variable assignments do not satisfy the formula
            if len(clause) == 1:
                if f'{literal}' in clause and value == 0:
                    return None, False
                if f'-{literal}' in clause and value == 1:
                    return None, False

            #if the variable is in the clause and its evaluation is 1, that clause is eliminated
            if (f'{literal}' in clause and value == 1) or (f'-{literal}' in clause and value == 0):
                continue
            #If the variable is in the clause and its evaluation is 0, the variable is removed from the clause.
            elif (f'{literal}' in clause and value == 0) or (f'-{literal}' in clause and value == 1):
                new_clause = deepcopy(clause)
                if f'{literal}' in clause:
                    new_clause.remove(f'{literal}')
                else:
                    new_clause.remove(f'-{literal}')
                new_formula.append(new_clause)
            else:
                new_clause = deepcopy(clause)
                new_formula.append(new_clause)
        return new_formula, True
