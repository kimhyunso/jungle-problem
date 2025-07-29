import heapq
import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)

n = int(input())
maps = []
distarnce = [[INF] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    temp = []
    lines = input()
    for line in lines:
        temp.append(int(line))
    maps.append(temp)

def make_miro(x, y):
    que = []
    heapq.heappush(que, (0, x, y))
    distarnce[x][y] = 0

    while que:
        cost, nx, ny = heapq.heappop(que)

        if distarnce[nx][ny] < cost:
            continue

        for i in range(4):
            mx = dx[i] + nx
            my = dy[i] + ny

            if 0 <= mx < n and 0 <= my < n:
                d_cost = cost + (1 if maps[mx][my] == 0 else 0)
                if d_cost < distarnce[mx][my]:
                    distarnce[mx][my] = d_cost
                    heapq.heappush(que, (d_cost, mx, my)) 

make_miro(0 ,0)

print(distarnce[n - 1][n - 1])