# 이시영님
#  백준 9095 : 1, 2, 3 더하기
import sys
input = sys.stdin.readline

T = int(input().strip())
result = []

# 재귀함수 작성 : 1,2,3의 합으로 n을 만들 수 있는 경우의 수를 구하는 함수(dp 사용 X)
def solve_recursive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return solve_recursive(n - 1) + solve_recursive(n - 2) + solve_recursive(n - 3)

for _ in range(T):
    n = int(input().strip())
    result.append(solve_recursive(n))

sys.stdout.write('\n'.join(map(str, result)) + '\n')


##########

import sys

n=int(sys.stdin.readline().rstrip())

dp=[0]*12
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=4

for _ in range(n):
    problem=int(sys.stdin.readline().rstrip())
    if problem>=4: # 최적화 및 예외 방지를 위해
        for i in range(4,problem+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[problem])

# 해당 문제의 착안점은 n>3일 경우 모든 경우의 수든 항상 끝에 1,2,3이 온다는 것임
# 따라서 마지막에 1이 오는 경우는 dp[i-1]만큼 나타낼 수 있고, 마지막이 2가 되는 경우는 dp[i-2]만큼 나타낼 수 있고 마지막이 3이 되는 경우는 dp[i-3]만큼 나타낼 수 있다.
# indexerror를 방지하기 위해 초깃값을 dp[0]~dp[3]까지 구해두면 문제 없음.