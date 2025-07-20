import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

A, B, C = map(int, input().split())

def merge(x, n, c):
    if n <= 0:
        return 1

    result = merge(x, n // 2, c)
    if n % 2 == 0:
        return (result * result) % c
    else:
        return ((result * result) * x) % c

result = merge(A, B, C)
print(result)
    


