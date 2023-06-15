from DPLL import DPLL
from genetic import Genetic
from exhaustive_enumeration import Exhaustive_Enumeration
from pathlib import Path
from tester import test, validate

path = Path.cwd()
test_cases_path = path / "third_problem" / "source" /"test_cases" / "3SAT"
results_path = path / "third_problem" / "source" / "results"
method1 = Genetic(10,10,0.15)
method2 = DPLL()
method3 = Exhaustive_Enumeration()
#test(method3, test_cases_path, results_path)
validate(method1,method3)