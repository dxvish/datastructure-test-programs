# Stack using python - Operations Supported - Push, Pop, Is Empty, Top, Size

class ArrayStack:
    def __init__(self):
        self.array = []
    
    def push(self, item):
        self.array.append(item)
        

    def pop(self):
        if self.is_empty():
            raise Exception("EMPTY")
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0

    def top(self):
        if self.is_empty():
            raise Exception("EMPTY")
        return self.array[-1]

    def get_size(self):
        return len(self.array)
    