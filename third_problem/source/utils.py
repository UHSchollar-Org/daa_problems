import matplotlib.pyplot as plt
import json
from pathlib import Path
from statistics import mean
import numpy as np
from typing import List



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

def draw_results(methods_names, times_path):
    """Function that draws the results of the time of execution of the methods

    Args:
        methods_names (list): List of the names of the methods
        times_path (Path): Path to the folder with the time results
    """
    #Loading the data
    methods_time_results = []
    for i in range(len(methods_names)):
        time_results = {}
        with open(times_path / f"{methods_names[i]}_time_results.json", "r") as file:
            time_results = json.load(file)
        methods_time_results.append(time_results)
    
    index = np.argmin([len(methods_time_results[i].keys()) for i in range(len(methods_time_results))])
    n_values = methods_time_results[index].keys()
    #fig_rows = min([len(methods_time_results[i].keys()) for i in range(len(methods_time_results))])

    fig, axs = plt.subplots(len(n_values), len(methods_names), figsize=(12,7))
    for ax in axs.flatten():
        ax.grid(True)
        ax.set_xlabel("Clauses Count")
        ax.set_ylabel("Time")
    fig.suptitle(f"Time Results", fontsize=16)
    for i, n in enumerate(n_values):
        for j in range(len(methods_names)):
            plt.sca(axs[i,j])
            draw_graphic(methods_time_results[j],methods_names[j], n)
            plt.tight_layout()
        
    for ax in axs.flatten():
        ax.legend()
    plt.show()

def draw_graphic(time_results, method_name, n):
    """Function that draws a graphic with the time results for a given method and n

    Args:
        time_results (dicc): Dictionary of time results for each m
        method_name (str): Name of the method
        n (int): Number of variables
    """
    mean_vals = []
    std_vals = []
    min_vals = []
    max_vals = []
    
    #Sorting the results by m
    m_values = []
    for m in time_results[n]:
        m_values.append(m)
    m_values.sort(key = lambda x: int(x))
    
    #Getting the values for the graphic
    for m in m_values:
        results = [float(x) for x in time_results[n][m]]
        mean_vals.append(mean(results))
        std_vals.append(np.std(list(results)))
        min_vals.append(min(results))
        max_vals.append(max(results))
    
    #Drawing the graphic
    plt.plot(
        m_values,
        max_vals,
        "--",
        label="Time max",
        alpha=0.5,
    )
    plt.plot(m_values, mean_vals, label=f"Avg. Time",)
    plt.plot(m_values,min_vals,"--",label=f"Time min",alpha=0.5,)
    plt.grid()
    plt.xlabel("Clauses Count")
    plt.ylabel("Time")
    plt.title(f"{method_name} times for n = {n}")
    plt.legend(loc="best")

path = Path.cwd()
time_results_path = path / "third_problem" / "source" /"results" / "time_results"
values_results_path = path / "third_problem" / "source" / "results" / "values_results"
draw_results(["Exhaustive_Enumeration","DPLL"], time_results_path)