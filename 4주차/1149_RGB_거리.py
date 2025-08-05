import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dp = [[0] * 3 for _ in range(N)]
houses = [list(map(int, input().split())) for _ in range(N)]

for i in range(3):
    dp[0][i] = houses[0][i]


for j in range(1, N):
    for i in range(3):
        dp[j][i] = min(dp[j-1][x] for x in range(3) if x != i) + houses[j][i]

print(min(dp[N - 1]))