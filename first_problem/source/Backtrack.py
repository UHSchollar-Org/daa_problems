from typing import List

def Solve(studentsList : List[int], failedInP : List[bool], failedInR : List[bool], k : int) -> int:
    """Returns a list of sets of size k that satisfy that:
            *In one set, all students are from the same group
            *All students failed for the same exam P or R

    Args:
        studentsList (List[int]): List where in position i is the group to which student i belongs
        failedInP (List[bool]): List where in position i is True if student i failed P or Flase if not
        failedInR (List[bool]): List where in position i is True if student i failed R or Flase if not
        k (int): size that sets should be

    Returns:
        int: Maximum number of distinct sets of size k that satisfy the constraints
    """
    
    sets : List[List[int]] = []
    setsCount : int = int(len(studentsList)/k + 1)
    if (len(studentsList)%k)!=0:
        setsCount += 1
    for _ in range(setsCount):
        sets.append([])
    student : int = 0
    
    return Backtrack(student, studentsList, failedInP, failedInR, k, sets)

def Backtrack(student, studentsList : List[int], failedInP : List[bool], failedInR : List[bool], k : int, sets: List[List[int]]):
    if student == len(studentsList):
        return KGroupsCount(sets, k)
    
    maxKGroup : int = 0
    
    for i in range(len(sets)):
        if len(sets[i]) == k:
            continue
        if Insert(sets[i], studentsList, failedInP, failedInR, k, student):
            maxKGroup = max(maxKGroup,Backtrack(student+1, studentsList, failedInP, failedInR, k, sets))
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


def Insert(set : List[int], studentsList, failedInP, failedInR, k, student : int):
    if len(set)== 0:
        set.append(student)
        return True
    if  len(set) < k:
        same_group = True
        for i in range(len(set)):
            if studentsList[student]!=studentsList[set[i]]:
                same_group = False
                break
        if same_group:
            set.append(student)
            return True
        same_test_failed = True
        for i in range(len(set)):
            if failedInP[student] != failedInP[set[i]]:
                same_test_failed = False
                break
        if same_test_failed:
            set.append(student)
            return True
    return False