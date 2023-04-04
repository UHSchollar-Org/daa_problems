from typing import List

    
def Solve(n :int, k : int, a : List[int], b : List[int]):
    
    totA = 0
    totB = 0
    for i in range(n):
        totA += a[i]
        totB += b[i]
    
    dp = []
    for i in range(n+1):
        dp.append([False] * (k))
    dp[0][0] = True

    for i in range(1,n+1):
        for j in range(k):
            dp[i][j] = dp[i-1][(j-a[i]%k)%k]
            for x in range(min(k-1,a[i])+1):
                if (a[i]-x)%k + b[i] >= k:
                    dp[i][j] = dp[i][j] or dp[i-1][(j-x)%k]

    result = 0
    for i in range(k):
        if dp[n][i]:
            result = max(result,(totA+totB-i)//k)

    return result