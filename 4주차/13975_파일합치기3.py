import sys, heapq

sys.stdin = open("input.txt", "r")
T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    total = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        cost = a + b
        total += cost
        heapq.heappush(files, cost)

    print(total)

