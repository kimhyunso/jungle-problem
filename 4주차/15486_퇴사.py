import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]
# schedule.insert(0, [0, 0])
memo = [0] * (N + 2)

for i in range(1, N + 1):
    time = schedule[i - 1][0]
    price = schedule[i - 1][1]
    
    memo[i] = max(memo[i], memo[i - 1])

    if i + time - 1 <= N:
        memo[time + i] = max(memo[time + i], memo[i] + price)
        
print(memo[N])



