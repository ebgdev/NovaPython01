from icecream import ic 
from time import time
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if not self.head:
            return "None"
        astr = "None <--> "
        cur = self.head
        while cur:
            astr += f"{cur.value} <--> "
            cur = cur.next
        astr += "None"
        return astr

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1  
        return True
    
    def pop(self):
        if self.length == 0:  
            return None
        cur = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:  
                self.tail.next = None
            cur.prev = None
        self.length -= 1
        return cur  # Return the popped node safely
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            next_value = self.head
            self.head = new_node
            new_node.next = next_value
            next_value.prev = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def basic_get(self,index):
        # get method should return node itself so that's why we dont return cur.value
        if index < 0 or index>=self.length:
            return None
        position = 0
        cur = self.head
        while position != index:
            position +=1
            cur = cur.next
        # returning value itself
        return cur
    
    def advanced_get(self, index):
        if index < 0 or index >= self.length:  # Out-of-bounds check
            return None

        if index < self.length // 2:  # Closer to head
            cur = self.head
            pass
        else:  # Closer to tail
            pass

        return cur
    

    
# Test the doubly linked list
dl = DoublyLinkedList("emir") 
dl.prepend("ahmet")

dl.append("yusuf")
dl.append("ali")
dl.append("burak")
dl.append("onur")
dl.append("erhan")


print(dl.print_list())