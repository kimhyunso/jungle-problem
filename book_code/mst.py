## 최소 신장 트리
## 크루스칼 알고리즘
import sys
sys.stdin = open("input.txt", "r")

vetex, edge = map(int, input().split())
parent = [0] * (vetex + 1)

for i in range(1, vetex + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

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

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)