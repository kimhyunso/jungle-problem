import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
queue = deque()

for _ in range(M):
    vetex, edge = map(int, input().split())
    graph[vetex].append(edge)
    in_degree[edge] += 1 # 간선의 진입차수를 증가시킨다.

def solve_kahn():
    sorted_result = []

    # 진입차수가 0인 모든 노드를 queue에 삽입한다.
    for i in range(1, N + 1): 
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        sorted_result.append(node)
        
        for v in graph[node]:
            in_degree[v] -= 1
            if in_degree[v] <= 0:
                queue.append(v)
    return sorted_result

print(*solve_kahn())
