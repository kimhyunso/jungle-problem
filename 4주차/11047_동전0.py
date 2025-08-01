import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

result = 0
for coin in coins:
    if K <= 0:
        break

    result += K // coin
    K %= coin

print(result)