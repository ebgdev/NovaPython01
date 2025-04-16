from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Should return 0 for empty tree, not None
        
        max_depth = 0
        
        pass # fill this area
        return max_depth




# Helper function to create a tree from a list (for testing)
def create_tree(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = create_tree(lst, 2*index + 1)
    root.right = create_tree(lst, 2*index + 2)
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Simple balanced tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    tree1 = create_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1 Depth:", solution.maxDepth(tree1))  # Expected: 3
    
    # Test Case 2: Single node
    #     1
    tree2 = create_tree([1])
    print("Test 2 Depth:", solution.maxDepth(tree2))  # Expected: 1
    
    # Test Case 3: Empty tree
    tree3 = create_tree([])
    print("Test 3 Depth:", solution.maxDepth(tree3))  # Expected: 0
    
    # Test Case 4: Left-skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    tree4 = create_tree([1, 2, None, 3])
    print("Test 4 Depth:", solution.maxDepth(tree4))  # Expected: 3
    
    # Test Case 5: Right-skewed tree
    #     1
    #      \
    #       2
    #        \
    #         3
    tree5 = create_tree([1, None, 2, None, None, None, 3])
    print("Test 5 Depth:", solution.maxDepth(tree5))  # Expected: 3