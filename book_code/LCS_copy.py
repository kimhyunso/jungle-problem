import sys
sys.stdin = open("input.txt", "r")

X = input()
Y = input()
m, n = len(X), len(Y)
dp = [[0] * (n+1) for _ in range(m+1)]

# bottom-up 방식
for i in range(m):
    for j in range(n):
        if X[i] == Y[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

# LCS 문자열 추적
def trace_LCS(X, Y):
    i, j = len(X), len(Y)
    lcs_str = []

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))

result = trace_LCS(X, Y)
print(dp[m][n])
print(result)
