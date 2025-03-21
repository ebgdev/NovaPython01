import gc
from icecream import ic


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, n_data):
        new_node = Node(n_data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def insert_at_begin(self, n_data):
        new_node = Node(n_data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node

    def insert_at_index(self, index, n_data):
        new_node = Node(n_data)
        if self.head is None or index == 0:
            self.insert_at_begin(n_data)
            return

        cur = self.head
        position = 0
        while cur.next != self.head and position + 1 != index:
            position += 1
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node

    def search(self, target):
        if self.head is None:
            return None
        cur = self.head
        index = 0
        while True:
            if cur.data == target:
                return index
            cur = cur.next
            index += 1
            if cur == self.head:
                break
        return None

    def delete_from_begin(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = self.head.next
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return

        cur = self.head
        prev = None
        while cur.next != self.head:
            prev = cur
            cur = cur.next
        prev.next = self.head

    def reverseList(self, head):
        prev = None
        cur = head
        if cur is None:
            return None
        first = cur
        while True:
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
            if cur == first:
                break
        head.next = prev
        return prev

    def reverse(self):
        self.head = self.reverseList(self.head)

    def __str__(self):
        if self.head is None:
            return "Empty List"
        temp = ""
        cur = self.head
        while True:
            temp += f"{cur.data} --> "
            cur = cur.next
            if cur == self.head:
                break
        temp += "(Back to Head)"
        return str(temp)


# Test Cases
l1 = CircularLinkedList()
l1.insert_at_end("node1")
l1.insert_at_end("node2")
l1.insert_at_end("node3")
l1.insert_at_begin("leo")
l1.insert_at_end("node4")

print("Original List:")
print(l1)

ic(l1.delete_from_begin())
ic(l1.delete_from_end())
gc.collect()
print("After Deletions:")
print(l1)

# Testing insert_at_index
l1.insert_at_index(1, "newNode")
print("After inserting at index 1:")
print(l1)

# Testing reverse
l1.reverse()
print("After Reversing:")
print(l1)
