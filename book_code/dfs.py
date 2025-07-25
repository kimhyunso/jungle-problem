visited = [False] * 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)