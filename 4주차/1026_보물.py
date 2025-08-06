import sys
sys.stdin = open("input.txt", "r")

N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

result = 0
for i in range(N):
    result += a[i] * b[i]

print(result)