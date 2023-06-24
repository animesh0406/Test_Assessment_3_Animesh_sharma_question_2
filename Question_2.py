# Question 2
# Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.
class Queue:
    def __init__(self):
        self.items = list()

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
