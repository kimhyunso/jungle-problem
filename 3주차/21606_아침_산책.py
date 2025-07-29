import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)

N = int(input())
places = list(list(map(int, input())))
places.insert(0, 0)
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = 0

for _ in range(N - 1):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)

for u in range(1, N + 1):
    for v in graph[u]:
        if u < v:  # 중복 방지
            if places[u] == 1 and places[v] == 1:
                result += 2

def dfs(start, visited):
    count = 0
    visited[start] = True

    for node in graph[start]:
        if places[node] == 1:
            count += 1
        elif not visited[node]:
            count += dfs(node, visited)
    return count

for i in range(1, N + 1):
    if places[i] == 0 and not visited[i]:
        temp = dfs(i, visited)
        result += temp * (temp - 1)

print(result) 


