import sys

input = sys.stdin.readline

# 파스칼의 삼각형

N, K = map(int, input().split())

dp = [[1]*(N+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[N][K])
