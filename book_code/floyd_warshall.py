import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)
node_cnt = int(input())
edge_cnt = int(input())

graph = [[INF] * (node_cnt + 1) for _ in range(node_cnt + 1)]

for x in range(1, node_cnt + 1):
    for y in range(1, node_cnt + 1):
        if x == y:
            graph[x][y] = 0

for _ in range(edge_cnt):
    vetex, edge, cost = map(int, input().split())
    graph[vetex][edge] = cost

for k in range(1, node_cnt + 1):
    for x in range(1, node_cnt + 1):
        for y in range(1, node_cnt + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, node_cnt + 1):
    for y in range(1, node_cnt + 1):
        print(graph[x][y], end=' ')
    print()