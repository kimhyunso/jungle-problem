import sys
from heapq import heappush, heappop

sys.stdin = open("input.txt", "r") 
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    command = int(input())
    if command == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-command, command))
