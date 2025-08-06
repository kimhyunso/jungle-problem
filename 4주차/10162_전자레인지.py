buttons = [300, 60, 10]
T = int(input())

result = []
flag = False
for button in buttons:
    count = T // button
    T %= button
    if button == 10 and T % 10 != 0:
        flag = True
    result.append(count)

if flag:
    print(-1)
else:
    for r in result:
        print(r, end=' ')




