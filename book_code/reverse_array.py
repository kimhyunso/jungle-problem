# 배열 원소를 역순으로 정렬하는 알고리즘

def reverse_array(numbers):
    num_length = len(numbers) # 7
    for i in range(num_length // 2):
        numbers[i], numbers[num_length - i - 1] = numbers[num_length - i - 1], numbers[i]


numbers = [3, 5, 7, 8]
reverse_array(numbers)
print(numbers)