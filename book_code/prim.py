## mst 알고리즘
## 프림 알고리즘
import sys
import heapq
sys.stdin = open("input.txt", "r")
sys.stdin.readline

def prim(x):
    visited[x] = True
    route = [x]
    heap = graph[x]
    heapq.heapify(heap)
    res = 0 # 가중치

    while heap:
        weight, w = heapq.heappop(heap)
        if visited[w] == False:
            visited[w] = True
            route.append(w)
            res += weight
            for edge in graph[w]:
                if visited[edge[1]] == False:
                    heapq.heappush(heap, edge)
    return route, res

vetex_cnt, edge_cnt = map(int, input().split())
graph = [[] for _ in range(vetex_cnt + 1)]
visited = [False] * (vetex_cnt + 1)

for _ in range(edge_cnt):
    vetex, edge, weight = map(int, input().split())

    graph[vetex].append([weight, edge])
    graph[edge].append([weight, vetex])

print(prim(1))


