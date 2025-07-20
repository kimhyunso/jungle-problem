# 링큐
class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.no = 0 # 큐에 쌓여있는 데이터 개수를 나타내는 int형 정수
        self.front = 0 # 가장 처음에 넣은 맨 앞 원소 인덱스
        self.rear = 0 # 가장 마지막에 넣은 끝 원소의 다음 인덱스
        self.capacity = capacity
        self.que = [None] * capacity
    
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    # rear, no 증가
    # 만약 rear와 capacity 배열의 깊이가 같다면 rear를 0으로 만듬으로써 원형 큐를 유지한다.
    def enque(self, x):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity: # 인큐하기 전 rear가 capacity를 넘지 않도록
            self.rear = 0

    # front 증가, no 감소
    # 만약 front와 capacity 배열의 깊이가 같다면 front를 0으로 만듬으로써 원형 큐 유지
    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity: # 디큐하기 전 front가 capacity를 넘지 않도록
            self.front = 0
        return x
    
    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value):
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value):
        return self.count(value)
    
    def clear(self):
        self.no = self.front = self.rear = 0
    
    def dump(self):
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()

que = FixedQueue(5)
que.enque(10)
que.enque(2)
que.enque(3)

result = que.peek()
print(result)


front = que.deque()
print(front)



