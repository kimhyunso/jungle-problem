def seq_search_while(nums, key):
    index = 0
    while True:
        if nums[index] == key:
            return 1
        if len(nums) == index:
            return -1
        index += 1

def seq_search_for(nums, key):
    for num in nums:
        if num == key:
            return 1
    return -1

def binary_search(nums, key):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] == key:
            return nums[mid]
        elif nums[mid] < key:
            start = mid + 1
        elif nums[mid] > key:
            end = mid - 1
    return -1



numbers = [5, 2, 3, 6, 8, 10, 30]
numbers.sort()
print(binary_search(numbers, 90))







