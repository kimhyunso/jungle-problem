import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 최단 거리, 최장 거리
house_count, wifi = map(int, input().split())
house_matrix = []

for _ in range(house_count):
    house_matrix.append(int(input()))
house_matrix.sort()

start = house_matrix[0]
end = house_matrix[-1] - house_matrix[0]

def binary_search(start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = 1 # 와이파이 설치 개수
        last = house_matrix[0]
        
        for i in range(1, house_count):
            if house_matrix[i] - last >= mid:
                count += 1
                last = house_matrix[i]
        
        if count >= wifi:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

result = binary_search(start, end)
print(result)









