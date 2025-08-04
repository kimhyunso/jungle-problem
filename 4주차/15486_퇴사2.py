import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]
memo = [0] * (N + 2)

for i in range(1, N + 1):
    time, price = schedule[i - 1]
    
    memo[i] = max(memo[i], memo[i - 1])

    if i + time - 1 <= N:
        memo[time + i] = max(memo[time + i], memo[i] + price)
        
print(max(memo))



