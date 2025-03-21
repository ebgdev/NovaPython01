class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_begin(data)
            return
        new_node = Node(data)
        cur = self.head
        for _ in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        new_node.next = cur.next
        if cur.next:
            cur.next.prev = new_node
        cur.next = new_node
        new_node.prev = cur

    def search(self, key):
        cur = self.head
        index = 0
        while cur:
            if cur.data == key:
                return index
            cur = cur.next
            index += 1
        return -1

    def print_ll(self):
        cur = self.head
        while cur:
            print(cur.data, end=' <-> ')
            cur = cur.next
        print('None')

    def del_from_begin(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def del_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None

    def del_from_index(self, index):
        if index == 0:
            self.del_from_begin()
            return
        cur = self.head
        for _ in range(index):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        if cur.next:
            cur.next.prev = cur.prev
        if cur.prev:
            cur.prev.next = cur.next

# Example usage
dll = DoublyLinkedList()
dll.insert_at_begin(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_index(1, 15)
dll.print_ll()  # 10 <-> 15 <-> 20 <-> 30 <-> None
dll.del_from_end()
dll.print_ll()  # 10 <-> 15 <-> 20 <-> None
dll.del_from_begin()
dll.print_ll()  # 15 <-> 20 <-> None
dll.del_from_index(1)
dll.print_ll()  # 15 <-> None
