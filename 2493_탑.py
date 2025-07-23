import sys
sys.stdin = open("input.txt", "r")

N = int(input())

tower = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()
        
    if stack:
        result[i] = stack[-1] + 1
    else:
        result[i] = 0
    stack.append(i)

print(result)


