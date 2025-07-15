import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key):
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        
        return None

    def add(self, key, value):
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return False
            node = node.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key):
        hash = self.hash_value(key)
        node = self.table[hash]
        head = None

        while node is not None:
            if node.key == key:
                if head is None:
                    self.table[hash] = node.next
                else:
                    head.next = node.next
            head = node
            node = node.next
        return False
    
    def dump(self):
        for i in range(self.capacity):
            node = self.table[i]
            print(i, end='')
            while node is not None:
                print(f' -> {node.key} ({node.value})', end='')
                node = node.next
            print()

    
    

    


                
            

    
