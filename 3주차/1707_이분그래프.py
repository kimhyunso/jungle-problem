from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

sys.stdin = open("input.txt", "r")
T = int(input())
que = deque()

def dfs(graph, colors, start, visited):
        visited[start] = True

        for v in graph[start]:
            if not visited[v]:
                colors[v] = 1 - colors[start]
                if not dfs(graph, colors, v, visited):
                    return False
            else:
                if colors[v] == colors[start]:
                    return False
        return True


for _ in range(T):
    vertex_cnt, edge_cnt = map(int, input().split())
    graph = [[] for _ in range(vertex_cnt + 1)]
    visited = [False] * (vertex_cnt + 1)
    colors = [-1] * (vertex_cnt + 1)

    for i in range(edge_cnt):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    is_checked = True
    for i in range(1, vertex_cnt + 1):
        if not visited[i]:
            colors[i] = 0
            if not dfs(graph, colors, i, visited):
                is_checked = False
                break
    print(colors)

    print('YES' if is_checked else 'NO')















