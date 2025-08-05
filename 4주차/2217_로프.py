import sys
sys.stdin = open("input.txt", "r")

N = int(input())
weights = []

for _ in range(N):
    weights.append(int(input()))

weights.sort(reverse=True)
max_value = weights[0] * 1

for i in range(1, N):
    value = weights[i] * (i + 1)
    if max_value < value:
        max_value = value

print(max_value)