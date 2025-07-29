from collections import deque

n, k = map(int, input().split())
que = deque()
visited = [False] * (n + 1)
graph = []

coins = []
for _ in range(n):
    coins.append(int(input()))



def bfs(start):
    visited[start] = True
    que.append(start)

    while que:
        node = que.popleft()
        for v in graph[node]:
            if not visited[v]:
                pass




