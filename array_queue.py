class ArrayQueue:
    DEFAULT_SIZE = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def _len(self):
        return self._size
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1


    def resize(self, cap):
        old = self._data
        self._data = [None]* cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) %len(old)
        self._front = 0


    def dequeue(self):
        if self.is_empty():
            raise Exception("QUEUE EMPTY")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        
        return answer

    def first(self):
        if self.is_empty():
            raise Exception("QUEUE EMPTY")
        return self._data[self._front]


q = ArrayQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.first()
q.resize(20)
q.is_empty()