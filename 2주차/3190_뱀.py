import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(input())
apple_cnt = int(input())
def map_init():
    maps = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(apple_cnt):
        x, y = map(int, input().split())
        maps[x - 1][y - 1] = 1
    return maps
maps = map_init()

que = deque([(0, 0)])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

game_time = 0
command_cnt = int(input())
commands = dict()
for _ in range(command_cnt):
    time, command = input().split()
    commands[int(time)] = command

while True:
    game_time += 1

    x, y = que[-1]
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if (x, y) in que:
        break

    if maps[x][y] == 1:
        maps[x][y] = 0
        que.append((x, y))
    else:
        que.append((x, y))
        que.popleft()
    
    if game_time in commands:
        if commands[game_time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(game_time)