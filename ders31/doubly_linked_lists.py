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
            for _ in range(index):
                cur = cur.next
        else:  # Closer to tail
            cur = self.tail
            for _ in range(self.length - 1, index, -1):
                cur = cur.prev

        return cur
    

    def set_value(self,index,value):
        cur = self.get(index) # there is two states either cur will be None or will return node
        if cur:
            cur.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.advanced_get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after

        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
        

    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     elif index == 0:
    #         return self.prepend(value)
    #     elif index == self.length:
    #         return self.append(value)
    #     else:
    #         new_node = Node(value)
    #         before = self.advanced_get(index-1)
    #         after = before.next

    #         new_node.prev = before
    #         new_node.next = after

    #         before.next = new_node
    #         after.prev = new_node

    #         self.length += 1
    #         return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
            
        if index == self.length-1:
            return self.pop()
        
        cur = self.advanced_get(index)
        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        cur.next = None
        cur.prev = None

        self.length -=1
        return cur
    
    def print_form_last(self):
        if self.length == 0:
            return None
        cur = self.tail
        alist = [" <-- None"]
        while cur:
            alist.insert(0,f" <-- {cur.value} ")
            cur = cur.prev
        astr = " None " + "".join(alist)
        print(astr)
            

# Test the doubly linked list
dl = DoublyLinkedList("emir") 
dl.prepend("ahmet")

dl.append("yusuf")
dl.append("ali")
dl.append("burak")
dl.append("onur")
dl.append("erhan")
dl.insert(1,"erdal")
print(dl.print_list())
ic(dl.length)
t1 = time()
ic(dl.basic_get(6))
t2 = time()
ic(dl.advanced_get(6))
t3 = time()

ic(t2-t1)
ic(t3-t2)

dl.print_form_last()
    