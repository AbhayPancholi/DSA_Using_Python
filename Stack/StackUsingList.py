class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        values = reversed(self.stack)
        values = [str(x) for x in values]
        return "\n".join(values)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack = self.stack + [item]

    def pop(self):
        if self.is_empty():
            return None
        top = self.stack[-1]
        self.stack = self.stack[:-1]
        return top

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        count = 0
        for _ in self.stack:
            count += 1
        return count


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
