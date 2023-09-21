class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        super().__init__()
        print("I caught it")


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        try:
            val = self.queue[-1]
            del self.queue[-1]
            return val
        except IndexError:
            raise QueueError()

    def queue_contents(self):
        return bool(self.queue)


que = Queue()
print(que.queue_contents())
que.put(1)
que.put("dog")
que.put(False)
print(que.queue_contents())
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
