import sys
sys.stdin = open("input.txt", "r")

X = input()
Y = input()

# def LCS(X, Y):
#     n, m = len(X), len(Y)
#     if n <= 0 or m <= 0:
#         return 0

#     if X[-1] == Y[-1]:
#         return LCS(X[:n - 1], Y[:m - 1]) + 1
#     else:
#         return max(LCS(X[:n - 1], Y), LCS(X, Y[:m - 1]))

def LCS(X, Y):
    n, m = len(X), len(Y)
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                memo[i+1][j+1] = memo[i][j] + 1
            else:
                memo[i+1][j+1] = max(memo[i][j+1], memo[i+1][j])
    return memo[n][m]

result = LCS(X, Y)
print(result)