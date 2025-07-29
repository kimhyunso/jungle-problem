import sys
sys.stdin = open("input.txt", "r") 

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
target = int(input())

left = 0
right = len(numbers) - 1

count = 0

while left < right:
    sum = numbers[left] + numbers[right]
    
    if sum == target:
        count += 1
        left += 1
        right -= 1
    elif sum < target: # target보다 값이 커져야하니 <
        left += 1
    else: # target보다 값이 작아져야하니 >
        right -= 1


print(count)
            



