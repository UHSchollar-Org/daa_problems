from typing import List

def Solve(G : List[int], F : List[int], k : int) -> int:
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
    setsCount : int = int(len(G)//k + 1)
    
    if (len(G) % k) != 0:
        setsCount += 1
    
    for _ in range(setsCount):
        sets.append([])
    
    student : int = 0
    
    return Backtrack(student, G, F, k, sets)

def Backtrack(element, G : List[int], F : List[int], k : int, sets: List[List[int]]):
    if element == len(G):
        return KGroupsCount(sets, k)
    
    maxKGroup : int = 0
    
    for i in range(len(sets)):
        if len(sets[i]) == k:
            continue
        
        if Insert(sets[i], G, F, k, element):
            maxKGroup = max(maxKGroup,Backtrack(element+1, G, F, k, sets))
            sets[i].remove(element)
            
            if(maxKGroup==len(G)/k):
                break
            
    return maxKGroup
    
def KGroupsCount(sets, k):
    result = 0
    for set in sets:
        if len(set)==k:
            result+=1
    return result


def Insert(set : List[int], G, F, k, element : int):
    if len(set)== 0:
        set.append(element)
        return True
    
    if  len(set) < k:
        same_group = True
        
        for i in range(len(set)):
            if G[element] != G[set[i]]:
                same_group = False
                break
            
            
        if same_group:
            set.append(element)
            return True
        
        same_test_failed = True
        
        for i in range(len(set)):
            if F[element] != F[set[i]]:
                same_test_failed = False
                break
            
        if same_test_failed:
            set.append(element)
            return True
        
    return False