class PQueue:
    def __init__(self):
        self.data = []
        self.priority = []

    def enqueue(self, val, priority: float):
        self.data.append(val)
        self.priority.append(priority)

    def dequeue(self):
        target_idx = 0
        for idx, prio in enumerate(self.priority):
            if prio > self.priority[target_idx]:
                target_idx = idx
        self.priority.pop(target_idx)
        return self.data.pop(target_idx)

    def peek(self):
        target_idx = 0
        for idx, prio in enumerate(self.priority):
            if prio > self.priority[target_idx]:
                target_idx = idx
        return self.data[target_idx]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str([(self.priority[i], self.data[i]) for i in range(len(self.data))])
