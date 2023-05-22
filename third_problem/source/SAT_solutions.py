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
    result = generate_assignments(variables, pos, n, m, c)
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

def check_formula(variables, m, c):
    """Function that checks if the formula is satisfied with the current assignment of truth values to boolean variables.

    Args:
        variables (list): is the list of size n with the truth values of the boolean variables.
        m (int): is the number of clauses in the formula.
        c (list): is the list of size m with the clauses of the formula

    Returns:
        bool: True if the formula is satisfied, False otherwise.
    """
    for i in range(m):
        clause = c[i].split()
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
        