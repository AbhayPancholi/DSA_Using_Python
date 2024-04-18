class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.counter = 0

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode.value
            curNode = curNode.next

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.counter += 1
        return "Element inserted successfully"

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        return self.head.value

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head.value
        self.head = self.head.next
        self.counter -= 1
        return popped_node

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.counter


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Popped node: {stack.pop()}")
print(f"Is the stack empty? {stack.isEmpty()}")

for element in stack:
    print(element)

print(stack.size())
