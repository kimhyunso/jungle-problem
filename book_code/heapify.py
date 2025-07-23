# def heapify(arr):
#     current = start = len(arr) - 1
#     while start > 0:
#         is_swaped = False

#         while current > 0:
#             parent = (current - 1) // 2 # 부모요소 
#             if arr[parent] > arr[current]:
#                 arr[parent], arr[current] = arr[current], arr[parent]
#                 current = parent
#                 is_swaped = True
#             else:
#                 break

#         if is_swaped:
#             current = start
#         else:
#             current = start = current - 1

from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

if heap:
    print(0)

for num in nums:
    heappush(heap, (-num, num))

# print(heappop(heap)[1])