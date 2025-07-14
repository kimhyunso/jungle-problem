def shaker_sort(numbers):
    left = 0
    right = len(numbers) - 1
    last = right

    while left < right:
        for j in range(right, left, -1):
            if numbers[j - 1] > numbers[j]:
                temp = numbers[j - 1]
                numbers[j - 1] = numbers[j]
                numbers[j] = temp
                last = j
        left = last

        for j in range(left, right):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j - 1] = numbers[j]
                numbers[j] = temp
        right = last
            

numbers = [3, 5, 2, 6, 1, 2, 8]
shaker_sort(numbers)
print(numbers)



