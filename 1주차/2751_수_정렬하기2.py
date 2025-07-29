'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
5
5
4
3
2
1
예제 출력 1 
1
2
3
4
5
'''
import sys


def find_mid(numbers, left, mid, right):
    if numbers[mid] < numbers[left]:
        numbers[mid], numbers[left] = numbers[left], numbers[mid]
    if numbers[right] < numbers[mid]:
        numbers[right], numbers[mid] = numbers[mid], numbers[right]
    return mid



def partition(numbers, left, right):
    partition_left = left
    partition_right = right
    pivot_index = find_mid(numbers, partition_left, (left + right) // 2, partition_right)
    pivot = numbers[pivot_index]

    while partition_left <= partition_right:
        while numbers[partition_left] < pivot: partition_left += 1
        while numbers[partition_right] > pivot: partition_right -= 1

        if partition_left <= partition_right:
            numbers[partition_left], numbers[partition_right] = numbers[partition_right], numbers[partition_left]
            partition_left += 1
            partition_right -= 1
    
    if left < partition_right:
        partition(numbers, left, partition_left)
    
    if partition_left < right:
        partition(numbers, partition_left, right)


N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

partition(numbers, 0, len(numbers) - 1)

for num in numbers:
    print(num)



    