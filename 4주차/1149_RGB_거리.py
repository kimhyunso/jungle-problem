import sys
sys.stdin = open("input.txt", "r")

N = int(input())

dp = [[0] * N for _ in range(N)]
houses = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    dp[0][i] = houses[0][i]

for i in range(1, N):
    for j in range(N):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j]) + houses[i][j]
        # dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + houses[i][0]
        # dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + houses[i][1]
        # dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + houses[i][2]


print(min(dp[N - 1]))



