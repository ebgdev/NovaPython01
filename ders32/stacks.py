# LIFO : Last In , First Out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def print_stack(self):
        if self.height == 0:
            print("Stack is empty.")
            return
        cur = self.top
        print("Top -> Bottom:")
        while cur:
            print(cur.value)
            cur = cur.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        cur = self.top
        self.top = self.top.next
        cur.next = None
        self.height -= 1
        return cur.value  # Return only the value


# Example Usage:
my_stack = Stack("chrome")
my_stack.push("vscode")
my_stack.push("datagrip")
my_stack.push("pycharm")
my_stack.push("vscode")
print("Popped:", my_stack.pop())
my_stack.print_stack()
