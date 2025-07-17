# import sys
# sys.stdin = open("input.txt", "r") 

# N 나무의 개수 / M 상근이가 가져갈 나무 길이
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

def binary_search():
    start = 0
    end = max(tree_list)

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for tree in tree_list:
            if tree > mid:
                total = total + (tree - mid)

        if total < M:
            end = mid - 1
        else:
            start = mid + 1
    return end

count = binary_search()
print(count)












