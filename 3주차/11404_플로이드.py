import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    vertex, edge, cost = map(int, input().split())
    graph[vertex][edge] = min(graph[vertex][edge], cost)

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            graph[x][y] = 0

for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


for x in range(1, N + 1):
    for y in range(1, N + 1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()
