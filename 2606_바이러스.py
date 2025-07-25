from collections import deque
import sys
sys.stdin = open("input.txt", "r")

computer_cnt = int(input())
edge_cnt = int(input())
graph = [[] for _ in range(computer_cnt + 1)]
queue = deque()
visited = [False] * (computer_cnt + 1)
count = 0

for i in range(edge_cnt):
    vetex, edge = map(int, input().split())
    graph[edge].append(vetex)
    graph[vetex].append(edge)

def bfs(graph, start, visited):
    global count
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()

        for v in graph[node]:
            if not visited[v]:
                count += 1
                visited[v] = True
                queue.append(v)


bfs(graph, 1, visited)

print(count)