import random as rnd
from typing import List
from pathlib import Path

def Generate(test_cases_count : int, max_students_count : int, path):
    """Generates test cases 
    Args:
        test_cases_count (int): Amount of test cases that will be generated
        max_students_count (int): Max lenght of student list can have
        path (str): Path where the generated cases will be saved
    """
    for _ in range(test_cases_count):
        lenght = rnd.randint(1,max_students_count)
        groups_count = rnd.randint(1,lenght)
        
        student_list = []
        failedInP : List[int] = []
        
        failedInP_count = 0
        failedInR_count = 0
        
        for _ in range(lenght):
            student_list.append(rnd.randint(1,groups_count))
            curse_failed = rnd.randint(1,2)
            if curse_failed == 1:
                failedInP.append(1)
                failedInP_count += 1
            else:
                failedInP.append(0)
                failedInR_count += 1
                
        k = rnd.randint(1, max(groups_count, failedInP_count, failedInR_count))
        
        Write_File(path,k,student_list,failedInP)

def Write_File(path, k, student_list, failedInP):
    with open(path,"a+") as file: 
        file.write("Case\n")
        file.write(f"{k}\n")
        for i in range(len(student_list)):
            file.write(f"{student_list[i]} ")
        file.write(f"\n")
        for i in range(len(failedInP)):
            file.write(f"{failedInP[i]} ")
        file.write(f"\n")
        

if __name__ == '__main__':
    path = Path.cwd() / f"first_problem/test_cases"    
    max_students_count = 2
    while max_students_count < 1200:
        Generate(10000,max_students_count, path / f"{max_students_count}_Max_Students_Count_Cases.txt")
        max_students_count *= 2

