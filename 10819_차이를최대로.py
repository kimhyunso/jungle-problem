import itertools

N = int(input())
arr = list(map(int, input().split()))

max_value = 0

for perm in itertools.permutations(arr, N):
    sum_number = 0
    for i in range(N - 1):
        sum_number += abs(perm[i] - perm[i + 1])
    max_value = max(max_value, sum_number)

print(max_value)
