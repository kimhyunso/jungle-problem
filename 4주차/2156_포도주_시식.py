import sys
sys.stdin = open("input.txt", "r")
n = int(input())

grape_glass = [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

dp[1] = grape_glass[0]
if n >= 2:
    dp[2] = dp[1] + grape_glass[1]


for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],
        dp[i - 3] + grape_glass[i - 2] + grape_glass[i - 1],
        dp[i - 2] + grape_glass[i - 1]
    )
    
print(max(dp))

