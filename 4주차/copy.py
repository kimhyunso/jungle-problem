import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = i번째부터 j번째까지 곱할 때 최소 연산 횟수
dp = [[0] * n for _ in range(n)]

for length in range(1, n):  # 구간 길이
    for start in range(n - length):
        end = start + length    
        dp[start][end] = float('inf') 

        for k in range(start, end):
            cost = (
                dp[start][k] + dp[k + 1][end] +
                matrix[start][0] * matrix[k][1] * matrix[end][1]
            )
            dp[start][end] = min(dp[start][end], cost)

print(dp[0][n - 1])
