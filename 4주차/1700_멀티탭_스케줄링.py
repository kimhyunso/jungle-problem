import sys
sys.stdin = open("input.txt", "r")

multi_tap, electronic_cnt = map(int, input().split())
use_orders = list(map(int, input().split()))

flugs = []

for i in range(multi_tap):
    flugs.append(use_orders[i])

count = 0

for i in range(multi_tap, electronic_cnt):
    for j in range(len(flugs)):
        if i + 1 < electronic_cnt and flugs[j] == use_orders[i + 1]:
            flugs[j] = use_orders[i]
            count += 1
            break

print(count)

