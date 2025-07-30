import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
hevy_graph = [[] for _ in range(N + 1)]
light_graph  = [[] for _ in range(N + 1)]

for _ in range(M):
    vertex, edge = map(int, input().split())
    light_graph[vertex].append(edge)
    hevy_graph[edge].append(vertex)

mid = (N + 1) // 2
result = 0

def dfs(graph, visited, node):
    visited[node] = True
    cnt = 1
    for nxt in graph[node]:
        if not visited[nxt]:
            cnt += dfs(graph, visited, nxt)
    return cnt

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    heavy_cnt = dfs(hevy_graph, visited, i) - 1
    if heavy_cnt >= mid:
        result += 1
        continue
    
    visited = [False] * (N + 1)
    light_cnt = dfs(light_graph, visited, i) - 1
    if light_cnt >= mid:
        result += 1

print(result)

