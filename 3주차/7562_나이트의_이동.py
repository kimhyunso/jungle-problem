import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

result = []
dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]

def bfs(start_x, start_y, end_x, end_y, visited):
    que = deque()
    visited[start_x][start_y] = True
    que.append((start_x, start_y, 0))

    while que:
        x, y, cnt = que.popleft()
        if x == end_x and y == end_y:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))
    return -1

for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[False for _ in range(N)] for _ in range(N)]
    print(bfs(start_x, start_y, end_x, end_y, visited))

