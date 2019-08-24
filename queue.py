class Queue:
    def __init__(self):
        self.queue = []
        self.first = 0
        self.last = 0
    
    def enqueue(self, val):
        self.queue += [val]
        self.last += 1

    def dequeue(self):
        if (len(self.queue) == 0):
            print("Nothing in the queue")
        else:
            del self.queue[self.first]
            self.last -= 1


newQ = Queue()
newQ.enqueue(2)
newQ.enqueue(3)
newQ.enqueue(5)
newQ.enqueue(100)
newQ.dequeue()
newQ.dequeue()
print(newQ.queue)

