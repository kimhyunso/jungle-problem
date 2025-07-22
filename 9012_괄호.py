import sys
sys.stdin = open("input.txt", "r")

N = int(input())

for _ in range(N):
    stack = []
    brekets = input()
    is_vps = True
    for breket in brekets:
        if breket == '(':
            stack.append(breket)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    
    if not stack and is_vps:
        print('YES')
    else:
        print('NO')

    





