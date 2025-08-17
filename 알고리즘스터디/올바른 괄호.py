def solution(s):
    stack = []
    
    for word in s:
        if word == '(':
            stack.append('(')
        else:
            if len(stack) < 1:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    return False