numbers = [5, 6, 4, 8, 3, 7, 9, 0, 1, 5, 2, 3]

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    
    mid = len(numbers) // 2
    low_numbers = merge_sort(numbers[:mid])
    high_numbers = merge_sort(numbers[mid:])
    result = []

    l = h = 0
    while l < len(low_numbers) and h < len(high_numbers):
        if low_numbers[l] < high_numbers[h]:
            result.append(low_numbers[l])
            l += 1
        else:
            result.append(high_numbers[h])
            h += 1
    result += low_numbers[l:]
    result += high_numbers[h:]
    return result

merge_sort(numbers)

print(numbers)
