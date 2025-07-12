'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3
'''

N = input()
nums = list(map(int, input().split()))
net = [2, 3, 5, 7]
count = 0

# 자기 자신으로 나누어 떨어지고, 2, 3, 5, 7로 나누어 떨어지지 않는 것

for num in nums:
    if num != 1: # 1이면 돌지 않음
        for i in range(2, num):
            if num % i == 0: # 2, 3, 5, 7로 나눔 만약 나누어 떨어지면 else 실행
                break
        else:
            count += 1

print(count)