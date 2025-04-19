# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

def create_tree(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = create_tree(lst, 2*index + 1)
    root.right = create_tree(lst, 2*index + 2)
    return root

if __name__ == "__main__":
    solution = Solution()
    tree1 = create_tree([2,1,3])
    inverted_tree = solution.invertTree(tree1)
    
    # Helper function to print the tree (for verification)
