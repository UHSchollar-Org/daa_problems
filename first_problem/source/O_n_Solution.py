from typing import List, Dict, Tuple

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
    
    result = 0
    
    failedInP_count = TrueCount(failedInP)
    failedInR_count = len(studentsList) - failedInP_count
    
    result += failedInP_count // k
    result += failedInR_count // k
    
    failedInP_to_locate = failedInP_count % k
    failedInR_to_locate = failedInR_count % k
    
    if (failedInP_to_locate + failedInR_to_locate) < k:
        return result
    
    fails_by_groups : Dict[int, Tuple[int, int]] = FailsByGroups(studentsList, failedInP, failedInR)
    
    for g in fails_by_groups:
        if fails_by_groups[g][0] >= failedInP_to_locate and fails_by_groups[g][1] >= failedInR_to_locate:
            result += 1
            return result
        elif fails_by_groups[g][0] >= failedInP_to_locate and fails_by_groups[g][1] < failedInR_to_locate:
            if failedInP_to_locate + fails_by_groups[g][1] >= k:
                result += 1
        else:
            #fails_by_groups[g][0] < failedInP_to_locate and fails_by_groups[g][1] >= failedInR_to_locate:
            pass
    
    return result   
            

def FailsByGroups(st_list, failedInP, failedInR):
    fbg : Dict[int, Tuple[int, int]] = {}
    
    for i in range(len(st_list)):
        fbg[st_list[i]] = (0,0)
    
    for i in range(len(st_list)):
        if failedInP[i]:
            fbg[st_list[i]][0] += 1
        else:
            fbg[st_list[i]][1] += 1
                    
    
def TrueCount(list : List[bool]):
    result = 0
    for item in list:
        if item == True:
            result+=1
    return result

gl = [1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 3]
p = [True, True, False, False, False, True, False, False, False, False, False]
r = [False, False, True, True, True, False, True, True, True, True, True] 

a = Solve(gl, p, r, 3)

print(a)
 