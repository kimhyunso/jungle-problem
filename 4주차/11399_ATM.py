N = int(input())
money = list(map(int, input().split()))
money.sort()

for n in range(1, len(money)):
    money[n] = money[n - 1] + money[n]

print(sum(money))




