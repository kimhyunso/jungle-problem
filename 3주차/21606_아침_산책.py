import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
places = list(input())
places.insert(0, 0)
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
result = [0] * (n+1)

for _ in range(n-1):
    vetex, edge = map(int, input().split())
    graph[vetex].append(edge)
    graph[edge].append(vetex)
    
def dfs(node, start):
    if int(places[node]) == 1:
        result[node] += 1
        result[start] += 1
        return 
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, start)
            visited[next_node] = False

ans = 0
for i in range(1, n+1):
    if int(places[i]) == 1:
        visited[i] = True

        for next_node in graph[i]:
            if int(places[next_node]) == 1:
                if not visited[next_node]:
                    result[next_node] += 1
                    result[i] += 1
            else:
                visited[next_node] = True
                dfs(next_node, i)
                visited[next_node] = False

print(sum(result))