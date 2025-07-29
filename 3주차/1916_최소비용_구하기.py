import sys
sys.stdin = open("input.txt", "r")
# INF = int(1e9)

# city_cnt = int(input())
# bus_cnt = int(input())
# visited = [False] * (city_cnt + 1)
# graph = [[] for _ in range(city_cnt + 1)]
# distance = [INF] * (city_cnt + 1)

# for _ in range(bus_cnt):
#     vetex, edge, cost = map(int, input().split())
#     graph[vetex].append((edge, cost))

# start, end = map(int, input().split())

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, city_cnt + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for v in graph[start]:
#         distance[v[0]] = min(distance[v[0]], v[1])

#     for _ in range(city_cnt - 1):
#         now = get_smallest_node()
#         visited[now] = True

#         for node in graph[now]:
#             cost = distance[now] + node[1]
#             if cost < distance[node[0]]:
#                 distance[node[0]] = cost

# dijkstra(start)

# print(distance[end])

# 우선순위 큐 형식으로 구현
import heapq
INF = int(1e9)

city_cnt = int(input())
bus_cnt = int(input())
graph = [[] for _ in range(city_cnt + 1)]
distarnce = [INF] * (city_cnt + 1)
for _ in range(bus_cnt):
    vertex, edge, cost = map(int, input().split())
    graph[vertex].append((edge, cost))
start, end = map(int, input().split())

print(graph)

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start)) # cost, node
    while que:
        dist, now = heapq.heappop(que)
        if distarnce[now] < dist:
            continue
            
        for v in graph[now]:
            cost = dist + v[1]
            if cost < distarnce[v[0]]:
                heapq.heappush(que, (cost, v[0]))
                distarnce[v[0]] = cost
                
dijkstra(start)
# print(distarnce[end])










