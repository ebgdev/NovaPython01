class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev  # Pointer to previous node
        self.next = next  # Pointer to next node


# Creating nodes (backward linking)
node5 = Node("burak")
node4 = Node("onur", None, node5)
node5.prev = node4  # Linking back

node3 = Node("feyza", None, node4)
node4.prev = node3

node2 = Node("mehmet", None, node3)
node3.prev = node2

node1 = Node("taha", None, node2)
node2.prev = node1


# Print forward traversal
cur = node1
print("Forward Traversal:")
while cur:
    print(f"{cur.data} --> ", end="")
    cur = cur.next
print("None")

# Print backward traversal (starting from the last node)
cur = node5
print("\nBackward Traversal:")
while cur:
    print(f"{cur.data} --> ", end="")
    cur = cur.prev
print("None")
