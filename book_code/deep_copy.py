arrays = [15, 64, 53, ['ABC', 'BDC'], 'AAA']

for array in arrays:
    print(f'array = {array}, type = {type(array)}')


# list.copy: 얕은 복사

arrays2 = arrays.copy()
arrays2[3][0] = '변경하기'
arrays2[2] = 150

print(arrays, arrays2)


import copy
arrays3 = copy.deepcopy(arrays)
arrays3[3][0] = '변경하기3'

print(arrays, arrays3)