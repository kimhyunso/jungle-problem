# O(N^2)

def insert_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp


numbers = [10, 4, 5, 7, 2, 1]
insert_sort(numbers)

print(numbers)




