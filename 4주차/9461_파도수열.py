import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)
    dp[1] = 1

    if N >= 2:
        dp[2] = 1
    if N >= 3:
        dp[3] = 1

    for i in range(4, N + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[N])

