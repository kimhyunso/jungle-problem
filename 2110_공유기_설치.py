# 마스터정리
import sys
sys.stdin = open("input.txt", "r") 

house_count, wifi = map(int, input().split())
houses = []

for i in range(house_count):
    houses.append(int(input()))

houses.sort()

# 집에 공유기를 설치할 수 있는 최대의 거리를 구하기
# 집 간의 거리는 배열로 주어짐

start = houses[0]
end = houses[-1] - houses[0]
max_d = 0

def binary_search(start , end):
    global max_d
    if start > end:
        return
    
    mid = (start + end) // 2
    w = 1
    last = houses[0]

    for i in range(len(houses)):
        if houses[i] - last >= mid:
            last = houses[i]
            w += 1
    if w >= wifi:
        max_d = max(mid, max_d)
        binary_search(mid+1, end)
    else:
        binary_search(start, mid-1)



binary_search(start, end)

print(max_d)
