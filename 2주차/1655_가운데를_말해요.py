import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt", "r")

N = int(input())
left = []
right = []

for i in range(N):
    x = int(input())
    heappush(left, -x)

    if right and -left[0] > right[0]:
        val = -heappop(left)
        heappush(right, val)
        heappush(left, -heappop(right))
    
    if len(left) > len(right) + 1:
        heappush(right, -heappop(left))
    print(-left[0])