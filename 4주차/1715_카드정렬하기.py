import sys, heapq
sys.stdin = open("input.txt", "r")

N = int(input())
cards = [int(input()) for _ in range(N)]
cards.sort()

heapq.heapify(cards)
cost = 0

while 1 <= len(cards) - 1:
    card_dec1 = heapq.heappop(cards)
    card_dec2 = heapq.heappop(cards)

    result = card_dec1 + card_dec2
    heapq.heappush(cards, result)
    cost += result

print(cost)










