class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


node5 = Node("burak", None)
node4 = Node("onur", node5)
node3 = Node("feyza", node4)
node2 = Node("mehmet", node3)
node1 = Node("taha", node2)

# ------

print(node1.data)
print(node1.next)
print(node2)

# -------

cur = node1
while cur:
    print(f"{cur.data} --> ", end="")
    cur = cur.next
print("None")
