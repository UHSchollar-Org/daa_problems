from typing import List

def Solve(studentsList : List[int], failedInP : List[int], k : int) -> int:
    """Returns a list of sets of size k that satisfy that:
            *In one set, all students are from the same group
            *All students failed for the same exam P or R

    Args:
        studentsList (List[int]): List where in position i is the group to which student i belongs
        failedInP (List[bool]): List where in position i is True if student i failed P or Flase if not
        k (int): size that sets should be

    Returns:
        int: Maximum number of distinct sets of size k that satisfy the constraints
    """
    
    sets : List[List[int]] = []
    setsCount : int = int(len(studentsList)/k + 2)
    for _ in range(setsCount):
        sets.append([])
    student : int = 0
    
    return Backtrack(student, studentsList, failedInP, k, sets)

def Backtrack(student, studentsList : List[int], failedInP : List[int], k : int, sets: List[List[int]]):
    if student == len(studentsList):
        return KGroupsCount(sets, k)
    
    maxKGroup : int = 0
    
    for i in range(len(sets)):
        if len(sets[i]) == k:
            continue
        if Insert(sets[i], studentsList, failedInP, k, student):
            maxKGroup = max(maxKGroup,Backtrack(student+1, studentsList, failedInP, k, sets))
            sets[i].remove(student)
            if(maxKGroup==len(studentsList)/k):
                break
            
    return maxKGroup
    
def KGroupsCount(sets, k):
    result = 0
    for set in sets:
        if len(set)==k:
            result+=1
    return result

def Insert(set : List[int], studentsList, failedInP, k, student : int):
    if len(set)== 0:
        set.append(student)
        return True
    if  len(set) < k and (studentsList[student] == studentsList[set[0]] or 
                          failedInP[student] == failedInP[set[0]]):
        set.append(student)
        return True
    return False