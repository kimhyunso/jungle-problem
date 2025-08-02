import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    coin_type = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    memo = [0] * (target + 1)
    memo[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            memo[i] += memo[i - coin]
    
    print(memo[target])
