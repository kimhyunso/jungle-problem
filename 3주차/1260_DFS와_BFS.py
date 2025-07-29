import sys
import copy
from collections import deque
sys.stdin = open("input.txt", "r")

queue = deque()

N, M, V  = map(int, input().split())
dfs_graph = [[] for _ in range(N + 1)]
dfs_visited = [False] * (N + 1)

for i in range(M):
    to, value = map(int, input().split())
    dfs_graph[to].append(value)
    dfs_graph[value].append(to)

for nodes in dfs_graph:
    nodes.sort()

bfs_graph = copy.deepcopy(dfs_graph)
bfs_visited = copy.deepcopy(dfs_visited)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(dfs_graph, V, dfs_visited)
print()
bfs(bfs_graph, V, bfs_visited)


