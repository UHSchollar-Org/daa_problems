from Backtrack import Solve as bk
from O_n_Solution import Solve as on
from DP import Solve as dp
from pathlib import Path
import time

def Eval(test_cases_path, results_bk_path, results_on_path, results_dp_path):
    
    with open(test_cases_path,"r") as file:
        cases = file.read().split("Case")
    
    try:
        with open(results_bk_path,'r') as file:
            pos = len(file.read().split("Case")) - 1
    except:
        pos = 0
    
    for i in range(pos,len(cases)):
        _case = cases[i].split("\n")
        if len(_case) == 5:
            k, elements_list, failedInP = Format_Case(_case)
            sol_start_time = time.time()
            solution = on(elements_list, failedInP, k)
            sol_end_time = time.time()
            case_time = sol_end_time-sol_start_time
            Write_Solution(solution, case_time, results_on_path)
    
    for i in range(pos,len(cases)):
        _case = cases[i].split("\n")
        if len(_case) == 5:
            k, elements_list, failedInP = Format_Case(_case)
            sol_start_time = time.time()
            solution = dp(elements_list, failedInP, k)
            sol_end_time = time.time()
            case_time = sol_end_time-sol_start_time
            Write_Solution(solution, case_time, results_dp_path)
    
    for i in range(pos,len(cases)):
        _case = cases[i].split("\n")
        if len(_case) == 5:
            k, elements_list, failedInP = Format_Case(_case)
            sol_start_time = time.time()
            solution = bk(elements_list, failedInP, k)
            sol_end_time = time.time()
            case_time = sol_end_time-sol_start_time
            Write_Solution(solution, case_time, results_bk_path)
    
def Format_Case(_case):
    k = int(_case[1])
    elements_list = [int(x) for x in _case[2].split()]
    failedInP = [int(x) for x in _case[3].split()]
    return k, elements_list, failedInP

def Write_Solution(solution ,case_time, results_path):
    with open(results_path, "a+") as file:
        file.write("Case\n")
        file.write(f"{solution}\n")
        file.write(f"Time : {case_time}\n")

def Check(pathbk, pathon, pathdp):
    with open(pathbk,"r") as file:
        res1 = file.read().split("Case")
        
    with open(pathon, "r") as file:
        res2 = file.read().split("Case")
    
    with open(pathdp, "r") as file:
        res3 = file.read().split("Case")
    
    lres1 = []
    lres2 = []
    lres3 = []
    
    for i in range(1, len(res1)):
        lres1.append(res1[i].split('\n')[1])
        lres2.append(res2[i].split('\n')[1])
        lres3.append(res3[i].split('\n')[1])
    
    checker = lres1 == lres2 and lres1 == lres3
    
    if not checker:
        errors1 = []
        errors2 = []
        
        print("O(n) Solution Errors in case:")
        for i in range(len(lres1)):
            if lres1[i] != lres2[i]:
                errors1.append(i)
                
        if len(errors1):
            print(f"{len(errors1)*100/len(lres2)} percent of errors")
            #print(errors1)
        else:
            print("None")
            
        print("\n")
        
        print("Dp Solution Errors in case:")
        for i in range(len(lres1)):
            if lres1[i] != lres3[i]:
                errors2.append(i)
        
        if len(errors2):
            print(f"{len(errors2)*100/len(lres3)} percent of errors")
            #print(errors2)
        else:
            print("None")
            
    else:
        print("Non Errors")
    
if __name__ == '__main__':
    path = Path.cwd()
    
    test_cases_path =  path / "first_problem" / "test_cases"
    results_bk_path = path / "first_problem" / "results" / "backtrack"
    results_on_path = path / "first_problem" / "results" / "on"
    results_dp_path = path / "first_problem" / "results" / "dp"
    
    i = 2
    while i <= 16:
        itest_cases_path = test_cases_path / f"{i}_Max_Students_Count_Cases.txt"    
        iresults_bk_path = results_bk_path / f"{i}bk_Max_Students_Count_Results.txt" 
        iresults_on_path = results_on_path / f"{i}on_Max_Students_Count_Results.txt"
        iresults_dp_path = results_dp_path / f"{i}dp_Max_Students_Count_Results.txt"
        
        print(f"Cases max_len = {i}")
        Eval(itest_cases_path,iresults_bk_path,iresults_on_path, iresults_dp_path)
        Check(iresults_bk_path, iresults_on_path, iresults_dp_path)
        print("\n")
        
        i *= 2
    
        
         
    