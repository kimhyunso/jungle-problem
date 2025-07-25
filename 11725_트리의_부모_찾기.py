import sys
sys.stdin = open("input.txt", "r")
sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

# 양방향 표현
for i in range(N - 1):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)

def dfs(graph, start, visited):
    visited[start] = True

    for v in graph[start]:
        if not visited[v]:
            parent[v] = start
            dfs(graph, v, visited)

dfs(graph, 1, visited)

for i in range(2, N + 1):
    print(parent[i])