# # import sys
# # sys.stdin = open("input.txt", "r") 

# N = int(input())
# arry = list(map(int, input().split()))
# M = int(input())
# find_numbers = list(map(int, input().split()))

# arry.sort()
# start = 0
# end = len(arry) - 1

# def binary_search(arry, find_number):
#     start = 0
#     end = len(arry) - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if arry[mid] == find_number:
#             return 1
#         elif arry[mid] > find_number:
#             end = mid - 1
#         elif arry[mid] < find_number:
#             start = mid + 1
#     return 0

# for find_number in find_numbers:
#     result = binary_search(arry, find_number)
#     print(result)

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
find_numbers = list(map(int, input().split()))

for num in find_numbers:
    print(1 if num in arr else 0)