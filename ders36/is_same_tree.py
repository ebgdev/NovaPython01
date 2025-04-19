# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        # return True if both of them are empty
        if not p and not q:
            return True
        # if one of them is None
        if not p or not q:
            return False
        # if values are not the same
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def create_tree(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = create_tree(lst, 2*index + 1)
    root.right = create_tree(lst, 2*index + 2)
    return root

if __name__ == "__main__":
    solution = Solution()

    tree1 = create_tree([1, 2, 3])
    tree2 = create_tree([1, 2, 3])
    print(solution.isSameTree(tree1, tree2))  # True

    tree3 = create_tree([1, 2])
    tree4 = create_tree([1, None, 2])
    print(solution.isSameTree(tree3, tree4))  # False
