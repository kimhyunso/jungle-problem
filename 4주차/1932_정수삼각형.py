import sys
sys.stdin = open("input.txt", "r")

N = int(input())

dp = [[0] * N for _ in range(N)]
tri = [list(map(int, input().split())) for _ in range(N)]

dp[0][0] = tri[0][0]
if N >= 2:
    dp[1][0] = tri[1][0] + dp[0][0]
    dp[1][1] = tri[1][1] + dp[0][0]

for i in range(2, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]    
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[N - 1]))