# # top-down 방식 - 재귀

def LCS(X, Y):
    m, n = len(X), len(Y)
    if m == 0 or n == 0:
        return 0
    else:
        if X[-1] == Y[-1]:
            return LCS(X[:m - 1], Y[:n - 1]) + 1
        else:
            return max(LCS(X, Y[:n-1]), LCS(X[:m-1], Y))

X = input()
Y = input()
# X = 'ABCBDAB'
# Y = 'BDCAB'
m, n = len(X), len(Y)
dp = [[0] * (n+1) for _ in range(m+1)]

# bottom-up 방식 - dp
# def LCS_DP(X, Y):
#     for i in range(m):
#         for j in range(n):
#             if X[i] == Y[j]:
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:
#                 dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
#     return dp[m][n]

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

length = LCS(X, Y)
result = trace_LCS(X, Y)
print(length)
print(result)