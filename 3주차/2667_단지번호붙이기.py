from collections import deque
import sys

sys.stdin = open("input.txt", "r")
N = int(input())
maps = []
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
house_cnt = []

que = deque()
for _ in range(N):
    maps.append(list(map(int, input())))

def bfs(x, y):
    visited[x][y] = True
    que.append((x, y))
    count = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    count += 1
    return count


for y in range(N):
    for x in range(N):
        if not visited[x][y] and maps[x][y]:
            house_cnt.append(bfs(x, y))


print(len(house_cnt))
house_cnt.sort()
for house in house_cnt:
    print(house)