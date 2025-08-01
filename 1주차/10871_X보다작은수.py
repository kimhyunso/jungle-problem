# 문제 이해못함 [보류]

'''
X보다 작은 수 성공
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	380414	208358	166833	54.259%
문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

예제 입력 1 
10 5
1 10 4 9 2 3 8 5 7 6
예제 출력 1 
1 4 2 3
'''

X, target_number = map(int, input().split())
numbers = list(map(int, input().split()))
result = []

for number in numbers:
    if target_number > number:
        result.append(number)

for num in result:
    print(num)