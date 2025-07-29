import sys
sys.stdin = open("input.txt", "r")

row, col = map(int, input().split())
graph = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
melt_down = []

for _ in range(row):
    graph.append(list(map(int, input().split())))

def dfs(x, y, status):
    water = 0
    for move in range(4):
        nx = dx[move] + x
        ny = dy[move] + y

        if 0 <= nx < row and 0 <= ny < col:
            if graph[nx][ny] == 0:
                water += 1
                
            if graph[nx][ny] > 0:
                dfs(nx, ny, status)
    melt_down.append(water)

print(melt_down)


year = 1
visited = [[False for _ in range(col)] for _ in range(row)] 
for x in range(len(graph)):
    for y in range(len(graph[x])):
        status = dfs(x, y, 1)


