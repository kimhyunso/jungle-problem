import sys
from collections import deque
sys.stdin = open("input.txt", "r")

toy = int(input())
relation = int(input())
in_degree = [0] * (relation + 1)
graph = [[] for _ in range(toy + 1)]
queue = deque()
result = [0] * (toy + 1)

for _ in range(relation):
    part, part_num, cnt = map(int, input().split())
    graph[part].append(part_num)
    in_degree[part] += cnt

def kan_sort():
    for node in range(1, relation + 1):
        if in_degree[node] != 0:
            queue.append(node)

    count = 0

    while queue:
        node = queue.popleft()

        for v in graph[node]:
            in_degree[v] -= 1
            count += 1
            if in_degree[v] <= 0:
                queue.append(node)
                result[node] = count

kan_sort()

print(result)