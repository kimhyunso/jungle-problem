import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
que = deque()
visited = [-1] * (k + 1)

coins = []
for _ in range(n):
    coins.append(int(input()))

visited[0] = 0

def bfs():
    que.append(0)
    while que:
        current = que.popleft()

        for coin in coins:
            next_value = current + coin
            if next_value > k:
                continue
            if visited[next_value] == -1:  # 아직 방문하지 않은 금액이면
                visited[next_value] = visited[current] + 1
                que.append(next_value)

bfs()
print(visited[-1])

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

INF = int(1e9)
dp = [INF] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != INF else -1)