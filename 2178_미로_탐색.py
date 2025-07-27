from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
que = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maps = []
count = 0

for _ in range(N):
    maps.append(list(map(int, input())))

def bfs(x, y):
    que.append((x, y))

    while que:
        tx, ty = que.popleft()
        for i in range(4):
            nx = tx + dx[i] 
            ny = ty + dy[i]
            
            if  0 <= nx < N and 0 <= ny < M  and maps[nx][ny] == 1:
                maps[nx][ny] = maps[tx][ty] + 1
                que.append((nx, ny))

bfs(0, 0)
print(maps[N - 1][M - 1])