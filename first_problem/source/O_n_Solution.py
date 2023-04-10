from typing import List, Dict, Tuple

def Solve(G : List[int], F : List[int], k : int) -> int:
    """Returns a list of sets of size k that satisfy that:
            *In one set, all students are from the same group
            *All students failed for the same exam P or R

    Args:
        G (List[int]): List where in position i is the set to which integer i belongs
        F (List[int]): List where at position i is 0 if i does not possess a feature and 1 if it does
        k (int): size that sets should be

    Returns:
        int: Maximum number of distinct sets of size k that satisfy the constraints
    """
    
    sol = 0
    
    P_len = F.count(1)
    R_len = len(G) - P_len
    
    sol += P_len // k
    sol += R_len // k
    
    P_rem = P_len % k
    R_rem = R_len % k
    
    if (P_rem + R_rem) < k:
        return sol
    
    feat_by_sets = FeaturesBySets(G, F)
    
    for g in feat_by_sets:
        if min(feat_by_sets[g][0],P_rem) + min(feat_by_sets[g][1], R_rem) >= k:
            sol+=1
            
    return sol   
            

def FeaturesBySets(st_list, failedInP):
    fbs : Dict[int, List[int]] = {}
    
    for i in range(len(st_list)):
        fbs[st_list[i]] = [0,0]
    
    for i in range(len(st_list)):
        if failedInP[i] == 1:
            fbs[st_list[i]][0] += 1
        else:
            fbs[st_list[i]][1] += 1
    
    return fbs
 