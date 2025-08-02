import sys
sys.stdin = open("input.txt", "r")

N = int(input())
times = []

for _ in range(N):
    start_time, end_time = map(int, input().split())
    times.append((start_time, end_time))

times.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in times:
    if start >= end_time:
        end_time = end
        count += 1

print(count)

