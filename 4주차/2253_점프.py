import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
rocks = []

for _ in range(M):
    rocks.append(int(input()))
rocks.sort()

jumps = [0 * (N + 1) for _ in range(N + 1)]

jumps[1][1] = 1






