from collections import deque
import sys

sys.stdin = open("input.txt", "r")
T = int(input())
que = deque()

for _ in range(T):
    vertex_cnt, edge_cnt = map(int, input().split())
    graph = [[] for _ in range(vertex_cnt + 1)]
    visited = [False] * (vertex_cnt + 1)
    colors = [0] * (vertex_cnt + 1)

    for i in range(edge_cnt):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(graph, start, visited, color):
        visited[start] = True
        
        for v in visited[start]:
            if not visited[start]:
                dfs(graph, v, visited, color)
            












