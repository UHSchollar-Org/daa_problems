from Backtrack import Solve
from pathlib import Path
import time

def Eval(test_cases_path, results_path):
    
    with open(test_cases_path,"r") as file:
        cases = file.read().split("Case")
    
    try:
        with open(results_path,'r') as file:
            pos = len(file.read().split("Case")) - 1
    except:
        pos = 0
    
    for i in range(pos,len(cases)):
        _case = cases[i].split("\n")
        if len(_case) == 6:
            k, students_list, failedInP, failedInR = Format_Case(_case)
            sol_start_time = time.time()
            solution = Solve(students_list, failedInP, failedInR, k)
            sol_end_time = time.time()
            case_time = sol_end_time-sol_start_time
            Write_Solution(solution, case_time, results_path)
    
def Format_Case(_case):
    k = int(_case[1])
    students_list = [int(x) for x in _case[2].split()]
    failedInP = [eval(x) for x in _case[3].split()]
    failedInR = [eval(x) for x in _case[4].split()]
    return k, students_list, failedInP, failedInR

def Write_Solution(solution ,case_time, results_path):
    with open(results_path, "a+") as file:
        file.write("Case\n")
        file.write(f"{solution}\n")
        file.write(f"Time : {case_time}\n")

if __name__ == '__main__':
    path = Path.cwd()
    
    
    
    test_cases_path =  path / "first_problem" / "test_cases" / "8_Max_Students_Count_Cases.txt"
    results_path = path / "first_problem" / "results" / "backtrack" / "8_Max_Students_Count_Results.txt"
    Eval(test_cases_path,results_path)