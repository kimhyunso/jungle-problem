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
nets = [2, 3, 5, 7]
count = 0

for num in nums:
    for net in nets:
        if num == net:
            count += 1
            break
        elif num % net != 0:
            count += 1
            break
   
print(count)
