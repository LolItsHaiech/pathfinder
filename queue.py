class Queue:
    def __init__(self, capa: int):
        self.data = [0]*capa
        self.capa = capa
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, val: int):
        if self.size == self.capa:
            raise IndexError('Queue is full')
        self.data[self.front] = val
        self.front = (self.front + 1) % self.capa
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        a = self.data[self.rear]
        self.rear = (self.rear + 1) % self.capa
        self.size -= 1
        return a

    def peek(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        return self.data[self.rear]

    def is_full(self):
        return self.size == self.capa

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.size == 0:
            return '[]'
        lst = []
        i = self.rear
        f = True
        while i != self.front or f:
            f=False
            lst.append(str(self.data[self.rear]))
            i = (i+1) % self.capa
        return '['+', '.join(lst)+']'
