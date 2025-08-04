import sys
sys.stdin = open("input.txt", "r")

N = int(input())

memo = [0] * (N + 1)
steps = []
for _ in range(N):
    steps.append(int(input()))

memo[1] = steps[0]
if N >= 2:
    memo[2] = memo[1] + steps[1]

for i in range(3,  N + 1):
    memo[i] = max(
        memo[i - 2],
        memo[i - 3] + steps[i - 2]
    ) + steps[i - 1]

print(memo[N])

    

