# Tree Traversal : we are going to visit every node in the tree
# and then we are going to take the values and put them in a list and then we'll return that list

# Tree Traversal :
#    - BFS (Breadth First Search - Geniş Öncelikli Arama)
#    - DFS (Depth First Search - Derin Öncelikli Arama)


# DFS :
#   - preorder
#   - preorder
#   - preorder

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

    def bfs(self): # we use queue logic
        current_node = self.root # (47 is our root)
        queue = []
        results = []
        queue.append(current_node) # we put entire node means value and left and right.
        while len(queue) > 0: # we should put the the first node(root) in order to while loop work , it will run until queue gets empty
            current_node = queue.pop(0)
            results.append(current_node.value)
            # and now we should look to the right and left of the node
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results    

    def dfs_pre_order(self): # we use stack logic here
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self): # use stack logic
        # what's different here is that we'are just going to visit that 47 node.
        # we are not going to write that value to the results list yet.
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results




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


print(my_tree.bfs())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())