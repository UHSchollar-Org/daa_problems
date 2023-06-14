import random
from pathlib import Path

def generate_SAT_formula(num_variables, num_clauses, num_literals=3):
    """
    Generates a random SAT formula with num variables variables and num_classes clauses. 
    Each clause has num_literals literals.
    """
    formula = []
    for i in range(num_clauses):
        clause = []
        for j in range(num_literals):
            literal = random.randint(1, num_variables)
            while literal in clause or -literal in clause:
                literal = random.randint(1, num_variables)
            if random.randint(0, 1):
                literal *= -1
            clause.append(literal)
        formula.append(clause)
    return formula

def generate_SAT_formula_file( path, num_variables, num_clauses, num_literals=3,):
    """
    Generates a random SAT formula with num variables variables and num_classes clauses. 
    Each clause has num_literals literals and saves it to a file.
    """
    file_name = path/f"{num_literals}SAT"/f"{num_variables}_{num_clauses}_{num_literals}SAT_Cases.txt"
    with open(file_name, "w") as file:
        for _ in range(5000):
            formula = generate_SAT_formula(num_variables, num_clauses, num_literals)
            file.write(f"Case\n")
            for clause in formula:
                for literal in clause:
                    file.write(f"{literal} ")
                file.write("\n")