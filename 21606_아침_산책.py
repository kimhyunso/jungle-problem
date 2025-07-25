import sys

sys.stdin = open("input.txt", "r")

N = int(input())
place = list(map(int, input()))
place.insert(0, 0)

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(N - 1):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)
    if place[vertex] == 1 and place[edge] == 1:
        count += 1

def dfs(graph, start, visited):
    visited[start] = True
    n = 0
    for v in graph[start]:
        if not visited[v]:
            if place[v] == 1:
                n += 1
            elif place[v] == 0:
                n += dfs(graph, v, visited)
    return n
    

for i in range(1, N + 1):
    if not visited[i] and place[i] == 0:
        n = dfs(graph, i, visited)
        count += n * (n - 1) // 2

print(count)





