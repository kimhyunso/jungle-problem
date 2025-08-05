import sys
sys.stdin = open("input.txt", "r")

N = int(input())

load = list(map(int, input().split()))
city = list(map(int, input().split()))

result = 0
min_price = city[0]

for i in range(N - 1):
    if city[i] < min_price:
        min_price = city[i]
    result += min_price * load[i]

print(result)