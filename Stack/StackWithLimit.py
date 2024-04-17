class Stack:
    def __init__(self, MaxSize):
        self.MaxSize = MaxSize
        self.stack = []

    def __str__(self):
        values = reversed(self.stack)
        values = [str(x) for x in values]
        return "\n".join(values)

    def is_empty(self):
        return len(self.stack) == 0

    def isFull(self):
        if self.MaxSize == self.size():
            return True
        return False

    def push(self, value):
        if self.MaxSize == len(self.stack):
            return "Stack is full"
        self.stack += [value]

    def pop(self):
        if self.is_empty():
            return None
        top = self.stack[-1]
        self.stack = self.stack[:-1]
        return top

    def peek(self):
        if self.is_empty:
            return None
        return self.stack[-1]

    def size(self):
        if self.is_empty():
            return None
        count = 0
        for _ in self.stack:
            count += 1
        return count

    def delete(self):
        self.stack = None


stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
stack.push(4)
print(stack)
print(stack.push(3))
stack.delete()
# print(stack)
