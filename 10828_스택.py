import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.ptr = 0
        self.stk = [None] * capacity
    def size(self):
        return self.ptr
    
    def empty(self):
        if self.ptr <= 0:
            return 1
        return 0
    
    def top(self):
        if self.ptr > 0:
            return self.stk[self.ptr - 1]
        return -1
        
    def push(self, x):
        if self.ptr < self.capacity:
            self.stk[self.ptr] = x
            self.ptr += 1
    def pop(self):
        if self.ptr > 0:
            self.ptr -= 1
            return self.stk[self.ptr]
        return -1

N = int(input())
stack = Stack(N)

for _ in range(N):
    commands = input().split()
    if commands[0] == 'push':
        stack.push(int(commands[1]))
    elif commands[0] == 'pop':
        print(stack.pop())
    elif commands[0] == 'top':
        print(stack.top())
    elif commands[0] == 'size':
        print(stack.size())
    elif commands[0] == 'empty':
        print(stack.empty())

