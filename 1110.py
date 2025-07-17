# 내문제 풀이
N = int(input())

numbers = []

left = N // 10
right = N % 10
while True:
    numbers.append((left + right) % 10)
    left = right
    right = numbers[-1]

    if (left * 10) + right == N:
        break

print(len(numbers))

# 이시영님
# 백준 1110번 문제: 더하기 사이클
import sys
input = sys.stdin.readline

N = int(input().strip())
result = 0 # 사이클 수
temp_n = N

while True:    
    ten_digit = temp_n // 10 
    one_digit = temp_n % 10

    if temp_n < 10:
        temp_n = one_digit * 10 + one_digit
    else:
        temp_n = one_digit * 10 + (ten_digit + one_digit) % 10

    result += 1

    if temp_n == N:
        break

print(result)

########################

import sys

n=int(sys.stdin.readline().rstrip())

temp=n
count=0

def one_cycle(n,count): # 중점 포인트는 받은 수를 [십의 자리수, 일의 자리수] list로 변환하여 계산함
    if n<10: # 한자리 수일 경우
        num_list=[n]
        num_list.insert(0,0) # 맨 앞에 0을 추가
        # 이후 [0,n]으로 됨

        # count+=1  # 이 동작도 사이클 횟수로 칠 지 몰라 count를 했지만 예제에서 1 =>60 이므로 이 문제는 해당 동작을 사이클 횟수로 안 침

    else: # 두자리 수일 경우
        num_list=list(map(int,str(n))) # 각 자리수를 리스트화 시킴 ex) 12 = [1,2]

    n=num_list[1]*10+sum(num_list)%10 # 일의 자리수를 십의 자리수로 옮기고 각 자리수 더한 값의 일의 자리수를 가져옴 ab= [b, (a+b)%10]
    count+=1
    return [n,count]

n,count=one_cycle(n,count) # 한번은 무조건 돌아야 하기 때문에
while temp!=n: # 처음 주어진 수와 같을 때 까지
    n,count=one_cycle(n,count)

print(count)

# list로 변환할 필요없이 십의자리수, 일의자리수를 담는 변수를 만들어서 거기에 바로 연산 진행해도됨 이러면 한자리수 일경우를 나누지 않아도 충분
# digit_10=n//10, digit_1=n%10 temp=digit_10
# digit_10=digit_1, digit_1=(digit_1+temp)%10
# new_n=digit_10*10+digit_1