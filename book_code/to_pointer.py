arr = [i for i in range(8)]
target = 7

left = 0
right = len(arr) - 1

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print(arr[left], arr[right])
        left += 1
        right -= 1
    elif s < target:
        left += 1
    else:
        right -= 1
        
    