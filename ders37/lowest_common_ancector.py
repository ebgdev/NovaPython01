# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            

def create_tree(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = create_tree(lst, 2*index + 1)
    root.right = create_tree(lst, 2*index + 2)
    return root

if __name__ == "__main__":
    solution = Solution()

    # FIX 1: Remove extra brackets around the list
    tree_list = [6,2,8,0,4,7,9,None,None,3,5]

    # FIX 2: Build tree correctly
    tree1 = create_tree(tree_list)

    # FIX 3: Define p and q nodes (with same values that exist in the tree)
    p = TreeNode(2)
    q = TreeNode(8)

    # FIX 4: Call function with correct arguments
    ancestor = solution.lowestCommonAncestor(tree1, p, q)

    # Print the result
    print(f"The Lowest Common Ancestor of {p.val} and {q.val} is: {ancestor.val}")
