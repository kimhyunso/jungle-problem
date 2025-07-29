import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
papers = []
white = 0
blue = 0

for i in range(N):
    papers.append(list(map(int, input().split())))

def make_papers(x, y, size):
    global white, blue
    color = papers[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if papers[i][j] != color:
                half = size // 2
                make_papers(x, y, half)
                # 2분기 0 ~ 4 / 4 ~ 8
                make_papers(x, y + half, half)
                # 3분기 4 ~ 8 / 0 ~ 4
                make_papers(x + half, y, half)
                # 4분기 4 ~ 8 / 4 ~ 8
                make_papers(x + half, y + half, half)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

make_papers(0, 0, N)

print(white)
print(blue)    




