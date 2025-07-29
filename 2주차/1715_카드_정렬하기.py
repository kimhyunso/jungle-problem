import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

heap = []
temps = []

N = int(input())
for _ in range(N):
    x = int(input())
    heappush(heap, (x, x))

while len(heap) > 1:
    x = heappop(heap)[1]
    y = heappop(heap)[1]

    result = x + y
    temps.append(result)
    heappush(heap, (result, result))

print(sum(temps))