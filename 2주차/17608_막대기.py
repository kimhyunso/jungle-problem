import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

heights = []
for _ in range(N):
    heights.append(int(input()))

last = heights.pop()
count = 1

while heights:
    compara_num = heights.pop()
    if last < compara_num:
        count += 1
        last = compara_num
print(count)
