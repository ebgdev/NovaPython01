# Linked lists are used in various real-world applications where dynamic memory allocation, fast insertions/deletions, and efficient data management are required. Here are some key areas where linked lists are useful:

# 1. Dynamic Memory Allocation (OS and Memory Management)
# Use Case: Operating systems use linked lists to manage memory blocks dynamically (e.g., free memory blocks, process scheduling).
# Why? Unlike arrays, linked lists allow dynamic allocation and deallocation of memory without requiring a contiguous block.
#
# 2. Implementing Stacks and Queues
# Use Case: Linked lists form the basis of stack (LIFO) and queue (FIFO) implementations in many programming languages and applications.
# Why? Linked lists allow easy insertion and deletion at both ends without needing to shift elements (as required in arrays).
#
# 3. Undo/Redo Functionality in Applications
# Use Case: Word processors, image editors, and IDEs use linked lists to keep track of previous states (undo/redo functionality).
# Why? A doubly linked list allows traversal in both directions, making it easy to go back and forth between states.
#
# 4. Browser History Management
# Use Case: Web browsers use a doubly linked list to manage the back and forward navigation history.
# Why? Each visited webpage is stored as a node, and users can easily navigate backward and forward without excessive memory operations.
#
# 5. Music and Video Playlists (Media Players)
# Use Case: Media players use linked lists to manage playlists, allowing users to play, pause, skip, or loop tracks efficiently.
# Why? Linked lists allow easy addition, removal, and reordering of songs without resizing an array.
#
# 6. Graph Representation (Adjacency List in Graphs)
# Use Case: Graphs in networks, social media connections, and pathfinding algorithms use adjacency lists (implemented using linked lists).
# Why? Adjacency lists store edges dynamically and take up less memory compared to adjacency matrices.
#
# 7. File System Management
# Use Case: File allocation in storage systems (FAT file systems) uses linked lists to manage files and free space.
# Why? The system can store files in non-contiguous blocks while maintaining links to the next available memory location.
#
# 8. Real-Time Applications (Schedulers in OS)
# Use Case: Operating system schedulers use circular linked lists to cycle through processes in round-robin scheduling.
# Why? Circular linked lists allow continuous looping through processes without needing to reset pointers manually.
#
# 9. Social Media Feeds (Dynamic Content Updates)
# Use Case: News feeds in social media apps (Facebook, Twitter, Instagram) store posts in a linked list-like structure for efficient dynamic updates.
# Why? Linked lists allow easy insertion of new posts at the top without shifting elements like in arrays.
#
# 10. Polynomial Arithmetic and Big Integer Calculations
# Use Case: Scientific computing and cryptography use linked lists for operations on large numbers or polynomial expressions.
# Why? Linked lists allow efficient representation and manipulation of arbitrarily large numbers without overflow issues.
# Why Not Use Arrays Instead?
# ✅ Pros of Linked Lists over Arrays:

# Dynamic memory allocation (no need to define size in advance).
# Efficient insertions and deletions (no need to shift elements).
# No wasted memory due to fixed-size allocation.
# ❌ Cons of Linked Lists:

# Extra memory usage (due to pointers).
# Slower access times (O(n) traversal instead of O(1) random access in arrays).

# -------------------------
import gc
from icecream import ic


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
            self.insert_at_begin(n_data)  # Pass `n_data`
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

print("After Deletions:")
print(l1)

# Testing insert_at_index
l1.insert_at_index(1, "newNode")  # Inserts at index 1
print("After inserting at index 1:")
print(l1)
