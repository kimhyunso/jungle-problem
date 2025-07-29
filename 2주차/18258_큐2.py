import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.front_ = 0
        self.rear = 0
        self.count = 0
        self.que = [None] * capacity

    def push(self, x):
        if self.rear < self.capacity:
            self.que[self.rear] = x
            self.rear = (self.rear + 1) % self.capacity
            self.count += 1

    def pop(self):
        if self.count == 0:
            return -1
        value = self.que[self.front_]
        self.front_ = (self.front_ + 1) % self.capacity
        self.count -= 1
        return value


    def size(self):
        return self.count

    def empty(self):
        if self.size() <= 0:
            return 1
        return 0

    def front(self):
        if self.count > 0:
            return self.que[self.front_]
        return -1
    
    def back(self):
        if self.count > 0:
            return self.que[self.rear - 1]
        return -1

N = int(input())

queue = Queue(N)
for _ in range(N):
    commands = input().split()

    if commands[0] == 'push':
        queue.push(commands[1])
    elif commands[0] == 'front':
        print(queue.front())
    elif commands[0] == 'back':
        print(queue.back())
    elif commands[0] == 'size':
        print(queue.size())
    elif commands[0] == 'pop':
        print(queue.pop())
    elif commands[0] == 'empty':
        print(queue.empty())
