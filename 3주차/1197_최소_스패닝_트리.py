import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)

V, E = map(int, input().split())
graph = []
parent = [0] * (V + 1)

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    vertex, edge, cost = map(int, input().split())
    graph.append((cost, vertex, edge))

graph.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for edge in graph:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)