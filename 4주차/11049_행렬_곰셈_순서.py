import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dp = [[0] * N for _ in range(N)]
matrix = [list(map(int, input().split())) for _ in range(N)]

for length in range(1, N):  # 부분 행렬 개수
    for i in range(N - length): # 시작 인덱스
        j = i + length # 끝 인덱스
        dp[i][j] = float('inf')
        for k in range(i, j): # 괄호 자르기 위치
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp)