# 4 - 2 - 1
def shell_sort(numbers):
    n = len(numbers)
    h = n // 2

    while h > 0:
        for i in range(h, n): # 가운데 -> [7, 1, 9, 8]에 대한 인덱스
            j = i - h # 처음부터 가운데까지 인덱스 0 - 2
            temp = numbers[i]
            while j >= 0 and numbers[j] > temp: # 처음인덱스가 -로 넘어가지 못하게 막고 있음
                numbers[j + h] = numbers[j] 
                j -= h # 0, 1, 2 증가
            numbers[j + h] = temp
        
        h //= 2 # 전체 4, 2, 1 길이 [4번째 원소, 2번째 원소, 1번째원소]를 찾기위해 사용


# O(n)

numbers = [6, 4, 8, 7, 1, 9, 8]
shell_sort(numbers)

