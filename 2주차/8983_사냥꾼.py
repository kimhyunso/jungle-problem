# 사냥감의 갯수새기 문제
# M = 사대수, N = 동물의 수, L = 사정거리
import sys
sys.stdin = open("input.txt", "r") 

M, N, L = map(int, input().split())

gun_bases = list(map(int, input().split())) # 사대
gun_bases.sort()

animal_positions = []
for _ in range(N):
    animal_positions.append(list(map(int, input().split())))
count = 0

# 사냥감의 좌표
for animal in animal_positions:
    start = 0
    end = len(gun_bases) - 1
    x = animal[0]
    y = animal[1]

    while start <= end:
        mid = (start + end) // 2

        # 사냥감이 사정거리 안에 있는지 판단
        if abs(gun_bases[mid] - x) + y <= L:
            count += 1
            start = end + 1
        # 사대가 동물보다 왼쪽에 있는지 판별
        elif gun_bases[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

print(count)