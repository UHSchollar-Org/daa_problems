from SAT_solutions import exhaustive_enumeration
from DPLL import DPLL
from genetic import Genetic
from pathlib import Path
from tester import test

path = Path.cwd()
test_cases_path = path / "third_problem" / "source" /"test_cases" / "3SAT"
results_path = path / "third_problem" / "source" / "results"
method1 = Genetic(10,10,0.15)
method2 = DPLL()
test(method2, test_cases_path, results_path)