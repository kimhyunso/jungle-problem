from collections import deque
import sys
input = sys.stdin.readline

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
queue = deque()
count = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited):
    visited[start] = True
    queue.append(start)

    while queue:
        node = queue.popleft()

        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        bfs(graph, i, visited)


print(count)