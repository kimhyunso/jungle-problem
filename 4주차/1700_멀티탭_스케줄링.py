import sys
sys.stdin = open("input.txt", "r")

multi_tap_cnt, electronic_cnt = map(int, input().split())
machines = list(map(int, input().split()))

multi_tap = []
count = 0

for i in range(electronic_cnt):
    # 멀티탭에 꽂혀있으면 다시
    if machines[i] in multi_tap:
        continue
    
    # 필요할 때만 꽃아야 함
    if len(multi_tap) < multi_tap_cnt:
        multi_tap.append(machines[i])
        continue

    # 멀티탭 상태를 고려하여 가장 늦게 다시 쓰이거나, 다시 안 쓰이는 기기를 찾아 교체할 대상을 선택하기
    latest_idx = -1
    target = -1

    for plugged in range(len(multi_tap)):
        try:
            next_idx = machines[i+1:].index(multi_tap[plugged]) # [i+1:]
        except ValueError:
            next_idx = float('inf')

        if next_idx > latest_idx:
            latest_idx = next_idx
            target = plugged

    multi_tap[target] = machines[i]
    count += 1
    
print(count)