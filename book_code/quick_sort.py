# log N

count = 0

def partition(numbers, left, right):
    global count
    count += 1
    
    partition_left = left
    partition_right = right
    pivot_num = numbers[(left + right) // 2]

    while partition_left <= partition_right:
        while numbers[partition_left] < pivot_num: partition_left += 1
        while numbers[partition_right] > pivot_num: partition_right -= 1
        if partition_left <= partition_right:
            numbers[partition_left], numbers[partition_right] = numbers[partition_right], numbers[partition_left]
            partition_left += 1
            partition_right -= 1

    if left < partition_right: 
        print(f'{count} 왼쪽 파티션: {numbers[:partition_left]} 현재 INDEX: [:{partition_left}]')
        partition(numbers, left, partition_left)

    if partition_left < right: 
        print(f'{count} 오른쪽 파티션: {numbers[right:]} 현재 INDEX: [{right}:]')
        partition(numbers, partition_left, right)

numbers = [1, 8, 7, 4, 5, 2, 6, 3, 9]
partition(numbers, 0, len(numbers) - 1)

print(numbers)