def binary_search(key, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
    return 0

key = 2
arry = [i for i in range(8)]
x = binary_search(key, arry)
print(x)


def upper_bound(arr, key):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return start - 1

index = upper_bound(arry, 3)
print(arry[index - 1])


