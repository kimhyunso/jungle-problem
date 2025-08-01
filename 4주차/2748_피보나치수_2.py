N = int(input())

memo = [0] * (N + 1)

memo[0] = 0
memo[1] = 1
a, b = 0, 1
for i in range(2, N + 1):
    # memo[i] = memo[i - 1] + memo[i - 2]
    a, b = b, a+b

# print(memo[N])

print(b)


