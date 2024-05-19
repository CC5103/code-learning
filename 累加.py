# import pandas as pd

N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
INF = 10**18
dp = [[-INF] * N for _ in range(M)] #!  初始化要为无限小
dp[0][0] = A[0]

for i in range(0, M):
    for j in range(i, N-M+i+1):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = max(dp[i][j-1], A[j])
            continue
        dp[i][j] = max(dp[i-1][j-1]+A[j]*(i+1), dp[i][j-1])

print(max(dp[M-1]))

# dp = pd.DataFrame(dp)
# print(dp)