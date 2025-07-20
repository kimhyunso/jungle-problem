import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
papers = []
count = 0

for i in range(N):
    papers.append(list(map(int, input().split())))

def make_paper(width_len, w, height_len, h):
    global count
    if w <= 1 or h <= 1:
        return

    temp = papers[0][0]

    for i in range(width_len, w):
        for j in range(height_len, h):
            if papers[i][j] != temp:
                pass


make_paper(1, 1, N, N)

print(count)
    



