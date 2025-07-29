import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

que = deque()
city_cnt, load_cnt, target_d, start = map(int, input().split())
graph = [[] for _ in range(city_cnt + 1)]
distarnces = [-1] * (city_cnt + 1)
result = []

# 방향 그래프 -> 단방향 처리
for i in range(load_cnt):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)

def bfs(graph, start):
    distarnces[start] = 0
    que.append(start)

    while que:
        node = que.popleft()

        for v in graph[node]:
            if distarnces[v] == -1:
                distarnces[v] = distarnces[node] + 1
                que.append(v)

bfs(graph, start)

if target_d not in distarnces:
    print(-1)
else:
    for i in range(1, len(distarnces)):
        if distarnces[i] == target_d:
            print(i)
