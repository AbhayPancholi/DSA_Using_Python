class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        values = [str(x) for x in self.queue]
        return " ".join(values)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        self.queue = self.queue[1:]

    def peek(self):
        return self.queue[0]

    def delete(self):
        self.queue = []
        return "Queue successfully deleted"


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue)
queue.dequeue()
print(queue)
