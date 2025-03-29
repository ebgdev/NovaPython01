# root : up most elemant in the tree is node
# parent
# child and children
# sibilings : children of the same node are called sibilings
# leaf node : any node in the tree that dosent have child 
# ancestor
# descendent

# we use tree when we need to store data hierarchically.

# by having a tree with N nodes then we'll have max N-1 edges.
# Depth: number of edeges to the specific node is called depth
# height: number of edges in longest path from node to the leaf node , Max(depth )
# Note: height of the leaf node will always be 0


# https://builtin.com/articles/tree-python
# internette bazen yanlis bilgiler goruyorum bunlara dikkat edelim ve her zaman bilgiyi bir kac kaynaktan onaylatalim 


class Node:
    """A class to represent a node in the binary search tree."""
    def __init__(self, value):
        self.value = value  # Node's value
        self.left = None    # Left child (smaller values)
        self.right = None   # Right child (greater values)
        

class BinarySearchTree:
    """A class to represent a Binary Search Tree (BST)."""
    def __init__(self):
        self.root = None  # Root node of the tree

    def insert(self, value):
        """Inserts a new node into the BST."""
        new_node = Node(value)
        if self.root is None:  # If tree is empty, set root as new node
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:  # No duplicate values allowed
                return False
            if new_node.value < temp.value:  # Go left for smaller values
                if temp.left is None:  # Insert if left child is empty
                    temp.left = new_node
                    return True
                temp = temp.left  # Otherwise, keep moving left
            else:  # Go right for larger values
                if temp.right is None:  # Insert if right child is empty
                    temp.right = new_node
                    return True
                temp = temp.right  # Otherwise, keep moving right

    def contains(self, value):
        """Checks if a given value exists in the BST."""
        temp = self.root
        while temp is not None:  # Traverse the tree
            if value < temp.value:  # Search in left subtree
                temp = temp.left
            elif value > temp.value:  # Search in right subtree
                temp = temp.right
            else:
                return True  # Found the value
        return False  # Value not found

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """
        Recursively prints the BST structure in a readable format.
        - node: Current node (default: root)
        - level: Depth level for indentation
        - prefix: Label for child nodes (Root, L-- , R--)
        """
        if node is None:  # Start from the root
            node = self.root
        if node is not None:
            print("  " * level + prefix + str(node.value))  # Print node value
            if node.left:  # Print left subtree
                self.print_tree(node.left, level + 1, "L-- ")
            if node.right:  # Print right subtree
                self.print_tree(node.right, level + 1, "R-- ")

# Example Usage
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# Search for values
print("Contains 27:", my_tree.contains(27))  # Should return True
print("Contains 17:", my_tree.contains(17))  # Should return False

# Print the BST structure
print("\nBinary Search Tree Structure:")
my_tree.print_tree()

