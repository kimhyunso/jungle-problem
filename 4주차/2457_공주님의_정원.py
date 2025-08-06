import sys
sys.stdin.readline
sys.stdin = open("input.txt", "r")

flower_cnt = int(input())
graden = []

for _ in range(flower_cnt):
    start_month, start_day, end_month, end_day = map(int, input().split())
    graden.append((start_month * 100 + start_day, end_month * 100 + end_day))

graden.sort()

start = 301
end = 1130
idx = 0
cnt = 0
max_end = 0

while start <= end:
    updated = False
    while idx < flower_cnt and graden[idx][0] <= start:
        if graden[idx][1] > max_end:
            max_end = graden[idx][1]
            updated = True
        idx += 1

    if not updated:
        cnt = 0
        break

    start = max_end
    cnt += 1

print(cnt)



