import gc
from icecream import ic

# sona eklerken veya sondan cikarirken yapacagim islem while :cur.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, n_data):
        new_node = Node(n_data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_at_begin(self, n_data):
        new_node = Node(n_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, n_data):
        new_node = Node(n_data)
        cur = self.head

        if cur is None or index == 0:
            self.insert_at_begin(n_data)
            return

        position = 0
        while cur is not None and position + 1 != index:
            position += 1
            cur = cur.next

        if cur is not None:
            new_node.next = cur.next
            cur.next = new_node
        else:
            print("index not present")

    def search(self, target):
        cur = self.head
        index = 0
        while cur:
            if cur.data == target:
                return index
            cur = cur.next
            index += 1
        return None

    def delete_from_begin(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        cur = self.head
        temp_prev = None

        while cur.next:
            temp_prev = cur
            cur = cur.next

        if temp_prev:
            temp_prev.next = None

    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev  # New head of the reversed list

    def reverse(self):
        self.head = self.reverseList(self.head)

    def __str__(self):
        temp = ""
        cur = self.head
        while cur:
            temp += f"{cur.data} --> "
            cur = cur.next
        temp += "None"
        return str(temp)


# Test Cases
l1 = LinkedList()
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
