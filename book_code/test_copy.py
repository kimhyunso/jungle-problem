import heapq
INF = int(1e9)
N = int(input())

distarnce = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    vertex, edge, cost = map(int, input().split())
    graph[vertex].append((cost, edge))

def test(start):
    distarnce[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, node = heapq.heappop(heap)

        if distarnce[node] < cost:
            continue
        
        for now in graph[node]:
            new_cost = now[0] + cost
            if new_cost < distarnce[now[1]]:
                heapq.heappush(heap, (new_cost, now[1]))
                distarnce[now[1]] = new_cost
