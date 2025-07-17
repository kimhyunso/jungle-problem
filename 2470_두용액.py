import sys
sys.stdin = open("input.txt", "r") 

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = len(numbers) - 1
result = []

for i in range(N // 2):
    result.append([numbers[left] + numbers[right], left, right])

    left += 1
    right -= 1

min_value = 0

# 0에 가까우니 0에 근접한 것 찾기

for i in range(len(result)):
    if min_value > result[i][0]:
        print(numbers[result[i][1]], numbers[result[i][2]])
