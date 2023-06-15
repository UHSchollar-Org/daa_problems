import os
import time
import json
from pathlib import Path

def test(method, test_cases_path, results_path):
    tests = os.listdir(test_cases_path)
    tests.sort(key=lambda case: int(case.split('_')[0]) + int(case.split('_')[0]))
    method_results = {}
    method_times = {}
    method_name = type(method).__name__
    for test in tests:
        with open(test_cases_path/test, 'r') as file:
            cases = file.read().split("Case")[1:]
            case_number = 0
            
            n = int(test.split("_")[0])
            m = int(test.split("_")[1])
            print(n,m)
            time.sleep(5)
            
            try:
                method_results[n][m] = []
                method_times[n][m] = []
            except:
                method_results[n] = {m : []}
                method_times[n] = {m : []}
            
            for raw_case in cases:
                case = raw_case.split("\n")[1:-1]
                
                str_time = time.time()
                result = method.Solve(n,m,case)
                end_time = time.time()
                case_time = end_time - str_time
                
                method_times[n][m].append(case_time)
                method_results[n][m].append(result)
            
            with open(results_path/"time_results"/f"{method_name}_time_results.json", "w") as file:
                json.dump(method_times, file)
            
            with open(results_path/"values_results"/f"{method_name}_values_results.json", "w") as file:
                json.dump(method_results, file)
