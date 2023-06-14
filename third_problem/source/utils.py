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
    """Parse a formula in list(string) form to a list(list(string))

    Args:
        formula (list): is the list with the clauses of the formula

    Returns:
        list(list(string)): resulting formula
    """
    parsed_formula = []
    for i in range(len(formula)):
        clause = formula[i].split()
        parsed_formula.append(clause)
    return parsed_formula
