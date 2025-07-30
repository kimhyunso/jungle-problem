import sys
from collections import deque

sys.stdin = open("input.txt", "r")
R, C = map(int, input().split())
maps = []
visited = [[False for _ in range(C)] for _ in range(R)] 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

water_q = deque()
hed_q = deque()

for _ in range(R):
    maps.append(list(input()))

for y in range(R):
    for x in range(C):
        if maps[y][x] == 'S':
            hed_q.append((y, x, 0)) # x, y, time
            visited[y][x] = True
        elif maps[y][x] == '*':
            water_q.append((y, x))

def bfs():
    while hed_q:
        for _ in range(len(water_q)):
            y, x = water_q.popleft()

            for m in range(4):
                mx = dx[m] + x
                my = dy[m] + y

                if 0 <= mx < C and 0 <= my < R and maps[my][mx] == '.':
                    maps[my][mx] = '*'
                    water_q.append((my, mx))

        for _ in range(len(hed_q)):
            y, x, time = hed_q.popleft()

            for m in range(4):
                mx = dx[m] + x
                my = dy[m] + y
                if 0 <= mx < C and 0 <= my < R:
                    if maps[my][mx] == 'D':
                        return time + 1
                    if maps[my][mx] == '.' and not visited[my][mx]:
                        visited[my][mx] = True
                        hed_q.append((my, mx, time + 1))
    return 'KAKTUS'

print(bfs())