def solution(s):
    temp = list(map(int, s.split(' ')))
    max_value = max(temp)
    min_value = min(temp)

    return str(min_value) + ' ' + str(max_value)