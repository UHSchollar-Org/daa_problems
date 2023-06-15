from typing import List
from utils import parse_formula, check_formula

class Exhaustive_Enumeration:
    def __init__(self) -> None:
        """Brute Force Method: Lists all possible assignments of truth values 
        to boolean variables and check if any of them satisfies the formula.
        """
        pass

    def Solve(self,n,m,c):
        """TODO _summary_

        Args:
            n (int): is the number of boolean variables in the formula.
            m (int): is the number of clauses in the formula.
            c (list): is the list of size m with the clauses of the formula

        Returns:
            List[int]: TODO _description_
        """
        variables = [0] * n
        pos = 0
        formula = parse_formula(c)
        result = self.generate_assignments(variables, pos, n, m, formula)
        return result

    def generate_assignments(self, variables, pos, n, m, c):
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
            if self.generate_assignments(variables, pos + 1, n, m, c):
                return variables
            variables[pos] = 1
            if self.generate_assignments(variables, pos + 1, n, m, c):
                return variables
            return None