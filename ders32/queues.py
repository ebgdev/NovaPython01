# FIFO --> first in first out
# head --> first , tail --> last
from icecream import ic

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1  # Space after '=' for readability

    def print_queue(self):
        cur = self.first
        while cur:
            print(cur.value)
            cur = cur.next

    def enqueue(self, value):  # Adds to the end
        new_node = Node(value)
        if self.first is None:  # Edge case: Empty queue
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1  # Indentation fixed

    def dequeue(self):  # Removes from the front
        if self.first is None:  # Edge case: Empty queue
            return None
        cur = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return cur.value  # Return the dequeued value instead of the node
    
    def in_and_last(self):
        return self.first.value,self.last.value

# Testing
my_queue = Queue("fatih")
my_queue.enqueue("adil")
my_queue.enqueue("emir")
my_queue.enqueue("taha")
my_queue.dequeue()
my_queue.enqueue("mess")

my_queue.print_queue()
ic(my_queue.in_and_last())
