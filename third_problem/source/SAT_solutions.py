"""Module that contains a set of different algorithms that solve the Boolean Satisfaction Problem. 
    An entry is established with the following characteristics:
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
    
#region Utils
def check_formula(variables, m, c):
    """Function that checks if the formula is satisfied with the current assignment of truth values to boolean variables.

    Args:
        variables (list): is the list of size n with the truth values of the boolean variables.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula

    Returns:
        bool: True if the formula is satisfied, False otherwise.
    """
    for clause in c:
        clause_result = False
        for literal in clause:
            if literal[0] == '-':
                if variables[abs(int(literal)) - 1] == 0:
                    clause_result = True
                    break
            else:
                if variables[abs(int(literal)) - 1] == 1:
                    clause_result = True
                    break
        if not clause_result:
            return False
    return True

def parse_formula(formula):
    parsed_formula = []
    for i in range(len(formula)):
        clause = formula[i].split()
        parsed_formula.append(clause)
    return parsed_formula
#endregion    

#region Exhaustive Enumeration
def exhaustive_enumeration(n, m, c):
    """Brute Force Method: Lists all possible assignments of truth values 
    to boolean variables and check if any of them satisfies the formula.

    Args:
        n (int): is the number of boolean variables in the formula.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula
    """
    variables = [0] * n
    pos = 0
    formula = parse_formula(c)
    result = generate_assignments(variables, pos, n, m, formula)
    return result

def generate_assignments(variables, pos, n, m, c):
    """Recursive function that checks if the formula is satisfied with the current assignment of truth values to boolean variables.
    If the formula is not satisfied, it changes the truth values of the variables and calls itself again.

    Args:
        variables (list): is the list of size n with the truth values of the boolean variables.
        pos (int): is the position of the variable to be changed.
        n (int): is the number of boolean variables in the formula.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula

    Returns:
        bool: True if the formula is satisfied, False otherwise.
    """
    if pos == n:
        if check_formula(variables, m, c):
            return variables
        else:
            return None
    else:
        variables[pos] = 0
        if generate_assignments(variables, pos + 1, n, m, c):
            return variables
        variables[pos] = 1
        if generate_assignments(variables, pos + 1, n, m, c):
            return variables
        return None
#endregion

#region DPLL backtracking algorithm
def DPLL(n, m, c):
    """Davis-Putnam-Logemann-Loveland algorithm: It is a recursive algorithm that uses the unit propagation and the pure literal rule to simplify the formula.

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
    return DPLL_rec(variables, assignations, n, m, formula)

def DPLL_rec(variables, assignations, n, m, c):
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
        return variables
    
    literal = select_next_literal(variables, c)
    values = select_literal_values(variables, assignations, c, literal)
    
    for value in values:
        new_formula = unit_propagation(literal, value, variables, assignations, c)
        if new_formula:
            result = DPLL_rec(variables,assignations,n,m,new_formula)
            if result:
                return result
    return None
    """else:
        if unit_propagation(variables, n, m, c):
            return DPLL_rec(variables, n, m, c)
        elif pure_literal(variables, n, m, c):
            return DPLL_rec(variables, n, m, c)
        else:
            return None"""
            
def select_next_literal(variables, c):
    import random as rnd
    
    literal = rnd.randint(0,len(variables)-1)
    while(variables[literal] == 1):
        literal = rnd.randint(0,len(variables)-1)
        
    return literal + 1

def select_literal_values(variables, assignations, c, literal):
    import random as rnd
    values = []
    
    value = rnd.randint(0,1)
    values.append(value)
    values.append(abs(value-1))
    
    return values

def unit_propagation(literal, value, variables, assignations, c):
    from copy import deepcopy
    
    new_formula = deepcopy(c)
    assignations[literal-1] = True
    variables[literal - 1] = value
    change = True
    while change:
        new_formula = evaluate(literal, value, variables, new_formula)
        if new_formula:
            for clause in new_formula:
                if len(clause) == 1:
                    if clause[0][0] == '-':
                        literal = abs(int(clause[0]))
                        value = 0
                        variables[literal - 1] = value
                        
                    else:
                        literal = abs(int(clause[0]))
                        value = 1
                        variables[literal - 1] = value
                    change = True
                    break
                else:
                    change = False                    
        else:
            return None
    return new_formula

def evaluate(literal, value, variables, formula):
    from copy import deepcopy
    
    new_formula = []
    for clause in formula:
        if len(clause) == 1:
            if f'{literal}' in clause and value == 0:
                return None
            if f'-{literal}' in clause and value == 1:
                return None

        if (f'{literal}' in clause and value == 1) or (f'-{literal}' in clause and value == 0):
            continue
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
    return new_formula

"""def unit_propagation(variables, n, m, c):
    Function that applies the unit propagation rule to simplify the formula.

    Args:
        variables (list): is the list of size n with the truth values of the boolean variables.
        n (int): is the number of boolean variables in the formula.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula

    Returns:
        bool: True if the formula is simplified, False otherwise.
    
    for i in range(m):
        clause = c[i].split()
        if len(clause) == 1:
            if clause[0][0] == '-':
                variables[abs(int(clause[0])) - 1] = 0
            else:
                variables[abs(int(clause[0])) - 1] = 1
            return True
    return False"""

def pure_literal(variables, n, m, c):
    """Function that applies the pure literal rule to simplify the formula.

    Args:
        variables (list): is the list of size n with the truth values of the boolean variables.
        n (int): is the number of boolean variables in the formula.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula

    Returns:
        bool: True if the formula is simplified, False otherwise.
    """
    literals = set()
    for clause in c:
        literals.update(clause.split())

    for literal in literals:
        if literal[0] == '-':
            opposite_literal = literal[1:]
        else:
            opposite_literal = '-' + literal

        if opposite_literal not in literals:
            variable_index = abs(int(literal)) - 1
            if literal[0] == '-':
                variables[variable_index] = 0
            else:
                variables[variable_index] = 1

            return True

    return False


#endregion