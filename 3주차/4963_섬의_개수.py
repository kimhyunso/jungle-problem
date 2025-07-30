import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def make_maps():
    maps = []
    for y in range(h):
        maps.append(list(map(int, input().split())))
    return maps

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(width, height, x, y, visited, maps):
    visited[y][x] = True

    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
            if maps[ny][nx] == 1:
                dfs(width, height, nx, ny, visited, maps)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    maps = make_maps()
    visited = [[False for _ in range(w)] for _ in range(h)]
    count = 0

    for y in range(h):
        for x in range(w):
            if not visited[y][x] and maps[y][x] == 1:
                dfs(w, h, x, y, visited, maps)
                count += 1

    print(count)

