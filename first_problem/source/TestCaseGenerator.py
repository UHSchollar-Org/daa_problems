import random as rnd
from typing import List
from pathlib import Path

def Generate(test_cases_count : int, max_elements_count : int, path):
    """Generates test cases 
    Args:
        test_cases_count (int): Amount of test cases that will be generated
        max_elements_count (int): Max lenght of elements list can have
        path (str): Path where the generated cases will be saved
    """
    for _ in range(test_cases_count):
        lenght = rnd.randint(1,max_elements_count)
        groups_count = rnd.randint(1,lenght)
        
        elem_list = []
        features : List[int] = []
        
        feat = 0
        non_feat = 0
        
        for _ in range(lenght):
            elem_list.append(rnd.randint(1,groups_count))
            have_feat = rnd.randint(1,2)
            if have_feat == 1:
                features.append(1)
                feat += 1
            else:
                features.append(0)
                non_feat += 1
                
        k = rnd.randint(1, max(groups_count, feat, non_feat))
        
        Write_File(path,k,elem_list,features)

def Write_File(path, k, elem_list, features):
    with open(path,"a+") as file: 
        file.write("Case\n")
        file.write(f"{k}\n")
        for i in range(len(elem_list)):
            file.write(f"{elem_list[i]} ")
        file.write(f"\n")
        for i in range(len(features)):
            file.write(f"{features[i]} ")
        file.write(f"\n")
        

if __name__ == '__main__':
    path = Path.cwd() / f"first_problem/test_cases"    
    max_elements_count = 2
    while max_elements_count < 1200:
        Generate(10000,max_elements_count, path / f"{max_elements_count}_Max_Students_Count_Cases.txt")
        max_elements_count *= 2

