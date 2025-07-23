class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # 마지막 값을 루트로
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


heap = MinHeap()

heap.push(5)
heap.push(3)
heap.push(8)
heap.push(1)
heap.push(2)

# print("Heap:", heap)

