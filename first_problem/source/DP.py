from typing import List
from O_n_Solution import FeaturesBySets

def count_feat(fbs: dict):
    a = [0]*(len(fbs.keys()) + 1)
    b = [0]*(len(fbs.keys()) + 1)
    
    for i,g in enumerate(fbs.keys()):
        a[i+1] = fbs[g][0]
        b[i+1] = fbs[g][1]
    
    return a, b
    
def Solve(G: List[int], F: List[int], k: int) -> int:
    
    fbs = FeaturesBySets(G, F)
    
    n = fbs.keys().__len__()
    a, b = count_feat(fbs)
    
    totA = 0
    totB = 0
    for i in range(n+1):
        totA += a[i]
        totB += b[i]
    
    dp = []
    for i in range(n+1):
        dp.append([False] * (k))
    
    dp[0][0] = True
    for i in range(1,n+1):
        for j in range(k):
            dp[i][j] = dp[i-1][(j-a[i]%k+k)%k]
            for x in range(min(k-1,a[i])+1):
                if (a[i]-x)%k + b[i] >= k:
                    dp[i][j] = dp[i][j] or dp[i-1][(j-x+k)%k]

    result = 0
    for i in range(k):
        if dp[n][i]:
            result = max(result,(totA+totB-i)//k)

    return result