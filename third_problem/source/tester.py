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

def validate(method1, method2):
    path = Path.cwd()
    results_path = path / "third_problem" / "source" / "results"
    method1_path = results_path / "values_results" / f"{type(method1).__name__}_values_results.json"
    method2_path = results_path / "values_results" / f"{type(method2).__name__}_values_results.json"
    
    method1_results = load_json(method1_path)
    method2_results = load_json(method2_path)

    for n in method1_results:
        if n not in method2_results:
            break
        for m in n:
            if m not in method2_results[n]:
                break
            method1_values = method1_results[n][m]
            method2_values = method2_results[n][m]
            
            if len(method1_values) != len(method2_values):
                raise Exception(f"For {n},{m} there are diferent values count between method1 and method2")
            validate_values(method1_values, method2_values)
    print("Valid methods values")

def validate_values(method1_values, method2_values):
    for i in range(len(method1_values)-1):
        if type(method1_values[i]) != type(method2_values[i]):
            raise Exception(f"Results in case {i} not equals")

def load_json(json_path):
    data = {}
    
    with open(json_path, "r") as file:
        data = json.load(file)
    
    return data