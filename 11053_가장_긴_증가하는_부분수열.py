import sys
sys.stdin = open("input.txt", "r") 

N = int(input())
numbers = list(map(int, input().split()))
log_numbers = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            log_numbers[i] = max(log_numbers[i], log_numbers[j] + 1)

print(max(log_numbers))