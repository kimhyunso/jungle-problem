import sys
sys.stdin = open("input.txt", "r")

product_cnt, bag = map(int, input().split())

weights = [0] * (product_cnt + 1)
varables = [0] * (product_cnt + 1)

for i in range(1, product_cnt + 1):
    weights[i], varables[i] = map(int, input().split())

# 행: 물건의 개수 / 열: 가방의 최대용량
memo = [[0] * (bag + 1) for _ in range(product_cnt + 1)]
for cur_object in range(1, product_cnt + 1): # 물건의 개수
    for limit in range(1, bag + 1): # 가방의 용량


        # 1. 배낭에 넣는다.
        if weights[cur_object] <= limit: # 현재 물건 무게가 가방의 최대 용량 이하라면
            memo[cur_object][limit] = max(memo[cur_object - 1][limit], memo[cur_object - 1][limit - weights[cur_object]] + varables[cur_object])
            # 이 중 큰 가치의 값을 유지
        
        # 2. 배낭에 넣지 않는다.
        else:   # 현재 물건의 무게가 가방의 초대 용량보다 크다면
            memo[cur_object][limit] = memo[cur_object - 1][limit] # 현재 물건을 넣지 못함으로 가치의 값 유지


print(memo[-1][-1])


