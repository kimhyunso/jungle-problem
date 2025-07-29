import sys
sys.stdin = open("input.txt", "r") 

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = len(numbers) - 1
min_value = float('inf')

l = 0
r = 0

while left < right:
    sum = numbers[left] + numbers[right]

    if abs(sum) < min_value:
        min_value = abs(sum)
        l = left
        r = right
    
    if sum < 0:
        left += 1
    else:
        right -= 1
    

print(numbers[l], numbers[r])
