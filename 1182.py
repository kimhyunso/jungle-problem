# 이시영님
# 백준 1182 : 부분수열의 합
import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
count = 0

def solve_recursive(current_sum, depth):
    global count

    if depth == N:
        if current_sum == S:
            count += 1
        return

    solve_recursive(current_sum + arr[depth], depth + 1) # 포함
    solve_recursive(current_sum, depth + 1) # 포함X

solve_recursive(0,0)

# S가 0인 경우 : 첫 시점에 아무것도 선택하지 않은 경우도 하나의 부분수열로 간주되므로
if S == 0:
    count -= 1

sys.stdout.write(f"{count}\n")

# 5 0
# -7 -3 -2 5 8

########################3

import sys

n,answer_sum=list(map(int,sys.stdin.readline().rstrip().split()))

num_list=list(map(int,sys.stdin.readline().rstrip().split()))

count=0
for bit in range(1,1<<n):
    check_sum=0
    for i,value in enumerate(num_list):
        if bit&(1<<i): # i번째 원소가 있다.
            check_sum+=value
    if check_sum==answer_sum:
        count+=1

print(count)

# 이 문제는 bitmask로 해결했음.
# num_list에는 문제에서 주어진 순서대로 숫자들이 0~n-1번째까지 존재하는데,
# 숫자들의 조합의 경우를 bit로 나타내었음. ex) 00101 은 0번째 원소와 2번째 원소가 더해지는 경우
# 이 조합을 (len(num_list)==5일 경우로 예를 들면) 00001부터 11111까지 전부 계산하면서 구하고자 하는 합과 같을 경우 count+=1