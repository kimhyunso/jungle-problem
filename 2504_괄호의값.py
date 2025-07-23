import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

brakets = input().strip()

stack = []

for braket in brakets:
    if braket == '(' or braket == '[':
        stack.append(braket)

    if stack and braket == ')':
        temp = 0
        while stack:
            content = stack.pop()
            if content == '(':
                # stack.pop()
                stack.append(2 if temp == 0 else temp * 2)
                break
            elif isinstance(content, int):
                temp += content
            else:
                print(0)
                exit()

    elif stack and braket == ']':
        temp = 0
        while stack:
            content = stack.pop()
            if content == '[':
                # stack.pop()
                stack.append(3 if temp == 0 else temp * 3)
                break
            elif isinstance(content, int):
                temp += content
            else:
                print(0)
                exit()

# if any(isinstance(x, str) for x in stack):
#     print(0)
# else:
#     print(sum(stack))

if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))