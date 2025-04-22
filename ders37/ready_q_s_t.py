import queue
from collections import deque
from anytree import Node, RenderTree, PreOrderIter, LevelOrderIter

# QUEUE DEMO
def queue_methods_demo():
    print("=== queue.Queue Methods Demo ===")
    q = queue.Queue(maxsize=3)

    q.put("Task1") # wait or block
    q.put("Task2")
    print("Queue size:", q.qsize())
    print("Is queue empty?", q.empty())
    print("Is queue full?", q.full())

    q.put("Task3")
    print("Is queue full after 3 puts?", q.full())

    try:
        q.put_nowait("Task4")
    except queue.Full:
        print("Queue is full! Cannot add Task4.")

    print("Dequeued:", q.get())
    print("Dequeued (non-blocking):", q.get_nowait())
    print()

# STACK DEMO
def stack_methods_demo():
    print("=== deque Stack Methods Demo ===")
    stack = deque()

    stack.append("Undo1")
    stack.append("Undo2")
    stack.extend(["Undo3", "Undo4"])

    print("Current Stack:", list(stack))
    print("Top item (peek):", stack[-1]) # the most top item

    print("Popped:", stack.pop())
    stack.remove("Undo2")
    print("After remove Undo2:", list(stack))

    stack.clear()
    print("Stack after clear():", list(stack))
    print()

# TREE DEMO
# 'pip3 install anytree' any tree should be installed before


# Node(name, parent=...) | Define tree nodes and relationships
# node.children | Tuple of child nodes
# node.parent | Get the parent node
# RenderTree(root) | Print entire tree structure
# PreOrderIter(node) | Traverse in pre-order
# LevelOrderIter(node) | Traverse level by level


def tree_methods_demo():
    print("=== anytree Methods Demo ===")
    root = Node("CEO")
    mgr1 = Node("Manager1", parent=root)
    mgr2 = Node("Manager2", parent=root)
    dev1 = Node("Dev1", parent=mgr1)
    dev2 = Node("Dev2", parent=mgr1)
    intern = Node("Intern", parent=dev2)

    print("Pre-order traversal:")
    for node in PreOrderIter(root):
        print(node.name)

    print("Level-order traversal:")
    for node in LevelOrderIter(root):
        print(node.name)
    print()

# MAIN
if __name__ == "__main__":
    queue_methods_demo()
    stack_methods_demo()
    tree_methods_demo()
